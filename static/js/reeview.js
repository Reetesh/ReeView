
function draw_bar_chart( json, x_axis, title_text ) {
	$("#top-bar-container").highcharts({

	chart: {
		type: 'column'
	},

	title: {
		text: "#ReeView of " + title_text + " from " + x_axis
	},

	xAxis: {
		categories: [
			x_axis
		]
	},

	yAxis: {
		title: {
			text: "Number of tweets"
		}
	},

    plotOptions: {
        series: {
            cursor: 'pointer',
            point: {
                events: {
                    click: function () {

                        location.href =  '/tag/' + this.series.name;
                    }
                }
            }
        }
    },
	
	series: json

	})
}
