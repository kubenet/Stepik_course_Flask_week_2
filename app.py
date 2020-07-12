"""
    Проект первой недели по курсу "Flask с нуля"
    Ссылка на курс: https://stepik.org/course/61900

"""

from flask import Flask, render_template
from data import tours as tour, departures as depart, subtitle, description, title

app = Flask(__name__)  # объявляем экземпляр фласка


@app.route('/')  # объявим путь к главной странице
def index():
    return render_template('index.html', title=title, tours=tour, subtitle=subtitle, departures=depart,
                           description=description)


@app.route('/departures/<string:departure>')  # путь отобразить направления
def departures(departure):
    lst_depart = []  # список индексов туров из соответстующих направлению
    price_depart = []  # список цен подходящих туров
    count_nights = []  # список кол-во ночей подходящих туров

    for t in tour:
        if departure == tour[t]['departure']:
            lst_depart.append(t)
            price_depart.append(tour[t]['price'])
            count_nights.append(tour[t]['nights'])
    return render_template('departure.html', title=title, tours=tour, subtitle=subtitle,
                           lst_departures=lst_depart, departures=depart, city=departure,
                           description=description, price_depart=price_depart, count_nights=count_nights)


@app.route('/tours/<int:id>/')  # путь просмотра тура
def tours(id):
    return render_template('tour.html', title=title, tour_title=tour[id]['title'],
                           country=tour[id]['country'], departure=depart[tour[id]['departure']], departures=depart,
                           nights=tour[id]['nights'], description=tour[id]['description'],
                           picture=tour[id]['picture'], price=tour[id]['price'], stars=tour[id]['stars'])


if __name__ == "__main__":
    app.run()  # запустим сервер на 8000 порту, режим отладки включенен.
