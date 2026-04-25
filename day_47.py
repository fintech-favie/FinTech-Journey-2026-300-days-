Social = {
    "user_101": {"username": "favie", "posts": 250, "active": True},
    "user_102": {"username": "alex_dev", "posts": 90, "active": False},
    "user_103": {"username": "pro", "posts": 150, "active": True},
    "user_104": {"username": "ghost_user", "posts": 0, "active": False}
}
cleanup_queue = [ ]
for user_id, info in Social.items( ):
	if info["active"] == False:
		cleanup_queue.append(user_id)
		print("cleanup required")
		print(f"the following ID's are inactive:{cleanup_queue}")
		print(f"Total accounts to review:{len(cleanup_queue)}")