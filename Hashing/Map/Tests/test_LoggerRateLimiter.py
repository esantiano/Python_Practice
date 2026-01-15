import pytest
from Hashing.Map.LoggerRateLimiter import Logger

logger = Logger()
def test_shouldPrint_first_true():
    assert logger.shouldPrintMessage(1, "foo")==True
def test_shouldPrint_second_true():
    assert logger.shouldPrintMessage(2, "bar")==True
def test_shouldPrint_third_false():
    assert logger.shouldPrintMessage(8, "foo")==False
def test_shouldPrint_fourth_false():
    assert logger.shouldPrintMessage(9, "bar")==False
def test_shouldPrint_fifth_true():
    assert logger.shouldPrintMessage(11, "foo")==True
def test_shouldPrint_sixth_true():
    assert logger.shouldPrintMessage(12, "bar")==True