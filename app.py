from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task', '').strip()
    if task_text:
        tasks.append({"text": task_text, "done": False})
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

@app.route('/complete/<int:index>', methods=['POST'])
def complete(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index].get('done', False)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)