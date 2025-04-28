from flask import Flask, render_template, request, jsonify
import requests
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Use environment variable for backend URL
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "https://healthcare-api-backend.onrender.com/api")

@app.route('/')
def index():
    app.logger.debug("Serving index.html")
    return render_template('index.html')

@app.route('/create_program', methods=['GET', 'POST'])
def create_program():
    if request.method == 'POST':
        data = request.get_json()
        app.logger.debug("POST /create_program received: %s", data)
        response = requests.post(f"{BACKEND_API_URL}/programs", json=data)
        app.logger.debug("Backend response: %s", response.status_code)
        return jsonify(response.json()), response.status_code
    app.logger.debug("Serving create_program.html")
    return render_template('create_program.html', active_page='create_program')

@app.route('/register_client', methods=['GET', 'POST'])
def register_client():
    if request.method == 'POST':
        data = request.get_json()
        app.logger.debug("POST /register_client received: %s", data)
        response = requests.post(f"{BACKEND_API_URL}/clients", json=data)
        return jsonify(response.json()), response.status_code
    return render_template('register_client.html',active_page='register_client')

@app.route('/enroll_client', methods=['GET', 'POST'])
def enroll_client():
    if request.method == 'POST':
        data = request.get_json()
        app.logger.debug("POST /enroll_client received: %s", data)
        response = requests.post(f"{BACKEND_API_URL}/enrollments", json=data)
        return jsonify(response.json() if response.content else {}, response.status_code)
    return render_template('enroll_client.html',active_page='enroll_client')

@app.route('/search_client', methods=['GET', 'POST'])
def search_client():
    if request.method == 'POST':
        data = request.get_json()
        app.logger.debug("POST /search_client received: %s", data)
        response = requests.get(f"{BACKEND_API_URL}/clients/search", params=data)
        return jsonify(response.json()), response.status_code
    return render_template('search_client.html',active_page='search_client')

@app.route('/view_profile/<client_id>')
def view_profile(client_id):
    app.logger.debug("Serving view_profile.html for client_id: %s", client_id)
    return render_template('view_profile.html', client_id=client_id)

@app.route('/api/client/<client_id>')
def get_client(client_id):
    app.logger.debug("GET /api/client/%s", client_id)
    response = requests.get(f"{BACKEND_API_URL}/clients/{client_id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)