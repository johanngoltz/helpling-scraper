import datetime
import unittest

from dateutil.parser import parse as parse_date
from ddt import ddt, data, unpack

import client


# noinspection PyBroadException
@ddt
class TestCreateBid(unittest.TestCase):
    @data(69190, 76137)
    def test_bid_exists_after_create(self, postcode):
        bid_id = client.create_bid(postcode)
        self.assertEqual(bid_id, client.get_bid(bid_id).code)

    @data(12345)
    def test_bid_does_not_exist_for_invalid_postcode(self, postcode):
        bid_id = None
        try:
            bid_id = client.create_bid(postcode)
        except:
            pass
        finally:
            self.assertTrue(bid_id is None)

    def test_bid_has_default_values(self):
        bid_id = client.create_bid(10179)
        created_bid = client.get_bid(bid_id)
        self.assertEqual(12600, created_bid.duration)

    @unpack
    @data(["17:00", "26/05/2020"], ["10:15", "01/04/2020"])
    def test_bid_has_custom_values(self, time, date):
        bid_id = client.create_bid(76137, time=time, date=date)
        created_bid = client.get_bid(bid_id)
        expected = parse_date(time + " " + date, dayfirst=True).astimezone(datetime.timezone.utc)
        self.assertEqual(expected, created_bid.start_time)
