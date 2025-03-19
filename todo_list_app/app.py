from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    tasks.append({"task": task, "done": False})
    return redirect(url_for("index"))

@app.route("/mark_done/<int:task_id>")
def mark_done(task_id):
    tasks[task_id]["done"] = True
    return redirect(url_for("index"))

@app.route("/remove/<int:task_id>")
def remove_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
