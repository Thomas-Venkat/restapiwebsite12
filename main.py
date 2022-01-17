from flask import Flask, jsonify, render_template
import requests
import json

app = Flask(__name__)

access_token = "31zD6AfpfJ86qrZJaayG"

@app.route('/', methods=["GET","POST"])
def home():
    # pass
    req = requests.get("https://the-one-api.dev/v2/book")
    data = req.content
    print(data)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

# req = requests.get("https://the-one-api.dev/v2/book")
# data = json.loads(req.content)
# print(data)