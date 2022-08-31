from flask import Flask, jsonify

"""INSTANCE"""
app = Flask(__name__)

"""SET CONFIGURATION"""
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def pin_pong() :
    return jsonify({
        'status': 'success',
        'messge': 'pong' 
    })