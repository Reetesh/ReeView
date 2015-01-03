#this will be the file that'll have all the functions that generate stats for the api to serve
import pandas as pd

class StatsGenerator:
    

    def __init__( self, data_file ):
        self.tweet_store = pd.DataFrame.from_csv(data_file)

    def top_hashtags(self, top_list_size = 5, bin_type = "complete"):
        
        if bin_type == "complete":
            tweets = self.tweet_store['hashtag'].str.lower().value_counts()
        
        tweets = tweets.head(top_list_size)      
        tweets_json = tweets.to_json( force_ascii = False )
        return tweets_json
