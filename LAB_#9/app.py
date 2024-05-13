from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('books_read')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(500))
    name_book = db.Column(db.String(500))
    read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id} / {self.author}> {self.name_book}'


@app.route('/')
def main():
    tasks = Task.query.all()
    print(tasks)
    return render_template('books_read.html', tasks_list=tasks)

@app.route('/read/<int:task_id>', methods=['PATCH'])
def modify_task(task_id):
    task = Task.query.get(task_id)
    task.read = request.json['read']
    db.session.commit()
    return 'Ok'

@app.route('/task', methods=['POST'])
def create_task():
    data = request.json
    task = Task(**data)
    db.session.add(task)
    db.session.commit()
    return "ok"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
