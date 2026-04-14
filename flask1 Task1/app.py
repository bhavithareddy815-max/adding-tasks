from flask import Flask, render_template, request, redirect, url_for
from repository.student_repository import insert_student, get_all_students
app = Flask(__name__)
@app.route("/")
def register_page():
    return render_template("register.html")
@app.route("/register", methods=["POST"])
def register_student():
    name = request.form.get("name")
    email = request.form.get("email")
    dob = request.form.get("dob")
    department = request.form.get("department")
    phone = request.form.get("phone")
    insert_student(name, email, dob, department, phone)
    return redirect(url_for("students_page"))
@app.route("/students")
def students_page():
    students = get_all_students()
    return render_template("students.html", students=students)
if __name__ == "__main__":
    app.run(debug=True)
