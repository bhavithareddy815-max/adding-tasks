from .service import add_marks


def test_add_marks():

    result = add_marks(100, "Math", 90)

    assert result["message"] == "Marks added successfully"