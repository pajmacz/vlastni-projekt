from flask import Flask, render_template, request, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
	odpoved = None
	chyba = None
	current_route = request.path
	last_route = session.get("last_route", None)
	
	# Pokud se změní stránka, resetuj počet pokusů
	if last_route != current_route:
		pocet_pokusu = 0
		session["pocet_pokusu"] = 0
		session["last_route"] = current_route
	else:
		pocet_pokusu = session.get("pocet_pokusu", 0)
	
	if request.method == "POST":
		heslo = request.form.get("heslo", "").strip()
		if not heslo:
			chyba = "Prosím, zadej něco!"
		elif heslo=="Pavel Doležal" or heslo=="pavel doležal" or heslo=="PAVEL DOLEŽAL":
			odpoved="správná"
			session["pocet_pokusu"] = 0
		else:
			odpoved="špatná"
			pocet_pokusu += 1
			session["pocet_pokusu"] = pocet_pokusu
	return render_template("uvodni.html", odpoved=odpoved, pocet_pokusu=pocet_pokusu, chyba=chyba)

@app.route("/syr", methods=["GET", "POST"])
def syr():
	odpoved = None
	chyba = None
	current_route = request.path
	last_route = session.get("last_route", None)
	
	# Pokud se změní stránka, resetuj počet pokusů
	if last_route != current_route:
		pocet_pokusu = 0
		session["pocet_pokusu"] = 0
		session["last_route"] = current_route
	else:
		pocet_pokusu = session.get("pocet_pokusu", 0)
	
	if request.method == "POST":
		heslo = request.form.get("heslo", "").strip()
		if not heslo:
			chyba = "Prosím, zadej něco!"
		elif heslo=="knír" or heslo=="knir" or heslo=="Knír" or heslo=="Knir":
			odpoved="správná"
			session["pocet_pokusu"] = 0
		else:
			odpoved="špatná"
			pocet_pokusu += 1
			session["pocet_pokusu"] = pocet_pokusu
	return render_template("syr.html", odpoved=odpoved, pocet_pokusu=pocet_pokusu, chyba=chyba)

@app.route("/nepritel", methods=["GET", "POST"])
def nepritel():
	odpoved = None
	chyba = None
	current_route = request.path
	last_route = session.get("last_route", None)
	
	# Pokud se změní stránka, resetuj počet pokusů
	if last_route != current_route:
		pocet_pokusu = 0
		session["pocet_pokusu"] = 0
		session["last_route"] = current_route
	else:
		pocet_pokusu = session.get("pocet_pokusu", 0)
	
	if request.method == "POST":
		heslo = request.form.get("heslo", "").strip()
		if not heslo:
			chyba = "Prosím, zadej něco!"
		elif heslo=="vašek" or heslo=="Vašek" or heslo=="Vašek Trávníček" or heslo=="vašek trávníček" or heslo=="VAŠEK TRÁVNÍČEK":
			odpoved="správná"
			session["pocet_pokusu"] = 0
		else:
			odpoved="špatná"
			pocet_pokusu += 1
			session["pocet_pokusu"] = pocet_pokusu
	return render_template("nepritel.html", odpoved=odpoved, pocet_pokusu=pocet_pokusu, chyba=chyba)

if __name__=="__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, debug=False)