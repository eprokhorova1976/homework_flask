from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to online excursions shop. Choose what you are interested in.'


# @app.route('/excursions/')
# def excursions():
#     return render_template('excursions.html')


@app.route('/daily_diving/')
def daily_diving():
    return render_template('daily.html')


@app.route('/excursions/')
def excursions():
    excursions= [
        {"title":"Daily diving", "price":"45$ p.p.", "img":"/static/images/2.png", "address":"/daily/",
         "description":"Full day trip. 2 diving, transfer, equipment, lunch, soft drinks"},
        {"title": "Wreck diving. Salem Express", "price": "150$ p.p.", "img":"/static/images/3.png", "address":"#",
         "description": "Full day trip. 2 diving (wreck, coral reef), transfer, equipment, lunch, soft drinks"},
        {"title": "Night diving", "price": "60$ p.p.", "img":"/static/images/4.png", "address":"#",
         "description": "Full day trip. 1 diving, transfer, equipment"}
    ]
    return render_template('excursions.html', excursions=excursions)


if __name__=='__main__':
    app.run()
