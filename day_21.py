file_no = 1
print("starting file processing")
while file_no <= 10:
	if file_no ==7:
		print("critical error :{file_no}")
		break
		print(f"processing file {file_no}....[ok]")
		file_no = file_no + 1
		print("process terminated successfully")