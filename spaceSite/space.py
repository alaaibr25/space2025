from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def space_page():
    return render_template("space.html")

@app.route("/destination")
def destination_page():
    return render_template("destination.html")


@app.route("/crew")
def crew_page():
    return render_template("crew.html")



@app.route("/tech")
def tech_page():
    return render_template("tech.html")


















app.run(debug=True)
























