from flask import Flask, render_template
import urllib.request, json #Gets json objects
app = Flask(__name__)
with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

#----- Appends data from dictionary into a list -----
def list_results(dict_value, sorting=False):
    item_list = []
    for item in range(len(data["results"])):
        dict_item = data["results"][item].get(dict_value)
        if dict_value == "company" and sorting==True: 
            if dict_item in item_list:
                pass
            else:
                item_list.append(dict_item)
        else:
            item_list.append(dict_item)
    return item_list

# Checks to make sure that company is still in dataset, if it's not present the logo will not appear on the Homepage
def CompanyExists(company, company_image):
    image_list = {}
    for x in range(len(company)):
        for key, value in company_image.items():
            if key == company[x]:
                image_list[company[x]] = value
            else:
                pass
    return image_list


# 0=price, 1=price_discount, 2=company, 3=diesel, 4=diesel_discount, 5=geo, 6=key, 7=name:
data_keys = list(data["results"][0].keys()) 
company = list_results(data_keys[2], True) 
company_image = {"Atlantsolía":"/static/images/Atlantsolía.png", "Costco Iceland": "/static/images/Costco Iceland.png", "Dælan":"/static/images/Dælan.png", "N1":"/static/images/N1.png", "ÓB": "/static/images/ÓB.png","Olís":"/static/images/Olís.png","Orkan":"/static/images/Orkan.png" }

#Code for company location
def companyInfo(company):
    item_dict = {}
    data_list = data["results"]
    for item in data_list:
        for key, value in item.items():
            if value == "Orkan":
                print(item.get("company"))
                print(item.get("name"))
                item_dict["company"] = item.get("company")
                item_dict["name"] = item.get("name")
            else:
                pass
    return item_dict

@app.route('/')
def index():
	return render_template("gasvakt.html", company=CompanyExists(company,company_image))

@app.route('/company/<gasCompany>')
def station(gasCompany):
    return render_template("station.html",gasCompany=gasCompany)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)