import unittest
from OpenDateRange import DateRange
from helper import valid_dates_sorted


class Test(unittest.TestCase):


    def test_init(self):
        DateRange.DATE_FORMAT = "%Y-%m-%d"

        date1 = "2002-12-12"
        date2 = "2002-12-12"


        d1 = DateRange(date_from=date1, date_to=date2)
        self.assertFalse(d1.is_infinite())
        self.assertTrue(d1._length is None)

        d2 = DateRange(date_from=None, date_to=date2)
        self.assertTrue(d2.is_infinite())
        self.assertTrue(d2._length is None)

        d3 = DateRange(date_from=date1, date_to=None)
        self.assertTrue(d3.is_infinite())
        self.assertTrue(d3._length is None)

        d4 = DateRange(date_from=None, date_to=None)
        self.assertTrue(d4.is_infinite())
        self.assertTrue(d4._length is None)

        self.assertRaises(ValueError, DateRange, "2002-12-12", "2000-12-12")



    def test_repr(self):
        DateRange.DATE_FORMAT = "%Y-%m-%d"

        date1 = "2002-12-11"
        date2 = "2003-12-11"

        d1 = DateRange(date_from=date1, date_to=date2)
        d2 = DateRange(date_from=None, date_to=date2)
        d3 = DateRange(date_from=date1, date_to=None)
        d4 = DateRange(date_from=None, date_to=None)

        DateRange.DATE_FORMAT = "%d.%m.%Y"

        self.assertEquals(d1.__repr__(), 'DateRange(11.12.2002, 11.12.2003)')
        self.assertEquals(d2.__repr__(), 'DateRange(None, 11.12.2003)')
        self.assertEquals(d3.__repr__(), 'DateRange(11.12.2002, None)')
        self.assertEquals(d4.__repr__(), 'DateRange(None, None)')


    def test_contains(self):
        DateRange.DATE_FORMAT = "%d.%m.%Y"

        date1 = "01.01.1980"
        date2 = "24.07.2040"

        dr = DateRange(date_from=date1, date_to=date2)

        DateRange.DATE_FORMAT = "%Y-%m-%d"

        for date in valid_dates_sorted:
            self.assertTrue(date in dr)

        not_in_range = ["1979-12-31", "2040-07-25"]
        for date in not_in_range:
            self.assertFalse(date in dr)


    def test_intersects(self):
        DateRange.DATE_FORMAT = "%Y/%m/%d"

        dr = DateRange(date_from=None, date_to=None)
        self.assertTrue(dr.intersects(date_from="2000/10/10", date_to="2001/10/10"))
        self.assertTrue(dr.intersects(date_from="2000/10/10", date_to=None))
        self.assertTrue(dr.intersects(date_from=None, date_to="2000/10/10"))
        self.assertTrue(dr.intersects(date_from=None, date_to=None))

        dr = DateRange(date_from=None, date_to="2000/10/10")
        self.assertTrue(dr.intersects(date_from="2000/10/10", date_to=None))
        self.assertTrue(dr.intersects(date_from="2000/10/10", date_to="2000/10/10"))
        self.assertTrue(dr.intersects(date_from="2000/10/10", date_to="2000/10/11"))

        self.assertTrue(dr.intersects(date_from="2000/10/09", date_to=None))
        self.assertTrue(dr.intersects(date_from="2000/10/09", date_to="2000/10/10"))
        self.assertTrue(dr.intersects(date_from="2000/10/09", date_to="2000/10/11"))

        self.assertFalse(dr.intersects(date_from="2000/10/11", date_to=None))
        self.assertFalse(dr.intersects(date_from="2000/10/11", date_to="2000/10/11"))
        self.assertFalse(dr.intersects(date_from="2000/10/11", date_to="2000/10/12"))

        dr = DateRange(date_from="2000/10/10", date_to=None)
        self.assertTrue(dr.intersects(date_from=None, date_to="2000/10/10"))
        self.assertTrue(dr.intersects(date_from="2000/10/09", date_to="2000/10/10"))
        self.assertTrue(dr.intersects(date_from="2000/10/11", date_to="2000/10/11"))

        self.assertTrue(dr.intersects(date_from=None, date_to="2000/10/11"))
        self.assertTrue(dr.intersects(date_from="2000/10/09", date_to="2000/10/11"))
        self.assertTrue(dr.intersects(date_from="2000/10/11", date_to="2000/10/11"))

        self.assertFalse(dr.intersects(date_from=None, date_to="2000/10/09"))
        self.assertFalse(dr.intersects(date_from="2000/10/09", date_to="2000/10/09"))
        self.assertFalse(dr.intersects(date_from="2000/10/08", date_to="2000/10/09"))

        dr1 = DateRange(date_from="2000/10/10", date_to="2000/10/15")
        dr2 = DateRange(date_from="2000/10/12", date_to="2000/10/13")
        dr3 = DateRange(date_from="2000/10/14", date_to="2000/10/16")
        dr4 = DateRange(date_from="2000/10/09", date_to="2000/10/11")

        self.assertTrue(dr1.intersects(date_from="2000/10/12", date_to="2000/10/13"))
        self.assertTrue(dr2.intersects(date_from="2000/10/10", date_to="2000/10/15"))
        self.assertTrue(dr1.intersects(date_from="2000/10/14", date_to="2000/10/16"))
        self.assertFalse(dr2.intersects(date_from="2000/10/09", date_to="2000/10/11"))
        self.assertFalse(dr3.intersects(date_from="2000/10/09", date_to="2000/10/11"))
        self.assertFalse(dr4.intersects(date_from="2000/10/14", date_to="2000/10/16"))


    def test_iter(self):
        DateRange.DATE_FORMAT = "%Y-%m-%d"

        date1 = "2000-12-12"
        date2 = "2000-12-14"

        dr = DateRange(date_from=date1, date_to=None)
        self.assertRaises(ValueError, dr.__iter__)

        dr = DateRange(date_from=None, date_to=date2)
        self.assertRaises(ValueError, dr.__iter__)

        dr = DateRange(date_from=None, date_to=None)
        self.assertRaises(ValueError, dr.__iter__)

        dr = DateRange(date_from=date1, date_to=date2)
        dates_in_range = ["2000-12-12", "2000-12-13", "2000-12-14"]
        dates_in_iterator = [date for date in dr]
        self.assertEquals(dates_in_range, dates_in_iterator)


    def test_len(self):
        DateRange.DATE_FORMAT = "%Y-%m-%d"

        date1 = "2000-12-12"
        date2 = "2000-12-14"

        dr = DateRange(date_from=date1, date_to=None)
        self.assertRaises(ValueError, dr.__len__)

        dr = DateRange(date_from=None, date_to=date2)
        self.assertRaises(ValueError, dr.__len__)

        dr = DateRange(date_from=None, date_to=None)
        self.assertRaises(ValueError, dr.__len__)

        dr = DateRange(date_from=date1, date_to=date2)
        self.assertTrue(len(dr) == 3)
        self.assertTrue(len(dr) == 3)

        dr = DateRange(date_from=date1, date_to=date1)
        self.assertTrue(len(dr) == 1)
