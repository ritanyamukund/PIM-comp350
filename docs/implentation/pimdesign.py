def register_user(username: str, password: str) -> str
"""
Register a new user.
Returns JSON: {"success": bool, "message": str}
"""

def login_user(username: str, password: str) -> str
"""
Authenticate an existing user.
Returns JSON: {"success": bool, "message": str}
"""

def logout_user(username: str) -> str
"""
Log out the given user.
Returns JSON: {"success": bool, "message": str}
"""

def create_note(username: str, title: str, content: str) -> str
"""
Create a new note for a user.
Returns JSON: {"success": bool, "message": str}
"""

def get_note(username: str, title: str) -> str
"""
Retrieve a note by title for a user.
Returns JSON: {"success": bool, "note": dict or None}
"""

def in_place_viewer(username: str, title: str) -> str
"""
In-place viewer: show a short preview of the note content.
Returns JSON: {"success": bool, "title": str, "preview": str, "date": str}
"""

def particle_viewer(username: str, title: str) -> str
"""
Full viewer: show the complete note.
Returns JSON: {"success": bool, "title": str, "content": str, "date": str}
"""


def edit_note(username: str, title: str, new_content: str) -> str
"""
Edit the content of a user’s note.
Returns JSON: {"success": bool, "message": str}
"""

def search_articles(username: str, query: str) -> str
"""
Search articles by keyword in title or body for a user.
Returns JSON: {"success": bool, "results": list[dict]}
Each result has {"id": int, "date": str, "title": str}
"""

def delete_note(username: str, title: str) -> str
"""
Delete a note by title for a user.
Returns JSON: {"success": bool, "message": str}
"""