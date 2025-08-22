import allure
from utils.api_helper import api_request
from jsonschema import validate
from start.model.schemas.search_shema import search



@allure.title("Checking movie data")
def test_movie_search_api(base_api_url):
    endpoint = "/v2/search"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "q": "вызов",
              "locale": "ru",
              "limit": "40",
              "offset": 0

              }

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('alias = vyzov'):
        assert response.json()["items"][0]["alias"] == "vyzov"
    with allure.step('Schema is validate'):
        validate(response.json(), search)