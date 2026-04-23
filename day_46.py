Social_app = {
    "user_101": {"username": "favie", "posts": 250, "active": True},
    "user_102": {"username": "alex_dev", "posts": 90, "active": True},
    "user_103": {"username": "pro", "posts": 150, "active": True},
    "user_104": {"username": "member_x", "posts": 20, "active": True}
}

vip_list = [info["username"] for info in Social_app.values() if info["posts"] > 100]

print("--- VIP USER LIST ---")
print(vip_list)
print(f"We have {len(vip_list)} users ready for the reward!")
