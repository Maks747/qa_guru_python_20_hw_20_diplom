import allure
from jsonschema import validate

from start.model.schemas.schemas import search_movie_schema
from utils.api_helper import api_request



@allure.title("Checking movie search")
def test_movie_search_api(base_api_url):
    endpoint = "/v2/search"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "q": "кухня",
              "locale": "ru",
              "limit": "40",
              "offset": 0
              }

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('alias = kuhnya'):
        assert response.json()["items"][0]["alias"] == "kuhnya"
    with allure.step('Validate response schema'):
        body = response.json()
        validate(body, search_movie_schema)