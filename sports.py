from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS=["circket", "football", "basketball"]
PARTICIPANTS={}

@app.route("/")
def form():
    return render_template("form.html", sports=SPORTS)

@app.route("/success", methods=["POST"])
def success():
    name = request.form.get("name")
    if not name in PARTICIPANTS:
        return render_template("failure.html")
    sports = request.form.get("sport")
    if sports not in SPORTS:
        return render_template("/failure.html")
    PARTICIPANTS[name] = sports
    return render_template("formConfirm.html")

@app.route("/registrants")
def reg():
    return render_template("registrants.html", registrants=PARTICIPANTS)

if __name__ == "__main__":
    app.run()