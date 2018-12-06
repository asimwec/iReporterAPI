try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse2 import urljoin

import requests

from constants import BASE_URL

all_incidents = urljoin(BASE_URL, 'incidents')
all_red_flags = urljoin(BASE_URL, 'red-flags')
all_red_flags_by_id = urljoin(BASE_URL, 'red-flags/3')
all_interventions = urljoin(BASE_URL, 'interventions')
all_interventions_by_id = urljoin(BASE_URL, 'interventions/2')
all_users = urljoin(BASE_URL, 'users')
all_users_by_id = urljoin(BASE_URL, 'users/1')
all_red_flags_for_users_by_id = urljoin(BASE_URL, 'users/1/red-flags')
all_interventions_for_users_by_id = urljoin(BASE_URL, 'users/2/interventions')


def get_all_incidents():
    response = requests.get(all_incidents)
    if response.ok:
        return response
    else:
        return None


def get_all_red_flags():
    response = requests.get(all_red_flags)
    if response.ok:
        return response
    else:
        return None


def get_all_red_flags_by_id():
    response = requests.get(all_red_flags_by_id)
    if response.ok:
        return response
    else:
        return None


def get_all_interventions():
    response = requests.get(all_interventions)
    if response.ok:
        return response
    else:
        return None


def get_all_interventions_by_id():
    response = requests.get(all_interventions_by_id)
    if response.ok:
        return response
    else:
        return None


def get_all_users():
    response = requests.get(all_users)
    if response.ok:
        return response
    else:
        return None


def get_all_users_by_id():
    response = requests.get(all_users_by_id)
    if response.ok:
        return response
    else:
        return None


def get_all_red_flags_for_users_by_id():
    response = requests.get(all_red_flags_for_users_by_id)
    if response.ok:
        return response
    else:
        return None


def get_all_interventions_for_users_by_id():
    response = requests.get(all_interventions_for_users_by_id)
    if response.ok:
        return response
    else:
        return None
