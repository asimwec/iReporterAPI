from nose.tools import assert_is_not_none
from services import get_heroku


def test_request_response():
    # Call the service, which will send a request to the server.
    response = get_heroku()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
