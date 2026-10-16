import os


# Credentials
USER_CREDENTIALS = {
    os.getenv("USER1_NAME", "Usuario 1"): os.getenv("USER1_PASS", "admin123"),
    os.getenv("USER2_NAME", "Usuario 2"): os.getenv("USER2_PASS", "admin123"),
}
USERS = list(USER_CREDENTIALS.keys())