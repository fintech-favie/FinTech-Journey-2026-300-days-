Company = { 
    "finance" : { "lead" : "anshika" , "target" : 50 ,"temp_data" :"xyz" } ,
    "tech": { "lead" : "alex" , "target" : 30 , "temp_data" : "abc" }
}

for dept, details in Company.items():
    if "temp_data" in details:
        del details["temp_data"]
    
    print(f"Updated {dept}: {details}")
