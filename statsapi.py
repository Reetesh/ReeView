import json
from flask import Flask, render_template
from statsgenerator import StatsGenerator

DATA_FILE = "./data/reeview_test.csv"

app = Flask(__name__)

def get_highcharts_series_json( stats_json ):

    highcharts_dict = json.loads(stats_json)
    highcharts_list = []
    for key in highcharts_dict.keys():
        highcharts_list.append( { "name" : key, "data" : [highcharts_dict[key]] } )
    highcharts_json = json.dumps( highcharts_list )
    return highcharts_json

@app.route('/')
def index():

    curr_year = 2014
    stats = StatsGenerator( DATA_FILE )
    top_tags = stats.top_hashtags()
    
    top_tags_highcharts_json  = get_highcharts_series_json( top_tags )
    app.logger.debug( top_tags_highcharts_json )
    
    return render_template("reeview.html", highcharts_series = top_tags_highcharts_json, x_axis= curr_year, title = "Top #ReeTags" )

@app.route('/tag/<tag>')
def tag_details(tag):
    
    curr_year = 2014
    stats = StatsGenerator(DATA_FILE)
    
    tag_frequency = stats.tag_breakdown( tag, curr_year )

    tag_frequency_highcharts_json  = get_highcharts_series_json( tag_frequency )
    app.logger.debug( tag_frequency_highcharts_json )
    
    return render_template("reeview.html", highcharts_series = tag_frequency_highcharts_json, x_axis= curr_year, title = "#"+tag)

    
    
if __name__ == '__main__':
    app.run(debug=True)

