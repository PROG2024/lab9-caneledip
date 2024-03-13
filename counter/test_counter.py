"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    """Test for counter."""

    def test_singleton(self):
        """Test that invoking another Counter does not create new one."""
        counter1 = Counter()
        counter2 = Counter()
        counter1.increment()
        counter2.increment()
        expected_count = 2
        self.assertEqual(counter1.count(), expected_count)
        self.assertEqual(counter2.count(), expected_count)
        self.assertIs(counter1, counter2)
      
    def test_singleton_counter_not_reset_after_call(self):
         """Test Counter count is not reset after invoking another Counter."""
         counter3 = Counter()
         self.assertNotEqual(counter3.count(), 0)
         self.assertEqual(counter3.count(), 2)
