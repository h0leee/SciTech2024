from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


PRODUCTS = ["T-Shirts", "Calcões", "Camisolas", "Calças"]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)

@app.route('/status')
def about():
    return render_template('status.html')


def json(message):
    return jsonify({'message': message})


@app.route('/api/buy', methods=['POST'])
def api_buy():
    
    product = request.form.get('product')
    quantity = request.form.get('quantity')

    if  not product or not quantity:
        return json('Please provide all required fields'), 400

    if quantity <= 0:
        return json('Invalid'), 400
    

    # here call functions by rodrigo



    response = {
        'message': f'Your order for {quantity}x{product} has been received.',
    }

    return jsonify(response), 200




@app.route('/api/buyformat', methods=['POST'])
def api_buy_format():
    
    data = request.form.get('data')

    if  not data:
        return json('Please provide all required fields'), 400


    # here call functions by rodrigo

    response = {
        'message': f'Your order has been received.',
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)