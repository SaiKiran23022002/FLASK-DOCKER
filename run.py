from app import create_app

app = create_app() #creating an instance of Flask application using create_app method


if __name__=="__main__":  # Check if the script is run directly
    app.run(host="0.0.0.0",port="5000")  # Run the Flask app on all available IP addresses at port 5000
