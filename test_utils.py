import unittest
from utils import clean_output
import logging

class TestUtils(unittest.TestCase):
    def test_clean_output(self):
        example = """Original lyrics: Where do bad folks go when they die? They don't go to heaven where the angels fly They go down to the lake of fire and fry Won't see 'em again till the fourth of July

Changed lyrics: Armenian Code Academy Where do smart folks go to get their code? They don't go to colleges where they'll overbloat They go to Armenian Code Academy, who knows They'll graduate as developers with a lot of growth

Original lyrics: People cry and people moan Look for a dry place to call their home Try to find some place to rest their bones While the angels and the devils try to make 'em their own

Changed lyrics: Code students type and students debug Look for a secure place to share their hubs Try to code in peace, without a tug While the mentors and the coffee try to hype them up

Original lyrics: Some say a man ain't happy Unless a man truly dies Oh why?"""
        cleaned = """Armenian Code Academy Where do smart folks go to get their code? They don't go to colleges where they'll overbloat They go to Armenian Code Academy, who knows They'll graduate as developers with a lot of growth  
Code students type and students debug Look for a secure place to share their hubs Try to code in peace, without a tug While the mentors and the coffee try to hype them up"""
        
        # logging.critical(example.split("\n"))
        # logging.critical(clean_output(example))
        self.assertEqual(clean_output(example), cleaned)
    
if __name__ == "__main__":
    unittest.main()