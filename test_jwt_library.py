import jwt_library

def test_decode():
    data = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZ2UiOi03LCJuYW1lIjoiZ2dqaXV3IiwiaWF0IjoxNTE2MjM5MDIyfQ.JtY-vs16O3hABvQYXS9BScOH7iiZxpT6PQ333jE0WM4'
    expected_result = {
        "age": -7,
        "name": "ggjiuw",
        "iat": 1516239022
    }
    actual_result = jwt_library.decode(data=data)
    assert expected_result == actual_result