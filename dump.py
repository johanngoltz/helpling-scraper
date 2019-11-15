import json

import requests

from query_strings import fetch_candidates, transition_to_provider_selection

BASE_URL = "https://www.helpling.de/api/"


class TransitionBidToProviderSelection:
    def __init__(self):
        self.date = "18/11/2019"
        self.duration = 12600
        self.frequency = "week"
        self.ironing = False
        self.materialsRequired = False
        self.notes = ""
        self.pets = False
        self.providerType = ""
        self.repeat = True
        self.time = "14:00null"
        self.workdayFlexibility = False


def create_bid(postcode: int, **kwargs) -> str:
    """
    Query the helpling API to create a new bid and return its code.
    This is the first step to scraping offers for a region.
    :param postcode: The postcode for which to request a new bid
    :param kwargs: The parameters to set for the search.
    :return: The bidCode of the created bid
    """
    response = requests.post(BASE_URL + "v1/bids", {"bid[postcode]": postcode, "bid[checkout_version]": 1})
    bid_id = response.json().get("data").get("code")

    print("Create bid for " + str(postcode) + " (" + bid_id + "): " + str(response.status_code))

    variable_defaults = TransitionBidToProviderSelection().__dict__
    response = requests.post(BASE_URL + "/v2/rr", json={
        "operationName": "transitionBidToProviderSelection",
        "query": transition_to_provider_selection,
        "variables": {**variable_defaults, **kwargs, "bidCode": bid_id}
    })

    transition_is_success = response.json().get("errors") is None
    print("Parametrize bid " + bid_id + ": " + str(response.status_code) if transition_is_success else response.text)

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
    bid_id = create_bid(10179, time="11:30")
    print(json.dumps(get_candidates(bid_id), indent=4))
