import pytest
from CW12 import UserFiltering
import json

u = UserFiltering("users.json")


def test_active():
    users = [
        {
            "username": "hacker007",
            "age": 22,
            "posts": 0,
            "followers": 5000,
            "action": True
        },
        {
            "username": "spam_bot",
            "age": 0,
            "posts": 2000,
            "followers": 2,
            "action": False
        },
        {
            "username": "ghost",
            "age": 19,
            "posts": 0,
            "followers": 0,
            "action": True
        }
    ]
    result = u._process_users(users)
    assert len(result) == 2
    assert all(user["action"] for user in users)
    assert any(user["username"] == "hacker" for user in users
