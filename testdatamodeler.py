import unittest
import os
import pandas as pd
from datamodeler import DataModeler

DATA_FILE = "./data/reeview_test.csv"
TWEET_ARCHIVE_DIR = "./data/test_archive"

class TestDataModeler( unittest.TestCase ):

    def setUp(self):
        if os.access( DATA_FILE, os.F_OK):
            os.remove(DATA_FILE)

    def test_write_tweets_to_csv( self ):
        df = pd.DataFrame(columns=('tweet_id', 'hashtag', 'created_at', 'user_id', 'tweet_text'))
        df.loc[123] = [ "test", "test", "test", "test", "test" ]

        DataModeler.write_tweets_to_csv(df, DATA_FILE )
        self.assertTrue( os.stat(DATA_FILE).st_size > 0, "data file is empty" )

    def test_load_tweets_from_twitter_archive( self ):
        dm = DataModeler()
        dm.load_tweets_from_twitter_archive( TWEET_ARCHIVE_DIR, DATA_FILE )
        self.assertTrue( os.stat(DATA_FILE).st_size > 0, "data file is empty" )

if __name__ == '__main__':
    unittest.main()

