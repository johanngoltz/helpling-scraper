import json

import requests

from query_strings import fetch_candidates, transition_to_provider_selection

BASE_URL = "https://www.helpling.de/api/"


def create_bid(postcode: int, **kwargs) -> str:
    """
    Query the helpling API to create a new bid and return its code.
    This is the first step to scraping offers for a region.
    :param postcode: The postcode for which to request a new bid
    :return: The bidCode of the created bid
    """
    response = requests.post(BASE_URL + "v1/bids", {"bid[postcode]": postcode, "bid[checkout_version]": 1})
    bid_id = response.json().get("data").get("code")
    print("Bid " + bid_id + " created for " + str(postcode) + ": " + str(response.status_code))
    response = requests.post(BASE_URL + "/v2/rr", json={
        "operationName": "transitionBidToProviderSelection",
        "query": transition_to_provider_selection,
        "variables": {
            "bidCode": bid_id,
            "date": "21/11/2019",
            "duration": 12600,
            "frequency": "week",
            "ironing": False,
            "materialsRequired": False,
            "notes": "",
            "pets": False,
            "providerType": "",
            "repeat": True,
            "time": "14:00null",
            "workdayFlexibility": False
        }
        # "variables": {"bidCode": bid_id, **kwargs}  # TODO migrate to class?
    })
    print("Bid " + bid_id + " parametrized: " + str(response.status_code))
    return bid_id


def get_candidates(bid_id: str):
    response = requests.post(BASE_URL + "v2/rr", json={
        "query": fetch_candidates,
        "variables": {
            "bidCode": bid_id,
            "endCursor": "",
            "ironing": False,
            "maxPrice": 10000,
            "minBookings": 0,
            "minPrice": 0,
            "minRating": 1,
            "pets": False,
            "sort": "relevance"
        }
    })
    return response.json().get("data").get("customerBid").get("potentialCandidates")


if __name__ == "__main__":
    bid_id = create_bid(10179, date="21/11/2019", duration=12600, frequency="week", time="14:00")
    print(json.dumps(get_candidates(bid_id), indent=4))
