from flask import Flask, render_template
import urllib.request, json # þurfum þennan til að sækja JSON object yfir netið og til að höndla json í py skránni
app = Flask(__name__)

# rútínan hérna fyrir neðan fer á url, sækir JSON object og setur í url breytuna
# json.loads hendir JSON obect yfir í dictionary sem við vinnum með í .py skrá
# Data er Dictionary sem inniheldur lista "results" sem inniheldur dictionary, þar eru gögnin sem eru þörf á.
with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

#----- Data -----
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
    

@app.route('/')
def index():
	# print(type(data)) debug, sjáum hvaða týpa data er = dict
	return data

if __name__ == "__main__":
	app.run(debug=True)