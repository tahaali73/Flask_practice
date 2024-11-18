from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

SPORTS=["circket", "football", "basketball"]

@app.route("/")
def form():
    return render_template("form.html", sports=SPORTS)

@app.route("/success", methods=["POST"])
def success():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    sports = request.form.get("sport")
    if sports not in SPORTS:
        return render_template("/failure.html")
    
    conn = get_db_connection()
    conn.execute("insert into games(name,sports) values(?, ?)",(name, sports))
    conn.commit()
    conn.close()

    return render_template("formConfirm.html")

@app.route("/registrants")
def reg():
    conn = get_db_connection()
    participants = conn.execute("select * from games").fetchall()
    conn.close()
    return render_template("registrants.html", registrant=participants)

@app.route("/deregister", methods=["POST"] )
def deregistrant():
    id = request.form.get("id")
    conn = get_db_connection()
    conn.execute("DELETE FROM games WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/registrants")


if __name__ == "__main__":
    app.run()