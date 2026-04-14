from .service import get_result


def test_get_result():

    result = get_result(100)

    assert result["average"] >= 0