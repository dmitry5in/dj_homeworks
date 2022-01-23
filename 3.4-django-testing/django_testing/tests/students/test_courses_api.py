import pytest
from rest_framework.test import APIClient

from students.models import Course, Student
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    courses = course_factory(_quantity=1)
    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_by_id(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/', {'id': courses[3].id})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == courses[3].id
    assert data[0]['name'] == courses[3].name


@pytest.mark.django_db
def test_filter_by_name(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/', {'name': courses[3].name})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == courses[3].name


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'Python the best'})

    assert response.status_code == 201
    assert response.data.get('name') == 'Python the best'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=1)
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data={'name': 'Python'})

    assert response.status_code == 200
    assert response.data.get('name') == 'Python'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=1)
    response = client.delete(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 204