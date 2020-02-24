import urllib.request, json # þurfum þennan til að sækja JSON object yfir netið og til að höndla json í py skránni

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

newDict = {"companyData":[{}]}
newDict["companyData"][0]["hi"] = "ok"
newDict["companyData"][0]["er"] = "no"

def companyInfo(company):
    #company_info ={"myData":[{}]}
    company_info = [{}]
    itemCounter = 0
    data_list = data["results"]
    for dict_item in data_list:
        for key, value in dict_item.items():
            if value == "Orkan":
                company_info[itemCounter]["company"] = dict_item.get("company")
                company_info[itemCounter]["name"] = dict_item.get("name")
            else:
                pass
    return company_info

print(companyInfo("Orkan"))

level1 = {'value1':0, 'value2':0, 'value3':0}
level2 = {'value1':0, 'value2':0, 'value3':0}
level3 = {'value1':0, 'value2':0, 'value3':0}
level3 = {'value1':0, 'value2':0, 'value3':0}

dic={}
for x in range (1,6):
    level = 'ok%d' % x 
    dic[level] = {}
    for iteration in range(1, 4): 
        value = 'value%d' % iteration
        dic[level][value] = 0 
print (dic)