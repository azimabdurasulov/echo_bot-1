# Import library
from flask import Flask, request, jsonify

# Create an instance of Flask
app = Flask(__name__)

# Create a route
@app.route('/api', methods=['POST'])
def api():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    output = {'message': 'Hello World'}
    return output


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

