import unittest

from test_cases.rekrutacja_na_testera_login_page_tests import RekrutacjaNaTesteraLoginPageTests
from test_cases.rekrutacja_na_testera_front_page_tests import RekrutacjaNaTesteraFrontPageTests


def full_suite():
    test_suit = unittest.TestSuite()
    test_suit.addTest(unittest.makeSuite(RekrutacjaNaTesteraLoginPageTests))
    test_suit.addTest(unittest.makeSuite(RekrutacjaNaTesteraFrontPageTests))
    return test_suit


runner = unittest.TextTestRunner(verbosity=2)
runner.run((full_suite()))

