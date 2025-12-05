from flask import Flask
from app import app

app = app

if __name__ == '__main__':
    app.run(port=8080, debug=True)
