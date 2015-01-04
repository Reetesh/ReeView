
function draw_bar_chart( json, year ) {
	$("#top-bar-container").highcharts({

	chart: {
		type: 'column'
	},

	title: {
		text: "#ReeView of top #ReeTags from " + year
	},

	xAxis: {
		categories: [
			year
		]
	},

	yAxis: {
		title: {
			text: "Number of tweets"
		}
	},
	
	series: json

	})
}
