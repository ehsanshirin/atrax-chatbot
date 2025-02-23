from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/recommend", methods=["POST"])  # 👈 باید روش POST در اینجا باشد
def recommend_perfume():
    data = request.get_json()
    if not data or "mood" not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    mood = data["mood"]
    
    # پاسخ نمونه
    response = {
        "message": f"بهترین عطر برای حالت {mood}، عطر X است!",
        "link": "https://yoursite.com/product/perfume-x"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
