import json


users = {}

def register_user(username: str, password: str) -> str:
    """
    Register a new user with a username and password.
    Returns JSON: {"success": bool, "message": str}
    """
    if username in users:
        return json.dumps({"success": False, "message": "User already exists"})
    users[username] = password
    return json.dumps({"success": True, "message": "User registered successfully"})


def login_user(username: str, password: str) -> str:
    """
    Log in a user with username and password.
    Returns JSON: {"success": bool, "message": str}
    """
    if users.get(username) == password:
        return json.dumps({"success": True, "message": "Login successful"})
    return json.dumps({"success": False, "message": "Invalid username or password"})


def logout_user(username: str) -> str:
    """
    Log out a user.
    Returns JSON: {"success": bool, "message": str}
    """
 
    return json.dumps({"success": True, "message": "Logout successful"})




