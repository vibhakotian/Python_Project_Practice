import requests
def test_get_post():
    response=requests.get(
       "https://jsonplaceholder.typicode.com/posts/1"
    )
    print(response.status_code)
    assert response.status_code==200
    data=response.json()
    assert data['id']==1
    print(data)

def test_get_non_existing_post():
    response=requests.get(
           "https://jsonplaceholder.typicode.com/posts/999999"
    )
    assert response.status_code==404
    data=response.json()
    assert 'id' not in data
    print(response.status_code)
    print(response.json())