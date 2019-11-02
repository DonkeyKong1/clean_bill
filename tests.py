"""
I use databases for aligning my data. In retrospect I perhaps should have used a dataframe for this exercise to account
for the unit tests. Databases are not easily unit-tested, and this presents an issue in my design in that it is
difficult to test.

In an ideal situation I would design the database not as an in-memory database, but as a standing structure. A solid
foundational database makes for a flexible system with highly reusable functionality.
"""
import unittest
from clean_bill import CleanBill


class CleanBillTest(unittest.TestCase):

    def setUp(self):
        self.CleanBill = CleanBill()
        self.CleanBill.make_database()
        self.CleanBill.load_data()

    def test_days_of_the_week_are_true(self):
        week = {'Sunday': '2019-11-03',
                'Monday': '2019-11-04',
                'Tuesday': '2019-11-05',
                'Wednesday': '2019-11-06',
                'Thursday': '2019-11-07',
                'Friday': '2019-11-08',
                'Saturday': '2019-11-09'}
        for day, date in week.items():
            dow = self.CleanBill.connection.execute("""
            SELECT strftime('%w', '{date}');""".format(date=date)).fetchone()[0]

            print(day, date, dow)
            db_day = self.CleanBill.connection.execute("""
            SELECT Day_Of_The_Week 
            FROM Day_Of_The_Week
            WHERE Day_Of_The_Week_ID = {dow_id};""".format(dow_id=dow)).fetchone()[0]

            self.assertEqual(day, db_day)
