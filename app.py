from flask import Flask, request, jsonify

app = Flask(__name__)

# دیتابیس ساده از عطرها بر اساس حس و حال
perfume_recommendations = {
    "شاد": {"name": "Dior Joy", "link": "https://yourwebsite.com/dior-joy"},
    "غمگین": {"name": "Tom Ford Black Orchid", "link": "https://yourwebsite.com/black-orchid"},
    "انرژی‌بخش": {"name": "Chanel Chance", "link": "https://yourwebsite.com/chanel-chance"},
    "آرامش‌بخش": {"name": "YSL Libre", "link": "https://yourwebsite.com/ysl-libre"},
}

@app.route("/recommend", methods=["POST"])
def recommend_perfume():
    data = request.json
    mood = data.get("mood", "").strip()

    recommendation = perfume_recommendations.get(mood, None)
    
    if recommendation:
        response = {
            "message": f"بر اساس حس و حال شما، پیشنهاد ما {recommendation['name']} است.",
            "link": recommendation["link"]
        }
    else:
        response = {
            "message": "متأسفم، عطر مناسبی برای این حس و حال در دیتابیس ما پیدا نشد.",
            "link": None
        }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
