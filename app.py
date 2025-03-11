from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your API Key

def get_address(latitude, longitude):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "results" in data and data["results"]:
        return data["results"][0]["formatted_address"]
    return "Address not found"

@app.route("/log_location", methods=["POST"])
def log_location():
    data = request.get_json()
    latitude, longitude = data.get("latitude"), data.get("longitude")

    if latitude and longitude:
        address = get_address(latitude, longitude)
        return jsonify({"status": "success", "latitude": latitude, "longitude": longitude, "address": address}), 200

    return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True)
