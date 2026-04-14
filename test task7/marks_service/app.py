from flask import Flask, request, jsonify
from .service import add_marks, get_marks
from exceptions import MarksNotFoundException

app = Flask(__name__)


@app.route("/marks", methods=["POST"])
def create_marks():

    data = request.json

    result = add_marks(
        data["student_id"],
        data["subject"],
        data["marks"]
    )

    return jsonify(result)


@app.route("/marks/<int:student_id>", methods=["GET"])
def marks(student_id):

    try:
        return jsonify(get_marks(student_id))

    except MarksNotFoundException as e:
        return jsonify({"error": str(e)}), 404


if __name__ == "__main__":
    app.run(port=5001, debug=True)