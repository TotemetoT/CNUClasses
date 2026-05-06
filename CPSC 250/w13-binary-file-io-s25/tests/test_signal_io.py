import unittest
from inspect import signature

from src import signal_io
import numpy as np
import os

class TestSignalIO(unittest.TestCase):

    def setUp(self):
        self.__delta = 0.0001
        # Check to see if you are running from the right directory
        if os.getcwd().endswith("tests"):
            raise Exception("You must run this file from the project root directory")

    def test_write_csv_as_binary(self):

        ws,ns,sd = signal_io.write_csv_as_binary("test_data")

        data = [1550629438, 0, 0.0,
        1550629438, 14662756, 0.11708323264823071,
        1550629438, 29325513, 0.23285875931231667,
        1550629438, 43988269, 0.34604481793933245,
        1550629438, 58651026, 0.4554109297552261,
        1550629439, 73313782, 0.5598020445850692,
        1550629439, 87976539, 0.6581609325877631,
        1550629439, 102639296, 0.7495483067016847,
        1550629439, 117302052, 0.8331602167816085,
        1550629439, 131964809, 0.9083423244482607]

        ws_expected=data[::3]
        ns_expected=data[1::3]
        sd_expected=data[2::3]

        HUNDRED_THOUSANDTHS_PLACE = 5

        self.assertEqual(ws_expected, ws, "Your ws data is not valid")
        self.assertEqual(ns_expected, ns, "Your ns data is not valid")
        self.assertAlmostEqual(sd_expected, sd, HUNDRED_THOUSANDTHS_PLACE,
                               "Your signal data not accurate. ")

    def test_read_binary(self):

        ws, ns, sd = signal_io.write_csv_as_binary("test_data")
        wsb, nsb, sdb = signal_io.read_binary("test_data")

        data = [1550629438, 0, 0.0,
                1550629438, 14662756, 0.11708323264823071,
                1550629438, 29325513, 0.23285875931231667,
                1550629438, 43988269, 0.34604481793933245,
                1550629438, 58651026, 0.4554109297552261,
                1550629439, 73313782, 0.5598020445850692,
                1550629439, 87976539, 0.6581609325877631,
                1550629439, 102639296, 0.7495483067016847,
                1550629439, 117302052, 0.8331602167816085,
                1550629439, 131964809, 0.9083423244482607]

        ws_expected = data[::3]
        ns_expected = data[1::3]
        sd_expected = data[2::3]

        HUNDRED_THOUSANDTHS_PLACE = 5

        self.assertEqual(ws_expected, ws, "Your ws data is not valid - write failed")
        self.assertEqual(ns_expected, ns, "Your ns data is not valid - write failed")
        self.assertAlmostEqual(sd_expected, sd, HUNDRED_THOUSANDTHS_PLACE,
                               "Your signal data not accurate - write failed")

        self.assertEqual(ws_expected, wsb, "Your binary ws data is not valid - read failed")
        self.assertEqual(ns_expected, nsb, "Your binary ns data is not valid - read failed")
        self.assertAlmostEqual(sd_expected, sdb, HUNDRED_THOUSANDTHS_PLACE,
                               "Your binary signal data not accurate - read failed")

    def test_read_binary_signal(self):
        ws, ns, sd = signal_io.write_csv_as_binary("signal_data")
        wsb, nsb, sdb = signal_io.read_binary("signal_data")

        HUNDRED_THOUSANDTHS_PLACE = 5

        self.assertEqual(ws, wsb, "Your ws data does not match - write or read failed")
        self.assertEqual(ns, nsb, "Your ns data does not match - write or read failed")
        self.assertAlmostEqual(sd, sdb, HUNDRED_THOUSANDTHS_PLACE,
                               "Your signal data does not match - write or read failed")

    def test_convert_data(self):
        data = [1550629438, 0, 0.0,
                1550629438, 14662756, 0.11708323264823071,
                1550629439, 29325513, 0.23285875931231667,
                1550629439, 43988269, 0.34604481793933245,
                1550629439, 58651026, 0.4554109297552261,
                1550629440, 23313782, 0.5598020445850692,
                1550629440, 57976539, 0.6581609325877631,
                1550629440, 802639296, 0.7495483067016847,
                1550629441, 117302052, 0.8331602167816085,
                1550629441, 331964809, 0.9083423244482607]

        ws_expected = data[::3]
        ns_expected = data[1::3]
        sd_expected = data[2::3]
        tv,sv = signal_io.convert_data(ws_expected,ns_expected,sd_expected)

        self.assertIsInstance(tv,np.ndarray,"must return numpy ndarray")
        self.assertIsInstance(sv,np.ndarray,"must return numpy ndarray")
        self.assertEqual(10,tv.shape[0],"time must load 10 elements from tests")
        self.assertEqual(10,sv.shape[0],"signal must load 10 elements from tests")

        tv_expected = np.squeeze(np.array([ (ws_expected[i] - ws_expected[0] + 1e-9*ns_expected[i]) for i in range(10)]))
        sv_expected = np.squeeze(np.array([ sd_expected ]))
        HUNDRED_THOUSANDTHS_PLACE = 5
        np.testing.assert_array_equal(tv_expected, tv, err_msg= "Your time data does not match expected")
        np.testing.assert_array_equal(sv_expected, sv, err_msg= "Your signal data does not match expected")


if __name__ == '__main__':
    unittest.main()
