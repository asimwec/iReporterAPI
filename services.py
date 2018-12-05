try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse2 import urljoin

# Third-party imports...
import requests

# Local imports...
from constants import BASE_URL

HEROKU_URL = urljoin(BASE_URL, 'incidents')


def get_heroku():
    response = requests.get(HEROKU_URL)
    if response.ok:
        return response
    else:
        return None