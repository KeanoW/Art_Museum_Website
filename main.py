from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("employee/Events.html")

@app.route("/requests")
def requests():
    return render_template("cleaner/Requests.html")

@app.route("/request")
def request():
    return render_template("employee/CreateRequest.html")

if __name__ == '__main__':
    app.run(debug=True)
