from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
import random
import json
import fib

# Set env variables to enable debug mode in local. $env:FLASK_ENV = "development"

app = Flask(__name__)

metrics = PrometheusMetrics(app)
# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

service1_counter = metrics.counter(
    'service1_counter', 'Request count by service 1',
    labels={'path': lambda: request.path}
)

# list of cat images
images = [
    "https://animalso.com/wp-content/uploads/2017/02/Golden-Retriever-12.jpg",
    "https://animalso.com/wp-content/uploads/2017/02/Golden-Retriever-11.jpg",
    "https://animalso.com/wp-content/uploads/2017/02/Golden-Retriever-10.jpg",
    "https://animalso.com/wp-content/uploads/2017/02/Golden-Retriever-09.jpg",
    "https://animalso.com/wp-content/uploads/2017/02/Golden-Retriever-08.jpg"  
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

@app.route("/<number>", methods=['GET'])
def get_fib(number):
    ''' Return Fibonacci JSON '''
    results = json.dumps(fib.get(int(number)))
    return render_template('results.html', resl=results)

@app.route("/service1", methods=['GET'])
@service1_counter
def service1():
    ''' Return Service 1 '''
    results = "This is just a service 1 test"
    return render_template('results.html', resl=results)

@app.route("/service2", methods=['GET'])
def service2():
    ''' Return Service 2 '''
    results = "This is just a service 2 test"
    return render_template('results.html', resl=results)

if __name__ == "__main__":
    app.run()
