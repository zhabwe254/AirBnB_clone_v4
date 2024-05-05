from flask import Flask, render_template
import uuid

app = Flask(__name__)


@app.route('/0-hbnb/')
def index():
    cache_id = uuid.uuid4()
    return render_template('0-hbnb.html', cache_id=cache_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
