Company = { "finance" : { "lead" : "anshika","target" : 50 , "status" : "acitve" 
} , 
"tech": {"lead" : "alex" , "target" : 30 , "status" : "hiring" 
},
}
for dept , details in Company.items( ) :
	details["status"] = "verified"
	details["target"] = details["target"] + 5
	for dept , details in Company.items( ) :
		print(f"{dept.upper()}: Target is now {details['target']}LPA ({details['status']})")
	
