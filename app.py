
from flask import Flask, current_app, flash, jsonify, make_response, redirect, request, url_for
from argparse import ArgumentParser
from zlib import decompress
from base45 import b45decode
from cose.messages import CoseMessage
from cbor2 import loads
import json
import argparse
app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route("/")
def hello():
    return "Hello"

@app.route('/', methods=['POST'])
def decoding():
    return jsonify({'Result':'success'})