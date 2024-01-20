import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)[0]

    response = client.get(f'/api/v1/courses/{course.id}/')

    data = response.json()
    assert response.status_code == 200
    assert course.id == data['id'] and course.name == data['name']


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/')

    data = response.json()
    assert response.status_code == 200
    assert len(courses) == len(data)


@pytest.mark.django_db
def test_filter_id_course(client, course_factory):
    course = course_factory(_quantity=10)[0]

    response = client.get(f'/api/v1/courses/?id={course.id}')

    data = response.json()
    assert response.status_code == 200
    assert course.id == data[0]['id']


@pytest.mark.django_db
def test_filter_name_course(client, course_factory):
    courses = course_factory(_quantity=10)
    name = courses[0].name

    response = client.get(f'/api/v1/courses/?name={name}')

    data = response.json()
    courses_filter = list(filter(lambda c: c.name == name, courses))
    assert response.status_code == 200
    if len(courses_filter) == len(data):
        for i, course in enumerate(data):
            assert courses_filter[i].name == course['name']


@pytest.mark.django_db
def test_create_course(client, course_factory):
    response = client.post('/api/v1/courses/', data={'name': 'test_name'}, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)[0]

    response = client.patch(f'/api/v1/courses/{course.id}/', data={'name': 'test_name'}, format='json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)[0]

    response = client.delete(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 204
