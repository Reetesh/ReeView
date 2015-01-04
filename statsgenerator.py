import calendar
import datetime
import pandas as pd
import numpy as np

class StatsGenerator:
    

    def __init__( self, data_file ):
        self.tweet_store = pd.DataFrame.from_csv(data_file)

    def top_hashtags(self, year = "", top_list_size = 5, bin_type = "complete"):
        
        if bin_type == "complete":
            tweets = self.tweet_store['hashtag'].str.lower().value_counts()
        
        tweets = tweets.head(top_list_size)      
        tweets_json = tweets.to_json( force_ascii = False )
        return tweets_json
    
    #currently returns count for each month/day
    # returns the values like
    # {0: count, 1: count ..., 12:count}
    #can be used for busiest month, daily breakdown etc
    def tag_breakdown( self, hashtag, query_year, query_month = 1, query_range = "year"  ):
        
        query_date_begin = str(query_year) + "-" + str(query_month) + "-01"
        #the tweet_store has created_at UTC timestamps
        query_timestamp_begin = calendar.timegm(datetime.datetime.strptime(query_date_begin, "%Y-%m-%d").timetuple())
        
        if query_range == "year":
            query_date_end = str(query_year+1) + '-' + str(query_month) + "-01"
            bin_size = 12+1
        else:
            #came up with a fancy mod-operator logic, but changed to this for readability
            #might even confuse future me :P
            if( query_month == 12 ):
               query_date_end = str(query_year+1) + "-01-01"
            else:
               query_date_end = str(query_year) + '-' + str(query_month+1) + "-01"
            bin_size = calendar.monthrange(query_year, query_month)[1] + 1
        query_timestamp_end = calendar.timegm(datetime.datetime.strptime(query_date_end, "%Y-%m-%d").timetuple())

        #get tweets that are in the range and with required hashtag
        tweets = self.tweet_store[ (self.tweet_store['created_at'] > query_timestamp_begin ) & (self.tweet_store['created_at'] < query_timestamp_end) ]
        tweets = tweets[ tweets['hashtag'].str.lower() == hashtag.lower() ]

        #bin the dataframe by dates by year/month
        bins = np.linspace( query_timestamp_begin, query_timestamp_end, bin_size)
        #get the bin indexes which have the required tweets
        #[1,2], [2,3] ... is the inteded bins
        #sadly pandas has no left-inclusive only option, so jan 1 of next year might be included
        tweets_binned = pd.cut(tweets['created_at'], bins, labels=range(1, bin_size), include_lowest=True)
        #get the count for each bin
        tweets_series = tweets['created_at'].groupby(tweets_binned).count()
        tweets_json  = tweets_series.to_json( force_ascii = False )
        return tweets_json

    


