from flask import Flask,Blueprint

root_file = Blueprint("routes_files",__name__)

@root_file.get('/')
def hello_world():  # put application's code here

    return  "Hello world"