import json
from flask import Flask, render_template
from statsgenerator import StatsGenerator

DATA_FILE = "./data/reeview_test.csv"

app = Flask(__name__)

@app.route('/')
def index():

    curr_year = 2014
    stats = StatsGenerator( DATA_FILE )
    top_tags = stats.top_hashtags( )
    top_tags_dict = json.loads(top_tags)

    ###
    # format for highcharts bar graph
    top_tags_highcharts_list = []
    for tag in top_tags_dict.keys():
        top_tags_highcharts_list.append( { "name" : tag, "data" : [top_tags_dict[tag]] } )
    top_tags_highcharts_json = json.dumps( top_tags_highcharts_list )
    app.logger.debug( top_tags_highcharts_json )
    ###

    return render_template("reeview.html", top_tags = top_tags_dict, highcharts_series = top_tags_highcharts_json, year= curr_year )

if __name__ == '__main__':
    app.run(debug=True)

