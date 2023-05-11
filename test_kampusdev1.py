"""
K-ampus dev
"""
import pytest
import requests


def test_status_code():
    """
    Test status code
    """
    response = requests.post('https://k-ampus.dev/api/v1/login', json={
        "username": "skhalipa@gmail.com", "password": "skhalipa@gmail.com"}, timeout=2)
    assert response.status_code == 200, ""

def test_body_token():
    """
    Test body token
    """
    response = requests.post('https://k-ampus.dev/api/v1/login', json={
        "username": "skhalipa@gmail.com", "password": "skhalipa@gmail.com"}, timeout=2)
    assert response.json()['accessToken'] is not None, ""

def test_status_code_competence(auth):
    """
    Status Code Competence
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2)
    assert response.status_code == 200, ""

def test_competence_content(auth):
    """
    Competence Content
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2)
    assert  isinstance(response.json()['content'], list), ""

def test_competence_content_not_none(auth):
    """
    Competence Content not none
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2)
    assert response.json()['content'] is not None, ""

def test_competence_content_types(auth):
    """
    Competence Content types
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2) 
    contents = response.json()['content']
    for content in contents:
        for k, v in content.items():
            if k == 'id':
                assert isinstance(v, int)
            elif k == 'name':
                assert isinstance(v, str)
            elif k == 'isHardSkill':
                assert isinstance(v, bool)
            elif k == 'skillIds':
                assert isinstance(v, list)
            else:
                pytest.fail(reason="Unexpected content item")  

def test_competence_pageable(auth):
    """
    Competence Pageable
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2)
    assert response.json()['pageable'], ""
    

def test_competence_pageable_types(auth):
    """
    Competence pageable types
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2) 
    pageables = response.json()['pageable']
    assert isinstance(pageables['pageSize'], int)
    assert isinstance(pageables['pageNumber'], int)
    assert isinstance(pageables['offset'], int)
    assert isinstance(pageables['unpaged'], bool)
    assert isinstance(pageables['paged'], bool),""

"""
Тест, что в объекте pageable присутствует подобъект sort
"""
def test_competence_pageable_sort(auth):
    """
    Competence pageable sort
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2) 
    pageables = response.json()['pageable']
    assert pageables['sort'], ""

"""
Тест, что объект sort содержит нижеописанные поля и данные поля соответствуют типам
"""
def test_competence_pageable_sort_types(auth):
    """
    Competence pageable sort types
    """
    response = requests.get('https://k-ampus.dev/api/v1/competence', headers={
        'Authorization':f'Bearer {auth}'}, timeout=2) 
    pageables = response.json()['pageable']
    sort_pageables=pageables['sort']
    assert isinstance(sort_pageables['sorted'], bool)
    assert isinstance(sort_pageables['unsorted'], bool)
    assert isinstance(sort_pageables['empty'], bool),""