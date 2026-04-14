from flask import Flask, request, jsonify
from .service import add_student, get_students, get_student
from exceptions import StudentNotFoundException

app = Flask(__name__)


@app.route("/students", methods=["POST"])
def create_student():

    data = request.json
    student = add_student(data["id"], data["name"])

    return jsonify(student)


@app.route("/students", methods=["GET"])
def students():

    return jsonify(get_students())


@app.route("/students/<int:student_id>", methods=["GET"])
def student(student_id):

    try:
        return jsonify(get_student(student_id))

    except StudentNotFoundException as e:
        return jsonify({"error": str(e)}), 404


if __name__ == "__main__":
    app.run(port=5000, debug=True)