from flask import Flask, render_template, request, redirect
from models import db, Student
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        email = request.form['email']

        new_student = Student(name=name, department=department, email=email)
        db.session.add(new_student)
        db.session.commit()

        return redirect('/')

    return render_template('add_student.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.name = request.form['name']
        student.department = request.form['department']
        student.email = request.form['email']

        db.session.commit()
        return redirect('/')

    return render_template('edit_student.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)