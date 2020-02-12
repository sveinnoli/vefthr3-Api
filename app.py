from flask import Flask, render_template
import urllib.request, json # þurfum þennan til að sækja JSON object yfir netið og til að höndla json í py skránni
app = Flask(__name__)


# rútínan hérna fyrir neðan fer á url, sækir JSON object og setur í url breytuna
# json.loads hendir JSON obect yfir í dictionary sem við vinnum með í .py skrá
# Data er Dictionary sem inniheldur lista "results" sem inniheldur dictionary, þar eru gögnin sem eru þörf á.
with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

@app.route('/')
def index():
	# print(type(data)) debug, sjáum hvaða týpa data er = dict
	return data

if __name__ == "__main__":
	app.run(debug=True)