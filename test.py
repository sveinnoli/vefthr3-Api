import urllib.request, json, time, datetime, # þurfum þennan til að sækja JSON object yfir netið og til að höndla json í py skránni

with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

#-------------------------
# Data dict/list testing
#--------------------------
#data_list = data["results"]
#for item in data_list:
#    for key, value in item.items():
#        if value == "Orkan":
#            print(item.get("company"))
#            print(item.get("name"))
#        else:
#            pass




name = {"results":[{"bensin95":235.9,"bensin95_discount":230.9,"company":"Atlantsolía","diesel":227.2,"diesel_discount":222.2,"geo":{"lat":65.69913,"lon":-18.135231},"key":"ao_000","name":"Baldursnes Akureyri"}]}

myDict = {"items":[{"gas":"expensive", "bones":"cool"}, {"gas":"cheap", "bones":"hot"}]}

#for key,value in myDict["items"][0].items():
    #print(key, value)


datalist = data["results"]
lastPrice = data["timestampPriceChanges"]
