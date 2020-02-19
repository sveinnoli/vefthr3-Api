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
def results(dict_value):
    item_list = []
    for item in range(len(data["results"])):
        dict_item = data["results"][item].get(dict_value)
        if dict_value == "company":
            if dict_item in item_list:
                pass
            else:
                item_list.append(dict_item)
        else:
            item_list.append(dict_item)
    return item_list

data_keys = list(data["results"][0].keys())
price = results(data_keys[0])
price_discount = results(data_keys[1])
company = results(data_keys[2])
diesel = results(data_keys[3])
diesel_discount = results(data_keys[4])
geo = results(data_keys[5])
key = results(data_keys[6])
name = results(data_keys[7])

print(company)
    
#print([data["results"][1].keys()])

data_keys = list(data["results"][0].keys())

#"bensin95": 233.9, 
#      "bensin95_discount": 228.9, 
#      "company": "Atlantsol\u00eda", 
#      "diesel": 226.2, 
#      "diesel_discount": 221.2, 
#      "geo": {
#        "lat": 65.69913, 
#        "lon": -18.135231
#      }, 
#      "key": "ao_000", 
#      "name": "Baldursnes Akureyri"
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