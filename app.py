from flask import Flask, request, render_template, redirect, url_for
import json
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
      city = request.form['city'].capitalize()
  else:
      #for default city
      city = 'delhi'.capitalize()

    # source contain json data from api
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0879920376ab99f52ea39ec8a65cfa93'.format(
      city)
  res = requests.get(url).text

  list_of_data = json.loads(res)

  # data for variable list_of_data
  data = {
      "City": str(list_of_data['name']),
      "Country": str(list_of_data['sys']['country']),
      "Coordinate": str(list_of_data['coord']['lon'])+' Lat.' + ' ' + str(list_of_data['coord']['lat'])+' Long.',
      "Temperature": str(list_of_data['main']['temp']),
      "Pressure": str(list_of_data['main']['pressure']),
      "Humidity": str(list_of_data['main']['humidity']),
  }
  print(data)
  return render_template('index.html', data=data)


if __name__ == '__main__':
  app.run()
