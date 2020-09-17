try:
    import json
    from flask import Flask, render_template,make_response
    import requests
    import json
    print("ALl modules Loaded ")
except Exception as e:
    print("Error : {} ".format(e))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/pipe', methods=["GET", "POST"])
def pipe():
    payload = {}
    headers = {}
    url = "https://demo-live-data.highcharts.com/aapl-ohlcv.json"
    r = requests.get(url, headers=headers, data ={})
    r = r.json()
    return {"res":r}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)