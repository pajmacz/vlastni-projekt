from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
	odpoved = None
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
		heslo=request.form.get("heslo")
		spravne_heslo="Pavel Doležal"
		if heslo==spravne_heslo:
			odpoved="správná"
			session["pocet_pokusu"] = 0
		else:
			odpoved="špatná"
			pocet_pokusu += 1
			session["pocet_pokusu"] = pocet_pokusu
	return render_template("uvodni.html", odpoved=odpoved, pocet_pokusu=pocet_pokusu)

if __name__=="__main__":
	app.run(debug=True)