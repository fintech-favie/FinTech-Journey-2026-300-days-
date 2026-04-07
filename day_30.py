Status = { "name" : "anshika" , "balance" : 1000 ,  " active " : True }
Status["balance"] = 1250
Status["lastwin"] = "XAU/USD"
del Status[" active "]
print(Status)
