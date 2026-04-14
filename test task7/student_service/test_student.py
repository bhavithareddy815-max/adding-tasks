from .service import add_student


def test_add_student():

    result = add_student(100, "TestStudent")

    assert result["message"] == "Student added successfully"