from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    age = int(data["age"])
    chol = int(data["chol"])
    bp = int(data["bp"])
    sex = data["sex"]

    # Heart Rate Prediction
    heart_rate = round(220 - age - (chol / 10))

    # Risk Score Prediction (0 to 1)
    risk_score = round(
        (age / 100) + (chol / 300) + (bp / 200),
        2
    )

    return jsonify({
        "heart_rate": heart_rate,
        "risk_score": risk_score,
        "features": {
            "age": age,
            "chol": chol,
            "bp": bp
        }
    })

if __name__ == "__main__":
    app.run(debug=True)

