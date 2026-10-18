from flask import Flask, jsonify, request, render_template
from roman import convert, to_roman

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/convert")
def api_convert():
    s = request.args.get("roman", "").strip().upper()
    try:
        return jsonify(roman=s, value=convert(s))
    except ValueError as e:
        return jsonify(error=str(e)), 400


@app.route("/api/to_roman")
def api_to_roman():
    raw = request.args.get("number", "").strip()
    try:
        n = int(raw)
    except ValueError:
        return jsonify(error="Lütfen bir tam sayı gir"), 400
    try:
        return jsonify(number=n, roman=to_roman(n))
    except ValueError as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(debug=True)