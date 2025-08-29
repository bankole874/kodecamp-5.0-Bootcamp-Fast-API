import json
import os
import argparse
from passlib.context import CryptContext

# Path for storing users
USERS_FILE = os.getenv("USERS_FILE", "users.json")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)


def add_user(username, password):
    users = load_users()
    if username in users:
        print(f"User '{username}' already exists — updating password.")
    hashed = pwd_context.hash(password)
    users[username] = {"username": username, "hashed_password": hashed}
    save_users(users)
    print(f"✅ User '{username}' saved to {USERS_FILE}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    args = parser.parse_args()
    add_user(args.username, args.password)
