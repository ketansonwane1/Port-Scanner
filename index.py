from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Initialize CSRF protection (not using a secret key)
csrf = CSRFProtect(app)

@app.route('/')
def home():
    return "Hello, World! This is served on port 5000."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
