from flask import Flask, jsonify 

app = Flask(__name__)

@app.route("/Elamparithi", methods=["GET"])
def profile():
    skills = ["DevOps", "Python", "Aws", "Sql", "Kubernetes"]
    like = ["Fitness", "Cricket", "Chess"]
    data = {}

    # Adding skills to data
    for i in range(len(skills)):
        name = f"skill{i + 1}"
        data[name] = skills[i]

    # Adding likes to data
    sports_likes = [f"He likes this sport: {i + 1}. {like[i]}" for i in range(len(like))]
    data["sports_likes"] = sports_likes

    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
