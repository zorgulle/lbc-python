from flask import request
from flask_api import FlaskAPI

from connector import Connector

app = FlaskAPI(__name__)

@app.route('/ads', methods=['GET'])
def list_ads():
    """
    Params accepted
    ===============
      - Search text
    Use case
    ========
     - http://mysite.com/ads?search-text=foo
    :return: Dict of ads found with the params
    """

    request_params = request.args
    connector = Connector()
    params = {
        "search-text": request_params['search-text']
    }
    connector = connector.get_ads(params)


    return {'ads': []}

@app.route('/', methods=['GET'])
def index():
    return {"message": "ok"}

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)