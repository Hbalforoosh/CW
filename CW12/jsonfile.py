import json

users = [
    {'username': 'hacker007', 'age': 22, 'posts': 0,
        'followers': 5000, 'action': True},
    {'username': 'spam_bot',  'age': 0,  'posts': 2000,
        'followers': 2,    'action': False},
    {'username': 'ghost',     'age': 19, 'posts': 0,
        'followers': 0,    'action': True}
]


with open("./users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
