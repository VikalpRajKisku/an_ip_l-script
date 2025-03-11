# IP Grabber

This project is a simple IP tracking and logging system built with Flask. It allows users to capture IP addresses and geolocation data using an API.

## Features
- Collects and logs IP addresses.
- Retrieves geolocation data based on IP.
- Uses Flask as a backend.
- Can be deployed using Ngrok or GitHub Pages (frontend only).

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip
- Virtual environment (venv)

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ip-grabber.git
   cd ip-grabber
   ```

2. **Create and activate a virtual environment:**
   - On Windows (PowerShell):
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. **Start the Flask server:**
   ```bash
   python app.py
   ```
2. The server will run on `http://127.0.0.1:5000/`

## Deployment
### **Using Ngrok for External Access**
If you want to expose your Flask app to the internet temporarily, use **Ngrok**:
```bash
ngrok http 5000
```
Ngrok will generate a public URL that you can use to access the service remotely.

## API Endpoints
| Method | Endpoint         | Description              |
|--------|----------------|--------------------------|
| POST   | `/log_location` | Logs IP and geolocation |

## Issues and Contributions
If you find any issues or want to contribute, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

---
Feel free to modify the repository link and customize the details based on your exact setup!

