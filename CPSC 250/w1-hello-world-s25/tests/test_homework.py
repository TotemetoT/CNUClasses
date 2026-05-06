import unittest

from src import homework


class TestHomework(unittest.TestCase):

    def test_homework_numbers(self):
        self.assertTrue("1" in homework.cnu_captains())
        self.assertTrue("11" in homework.cnu_captains())
        self.assertTrue("99" in homework.cnu_captains())

    def test_homework_cnu(self):
        self.assertTrue("cnu" in homework.cnu_captains().lower())

    def test_homework_cnu_exact(self):
        self.assertTrue("CNU" in homework.cnu_captains())

    def test_homework_captains(self):
        self.assertTrue("captains" in homework.cnu_captains().lower())

    def test_homework_captains_exact(self):
        self.assertTrue("CAPTAINS" in homework.cnu_captains())

    def test_homework_lines(self):
        lines = homework.cnu_captains().split("\n")
        self.assertEquals(101, len(lines), msg="Incorrect number of lines - between 1 and 100 inclusive!")

    def test_homework_exact(self):

        # Do your solution with a loop.  DO NOT copy this line!
        test_string = "1" + "\n" + "CNU" + "\n" + "3" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "7" + "\n" + "CNU" + "\n" + "9" + "\n" + "CNUCAPTAINS" + "\n" + "11" + "\n" + "CNU" + "\n" + "13" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "17" + "\n" + "CNU" + "\n" + "19" + "\n" + "CNUCAPTAINS" + "\n" + "21" + "\n" + "CNU" + "\n" + "23" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "27" + "\n" + "CNU" + "\n" + "29" + "\n" + "CNUCAPTAINS" + "\n" + "31" + "\n" + "CNU" + "\n" + "33" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "37" + "\n" + "CNU" + "\n" + "39" + "\n" + "CNUCAPTAINS" + "\n" + "41" + "\n" + "CNU" + "\n" + "43" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "47" + "\n" + "CNU" + "\n" + "49" + "\n" + "CNUCAPTAINS" + "\n" + "51" + "\n" + "CNU" + "\n" + "53" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "57" + "\n" + "CNU" + "\n" + "59" + "\n" + "CNUCAPTAINS" + "\n" + "61" + "\n" + "CNU" + "\n" + "63" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "67" + "\n" + "CNU" + "\n" + "69" + "\n" + "CNUCAPTAINS" + "\n" + "71" + "\n" + "CNU" + "\n" + "73" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "77" + "\n" + "CNU" + "\n" + "79" + "\n" + "CNUCAPTAINS" + "\n" + "81" + "\n" + "CNU" + "\n" + "83" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "87" + "\n" + "CNU" + "\n" + "89" + "\n" + "CNUCAPTAINS" + "\n" + "91" + "\n" + "CNU" + "\n" + "93" + "\n" + "CNU" + "\n" + "CAPTAINS" + "\n" + "CNU" + "\n" + "97" + "\n" + "CNU" + "\n" + "99" + "\n" + "CNUCAPTAINS"+ "\n"

        self.assertEqual(test_string, homework.cnu_captains(), msg='String is not an exact match')


if __name__ == '__main__':
    unittest.main()
