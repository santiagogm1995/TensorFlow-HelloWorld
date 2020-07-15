from flask import Flask, render_template, request, jsonify, abort
import os
import json
import requests
import tensorflow as tf



app = Flask(__name__)

@app.route('/')
def home():
    hello = tf.constant('Hello, TensorFlow!')

    # Start tf session
    sess = tf.Session()

    # Run the op
    print(sess.run(hello))
    return sess.run(hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
