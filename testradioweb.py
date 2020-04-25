from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<html><head><title>TestRadio</title><meta charset='UTF-8'></head><body>LiSTEN @ /static/radio.m3u !</body></html>"

if __name__ == "__main__":
    app.run(port=8081)