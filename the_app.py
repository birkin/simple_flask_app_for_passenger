# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import flask


app = flask.Flask(__name__)


@app.route( '/hello', methods=['GET'] )
def hi():
    return flask.jsonify( {'hello': 'world'} )

@app.route( '/bad_url', methods=['GET'] )
def oops():
    """ Generates error to test passenger error-handling. """
    1/0
    return flask.jsonify( {'sorry': 'you\'ll never see this'} )




if __name__ == '__main__':
    if os.getenv('DEVBOX') == 'true':
        app.run( host='0.0.0.0', debug=True )
    else:
        app.run()
