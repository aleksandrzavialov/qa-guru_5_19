import requests


base_url = 'https://reqres.in/'


def test_create_a_user_with_name_only():
    name = "John"

    response = requests.post(
        url=f'{base_url}api/users',
        json={
            "name": name
        }
    )

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert 'job' not in response.json()


def test_update_a_user_with_put_both_name_and_job():
    name = "John"
    job = 'Wrestler'

    response = requests.put(
        url=f'{base_url}api/users/2',
        json={
            "name": name,
            "job": job
        }
    )

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_update_a_user_with_patch_only_job():
    job = 'Wrestler'

    response = requests.patch(
        url=f'{base_url}api/users/2',
        json={
            "job": job
        }
    )

    assert response.status_code == 200
    assert response.json()['job'] == job
    assert 'name' not in response.json()


def test_register_an_existing_user():
    email = "lindsay.ferguson@reqres.in"
    password = "1234qwerty"

    response = requests.post(
        url=f'{base_url}api/register',
        json={
            "email": email,
            "password": password,
        }
    )

    assert response.status_code == 200
    assert len(str(response.json()['id'])) >= 1
    assert len(response.json()['token']) >= 17


def test_unable_to_register_a_not_existing_user():
    email = "test@test.com"
    password = "1234qwerty"

    response = requests.post(
        url=f'{base_url}api/register',
        json={
            "email": email,
            "password": password,
        }
    )

    assert response.status_code == 400
    assert (response.json()['error']) == 'Note: Only defined users succeed registration'


def test_unable_to_register_a_existing_user_sending_username_only():
    username = "byron.fields@reqres.in"

    response = requests.post(
        url=f'{base_url}api/register',
        json={
            "username": username
        }
    )

    assert response.status_code == 400
    assert (response.json()['error']) == 'Missing password'


def test_login_with_existing_user():
    email = "lindsay.ferguson@reqres.in"
    password = "1234qwerty"

    response = requests.post(
        url=f'{base_url}api/login',
        json={
            "email": email,
            "password": password,
        }
    )

    assert response.status_code == 200
    assert len(response.json()['token']) >= 17


def test_unable_login_with_non_existing_user():
    email = "test.superuser@yandex.ru"
    password = "1234qwerty"

    response = requests.post(
        url=f'{base_url}api/login',
        json={
            "email": email,
            "password": password,
        }
    )

    assert response.status_code == 400
    assert (response.json()['error']) == 'user not found'


def test_requested_per_page_number_with_delay_default_page():
    per_page = 3
    delay = 5

    response = requests.get('https://reqres.in/api/users', params={'delay': delay, 'per_page': per_page})

    assert response.status_code == 200
    assert response.json()['page'] == 1
    assert response.json()['per_page'] == per_page
    assert response.json()['total_pages'] == 4
    assert response.json()['total'] == 12


def test_requested_per_page_number_with_delay_second_page():
    per_page = 2
    page = 2
    delay = 3

    response = requests.get('https://reqres.in/api/users', params={'delay': delay, 'per_page': per_page, 'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page
    assert response.json()['per_page'] == per_page
    assert response.json()['total_pages'] == 6
    assert response.json()['total'] == 12





