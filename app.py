from flask import Flask, jsonify, request
app= Flask(__name__)
task= [
    {
        "id": 1,
        "title": "buy groceries",
        "description": "milk, cheese, pizza, fruit",
        "done": False
    },

{
        "id": 2,
        "title": "learn python",
        "description": "need to find good python books on web",
        "done": False
}
]

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/add-data",methods= ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)
    tasks= {
        "id": task[-1]["id"] +1,
        "title": request.json["title"],
        "description": request.json.get("description",""),
        "done": False
    }
    task.append(tasks)
    return jsonify({
            "status": "success",
            "message": "task added successfully"
        })

@app.route("/get-data")
def get_task ():
    return jsonify({
        "data": task
    })

if(__name__ == "__main__"):
    app.run(debug= True)
