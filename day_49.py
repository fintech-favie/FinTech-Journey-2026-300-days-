print("continuous tracker")
while True:
	task=input("\n enter task name (or type'exit' to stop):")
	if task.lower()=="exit": 
		print("closing the engine good bye...")
		hours= float(input(f"hours spent on {task}"))
		if hours >=5:
			print("status : deep work")
		else:
				print("status:quick progress")
				print("----engine stopped----")