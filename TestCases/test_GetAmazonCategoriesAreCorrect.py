import json
import requests
import jsonpath
import uuid
from Tools.Utility import Utility as uti

url = "http://sk-cat-stg.safekiddo.net/public-cat/api/v1/categorize-url"
cathegorized_url = "https://amazon.com"
auth_input = ('test', '123')
params = {"url": cathegorized_url}
hash_code = "36c71541-89b0-4636-81d2-5ee8bc47d55f"
headers = {"AuthHash": uti.generate_hash(cathegorized_url, hash_code),
           "Idempotency-Key": str(uuid.uuid1())}


def test_http_status_ok():
    response = requests.get(url, #auth=auth_input,
                            params=params,
                            headers=headers,
                            verify=False,
                            allow_redirects=False)
    assert response.status_code == 200


def test_categories_are_correct():
    response = requests.get(url, #auth=auth_input,
                            params=params,
                            headers=headers,
                            verify=False,
                            allow_redirects=False)
    response_json = json.loads(response.text)
    website = jsonpath.jsonpath(response_json, 'categorizedWebsite')

    categories = website[0]['categories']

    assert categories == [0, 902]


def test_reputation_categories_are_correct():
    response = requests.get(url, #auth=auth_input,
                            params=params,
                            headers=headers,
                            verify=False,
                            allow_redirects=False)
    response_json = json.loads(response.text)
    website = jsonpath.jsonpath(response_json, 'categorizedWebsite')

    categories = website[0]['reputationCategories']

    assert categories == [0, 2]


def test_secondary_categories_are_correct():
    response = requests.get(url, #auth=auth_input,
                            params=params,
                            headers=headers,
                            verify=False,
                            allow_redirects=False)
    response_json = json.loads(response.text)
    website = jsonpath.jsonpath(response_json, 'categorizedWebsite')
    secondary_categories = website[0]['secondaryCategories']

    assert secondary_categories == [0]


def test_security_categories_are_correct():
    response = requests.get(url, #auth=auth_input,
                            params=params,
                            headers=headers,
                            verify=False,
                            allow_redirects=False)
    response_json = json.loads(response.text)
    website = jsonpath.jsonpath(response_json, 'categorizedWebsite')
    security_categories = website[0]['securityCategories']

    assert security_categories == [0]
