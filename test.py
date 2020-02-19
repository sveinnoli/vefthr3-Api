import urllib.request, json # þurfum þennan til að sækja JSON object yfir netið og til að höndla json í py skránni

with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

#-------------------------
# Data dict/list testing
#--------------------------

#print(type(data))

#key_list = list(data.keys())
#print(key_list)

#val_list = list(data.values())
#print(val_list)o

#for key, value in data.items():
    #print("Key: %s\n" "value: %d\n", key, value)

#print(data["results"][0])

#print(len(data["results"])) 

    #print("item number:", item, "\n", data["results"][item], "\n") # Iterates through dict -> list
    #verd = data["results"][item].get("bensin95") #Gets price from results



#---------------------------
# Dictionary Testing
#---------------------------
#thisdict =	{
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#
#for key, value in thisdict.items():
#	print(key, value)