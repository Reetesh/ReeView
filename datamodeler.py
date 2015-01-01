import json
import time
import pandas as pd
import os

class DataModeler: 
    #TODO check if file empty or some other meaningful logic
    def load_tweets(self):
        if tweets == null:
            loadTweetsFromTwitterArchive()
            #"%a %b %d %H:%M:%S +0000 %Y"
        else:
            fetchTweetsSinceLast()

    # based off of twitter archive retrieved from profile on Dec 31 2014
    # current REST API version = v1.1
    #TODO sanitize the js files received by removing the first line of all files.
    def load_tweets_from_twitter_archive(self, archive_dir, data_file):
        df = pd.DataFrame(columns=('tweet_id', 'hashtag', 'created_at', 'user_id', 'tweet_text'))
        for js_filename in os.listdir(archive_dir):
            js_file = open(archive_dir + "/" + js_filename)
            tweets_loaded = json.load(js_file)
            for tweet in tweets_loaded:
                timestamp = time.mktime(time.strptime(tweet['created_at'], "%Y-%m-%d %H:%M:%S +0000"))
                hashtags = tweet['entities']['hashtags']
                if hashtags:
                    for hashtag in hashtags:
                        row_id = str(tweet["id"]) + "#" + hashtag["text"] + "@" + str(hashtag["indices"][0])
                        df.loc[row_id] = [tweet["id"], hashtag["text"], timestamp, tweet["user"]["id"], tweet["text"]]
                else:
                    row_id = tweet["id"]
                    df.loc[row_id] = [ tweet["id"], "", timestamp, tweet["user"]["id"], tweet['text'] ]
            js_file.close()
        #data from all files is now in the DataFrame
        self.write_tweets_to_csv( df, data_file )

    # write dataframe to a csv (csv is more readable)
    #TODO a tool that will convert this csv to json if portability need arises
    @staticmethod
    def write_tweets_to_csv( df, filename ):
        df.to_csv( filename, index_label = "row_id", encoding="utf-8" )
