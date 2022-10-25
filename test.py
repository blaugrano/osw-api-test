import requests

ENV = 'https://opencoders-staging-app-eef2y.ondigitalocean.app'


def test_search():
    json = {
      "projects": [],
      "types": [
        "Chore"
      ],
      "statuses": []
    }
    resp = requests.post(url=ENV + '/dev-requests/search?page=0', json=json)
    content = resp.json()
    assert len(content['rows']) == 0
