Social_app = {
    "user_101": {"username": "favie", "posts": 25},
    "user_102": {"username": "alex_dev", "posts": 10},
    "user_103": {"username": "pro", "posts": 42}
}

for id, data in Social_app.items():
    if data["posts"] > 30:
        data["verified"] = True
    else:
        data["verified"] = False

import pprint
pprint.pprint(Social_app)
