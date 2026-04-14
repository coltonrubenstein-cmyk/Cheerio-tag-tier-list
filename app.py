from flask import Flask, render_template, request, jsonify
from github_utils import pull_from_github, push_to_github

app = Flask(__name__)
data = pull_from_github()

@app.route('/')
def index():
    return render_template("index.html", players=data["players"])

@app.route('/add_player', methods=['POST'])
def add_player():
    name = request.json['name']
    role = request.json['role']
    data["players"].append({"name": name, "points": 0, "role": role})
    push_to_github(data)
    return jsonify(data["players"])

@app.route('/adjust_points', methods=['POST'])
def adjust_points():
    name = request.json['name']
    delta = request.json['delta']
    for player in data["players"]:
        if player["name"] == name:
            player["points"] += delta
            break
    push_to_github(data)
    return jsonify(data["players"])

if __name__ == "__main__":
    app.run(debug=True)
