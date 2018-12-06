from nose.tools import assert_is_not_none
from services import get_all_incidents, get_all_red_flags, get_all_interventions, get_all_users, \
    get_all_red_flags_by_id, get_all_interventions_by_id, get_all_users_by_id, get_all_red_flags_for_users_by_id, \
    get_all_interventions_for_users_by_id


def test_get_all_incidents():
    response = get_all_incidents()
    assert_is_not_none(response)


def test_get_all_red_flags():
    response = get_all_red_flags()
    assert_is_not_none(response)


def test_get_all_red_flags_by_id():
    response = get_all_red_flags_by_id()
    assert_is_not_none(response)


def test_get_all_interventions():
    response = get_all_interventions()
    assert_is_not_none(response)


def test_get_all_interventions_by_id():
    response = get_all_interventions_by_id()
    assert_is_not_none(response)


def test_get_all_users():
    response = get_all_users()
    assert_is_not_none(response)


def test_get_all_users_by_id():
    response = get_all_users_by_id()
    assert_is_not_none(response)


def test_get_all_red_flags_for_users_by_id():
    response = get_all_red_flags_for_users_by_id()
    assert_is_not_none(response)


def test_get_all_interventions_for_users_by_id():
    response = get_all_interventions_for_users_by_id()
    assert_is_not_none(response)


