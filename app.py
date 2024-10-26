from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/api/buy', methods=['POST'])
def api_buy():
    # Retrieve data from the form submission
    name = request.form.get('name')
    product = request.form.get('product')
    quantity = request.form.get('quantity')
    
    # Check if required fields are provided
    if not name or not product or not quantity:
        return jsonify({'error': 'Please provide all required fields'}), 400





if __name__ == '__main__':
    app.run(debug=True)