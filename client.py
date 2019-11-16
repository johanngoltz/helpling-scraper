from typing import List

import requests
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

import helpling_schema
from query_strings import transition_to_provider_selection

BASE_URL = "https://www.helpling.de/api/"
gql_endpoint = HTTPEndpoint(BASE_URL + "v2/rr", base_headers={
    # CloudFlare blocks the default user agent. Pretend to be IE 6.
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
})


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

    if bid_id is None:
        raise Exception("Bid for postcode " + str(postcode) + " could not be created: " + response.text)

    print("Create bid for " + str(postcode) + " (" + bid_id + "): OK")

    variable_defaults = TransitionBidToProviderSelection().__dict__
    response = requests.post(BASE_URL + "/v2/rr", json={
        "operationName": "transitionBidToProviderSelection",
        "query": transition_to_provider_selection,
        "variables": {**variable_defaults, **kwargs, "bidCode": bid_id}
    })

    if response.json().get("errors") is not None:
        raise Exception("Bid " + bid_id + " could not be parametrized: " + response.text)

    print("Parametrize bid " + bid_id + ": OK")
    return bid_id


def get_candidates_for_bid(bid_id: str) -> List[helpling_schema.DecoratedPotentialCandidateEdge]:
    op = Operation(helpling_schema.Query)

    candidates = op.customer_bid(code=bid_id).potential_candidates(first=1000)

    candidates.edges.node.price_per_hour()

    provider = candidates.edges.node.provider
    provider.__fields__("id", "firstname", "shortname", "default_profile_image", "pets", "windows", "ironing",
                        "ratings_received_count", "verification_level", "documents", "performed_cleanings_count",
                        "language_skills", "instabook_enabled")
    provider.avg_rating.total()
    provider.experience.__fields__()
    provider.distance_to_bid(bid_code=bid_id)

    data = gql_endpoint(op)

    return (op + data).customer_bid.potential_candidates.edges


def get_bid(bid_id: str) -> helpling_schema.CustomerBid:
    op = Operation(helpling_schema.Query)

    op.customer_bid(code=bid_id).__fields__("code", "duration", "start_time")

    data = gql_endpoint(op)
    return (op + data).customer_bid


if __name__ == "__main__":
    new_bid = create_bid(10179, time="11:30")
    # get_bid(new_bid)
    print(get_candidates_for_bid(new_bid))
