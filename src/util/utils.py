from flask import jsonify

def response(succes, response, statusCode = 200):

    return jsonify({
        "succes": succes,
        "response": response
    }), statusCode

