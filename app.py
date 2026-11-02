
from flask import Flask, request, render_template
import requests
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        url = request.form["url"]

        start = time.time()

        try:
            response = requests.get(url)
            end = time.time()

            result = "Status Code: " + str(response.status_code)
            result += "<br>Response Time: " + str(round((end-start)*1000, 2)) + " ms"

        except:
            result = "API is not working"

    return render_template("index.html", result=result)

app.run(debug=True)
