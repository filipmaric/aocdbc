import unittest
from icontract_hypothesis import test_with_inferred_strategy
from petlja.bus_ride import bus_ride

class TestBusRide(unittest.TestCase):
    def test_1(self) -> None:
        result = bus_ride(2, 59, 8, 3, 1, 14)
        assert result is not None
        h, m, s = result
        self.assertEqual(h, 0)
        self.assertEqual(m, 2)
        self.assertEqual(s, 6)

    def test_2(self) -> None:
        result = bus_ride(23, 59, 59, 0, 0, 1)
        assert result is not None
        h, m, s = result
        self.assertEqual(h, 0)
        self.assertEqual(m, 0)
        self.assertEqual(s, 2)

    def test_3(self) -> None:
        result = bus_ride(0, 0, 1, 23, 59, 59)
        assert result is not None
        h, m, s = result
        self.assertEqual(h, 23)
        self.assertEqual(m, 59)
        self.assertEqual(s, 58)
        
    def test_verify_with_icontract_hypothesis(self) -> None:
        test_with_inferred_strategy(bus_ride)
    
    
if __name__ == "__main__":
    unittest.main()
