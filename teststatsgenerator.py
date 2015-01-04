import unittest
import os
import logging
import json
import pandas as pd
from statsgenerator import StatsGenerator
from datamodeler import DataModeler

DATA_FILE = "./data/reeview_test.csv"
TWEET_ARCHIVE_DIR = "./data/test_archive"

class TestStatsGenerator( unittest.TestCase ):

    logging.basicConfig()
    log = logging.getLogger("reeview.statsgenerator")

    def setUpModule( ):
       dm = DataModeler()
       dm.load_tweets_from_twitter_archive( TWEET_ARCHIVE_DIR, DATA_FILE )
    
    def setUp( self ):
       self.stats_generator = StatsGenerator( DATA_FILE )

    def test_top_hashtags( self ):
        hashtags = self.stats_generator.top_hashtags()
        TestStatsGenerator.log.warning(hashtags)
        # no idea what to assert
    def test_tag_breakdown( self ):
        counts = self.stats_generator.tag_breakdown( "ReeMov", 2014, 12, "month" )
        TestStatsGenerator.log.warning(counts)

if __name__ == '__main__':
    unittest.main()

