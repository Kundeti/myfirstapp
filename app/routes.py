from app import app

@app.route('/home')
def home():
    return 'Welcome to Python'