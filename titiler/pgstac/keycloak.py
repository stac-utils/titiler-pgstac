from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from keycloak import KeycloakOpenID
import requests
import logging

import os

DEV_ALLOWED_ORIGINS = {"http://ares.local"}
DEV_ALLOWED_ROLES = {"ares-admin", "ares-user"}

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Keycloak configuration
# KEYCLOAK_SERVER_URL = "http://10.5.0.0:8080"
# KEYCLOAK_REALM = "fastapi-realm"
# KEYCLOAK_CLIENT_ID = "stac-api-client"
# KEYCLOAK_CLIENT_SECRET ="None"  # Use None for public clients
# #KEYCLOAK_CLIENT_SECRET = "Gbpnp5W0by7xmyuFcnIcC6GCtkPVgeXL"
# ALGORITHM = "RS256"

KEYCLOAK_SERVER_URL = os.environ["KEYCLOAK_SERVER_URL"]
KEYCLOAK_REALM = os.environ["KEYCLOAK_REALM"]
KEYCLOAK_CLIENT_ID = os.environ["KEYCLOAK_CLIENT_ID"]
KEYCLOAK_CLIENT_SECRET =os.environ["KEYCLOAK_CLIENT_SECRET"]  # Use None for public clients
#KEYCLOAK_CLIENT_SECRET = "Gbpnp5W0by7xmyuFcnIcC6GCtkPVgeXL"
ALGORITHM = os.environ["ALGORITHM"]

# Initialize KeycloakOpenID
keycloak_openid = KeycloakOpenID(
    server_url=f"{KEYCLOAK_SERVER_URL}",
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM,
    client_secret_key=KEYCLOAK_CLIENT_SECRET,
    verify=True
)
config_well_known = keycloak_openid.well_known()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        logger.info("Attempting production token verification...")
        logger.info(f"Token Data Type: {type(token)}")
        logger.info(f"Token Value: {token}")
        # Try production verification first
        decoded_token = keycloak_openid.decode_token(
            token,validate=True,
        )
        username = decoded_token['preferred_username']
        logger.info(f"Decoded token: {decoded_token}")
        # Verify the issuer claim
        issuer = decoded_token["iss"]
        
        expected_issuer = f"{KEYCLOAK_SERVER_URL.rstrip('/')}/realms/{KEYCLOAK_REALM}"
        if issuer != expected_issuer:
            logger.error(f"Issuer mismatch: got {issuer}, expected {expected_issuer}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid issuer")
        
        logger.info(f"username: {username}")
        return decoded_token
    except Exception as e:
        logger.warning(f"Prod Keycloak token validation failed: {e}. Attempting dev token fallback...")

        try:
            # Decode without verifying signature
            unverified_claims = jwt.get_unverified_claims(token)

            allowed_origins = set(unverified_claims.get("allowed-origins", []))
            roles = set(unverified_claims.get("realm_access", {}).get("roles", []))

            if DEV_ALLOWED_ORIGINS & allowed_origins and DEV_ALLOWED_ROLES & roles:
                logger.info("Dev token accepted based on allowed origins and roles.")
                return unverified_claims
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        except Exception as dev_e:
            logger.error(f"Dev token validation failed: {dev_e}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Extracts the user from the token after verification."""
    payload = verify_token(token)
    
    # Retrieve user information from the token payload
    user_id = payload.get("sub")
    username = payload.get("preferred_username")
    email = payload.get("email")
    roles = payload.get("realm_access", {}).get("roles", [])
    
    if not user_id or not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User information not found in token")
    
    # Create a user object or dictionary (customize this based on your needs)
    user = {
        "id": user_id,
        "username": username,
        "email": email,
        "roles": roles
    }
    
    return user

def add_swagger_config(app: FastAPI):
        """Adds the client id and secret securely to the swagger ui.
        Args:
            app (FastAPI): Optional FastAPI app to add the config to swagger
        Returns:
            None: Inplace method
        """        
        app.swagger_ui_init_oauth = {
            "usePkceWithAuthorizationCodeGrant": True,
            "clientId": KEYCLOAK_CLIENT_ID,
            "clientSecret": KEYCLOAK_CLIENT_SECRET,
        }