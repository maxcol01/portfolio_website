from flask import Flask, render_template, request, redirect  # type: ignore
import csv

app = Flask(__name__)

def save_data(data):
    with open("database.csv", mode="a", newline="") as file:
        fieldnames = ['email', 'subject', "message"]
            
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)

@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def page_html(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        username = data["email"].split("@")[0]
        try:
            save_data(data=data)
        except:
            return "Did not save to database"

    else:
        print("Something went wrong try again")
    
    return render_template("thankyou.html", username=username)