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


#print([data["results"][1].keys()])


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

image_list = ["/static/images/Atlantsolía.png", "/static/images/Costco Iceland.png", "/static/images/Dælan.png", "/static/images/N1.png", "/static/images/ÓB.png", "/static/images/Olís.png", "/static/images/Orkan.png"]

image_dict = {"Atlantsolía":"/static/images/Atlantsolía.png", "Costco Iceland": "/static/images/Costco Iceland.png", "Dælan":"/static/images/Dælan.png", "N1":"/static/images/N1.png", "Olís":"/static/images/Olís.png","Orkan":"/static/images/Orkan.png" }

company_images={"Atlantsolía":"lol", "Olís":"195"}
for key,value in image_dict.items():
    print(key)

company_images.update(Atlantsolía = "image")
