from graphy.backends import google_chart_api

monthly_rainfall = [3.2, 3.2, 2.7, 0.9, 0.4, 0.1, 0.0, 0.0, 0.2, 0.9, 1.8, 2.3]
months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()

chart = google_chart_api.LineChart(monthly_rainfall)
chart.bottom.labels = months print chart.display.Img(400, 300)
