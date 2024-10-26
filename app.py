from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)



PRODUCTS = ["T-Shirts", "Calcões", "Camisolas", "Calças"]


######## GENERAL FUNCTIONS


def json(message):
    return jsonify({'message': message})



@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)

@app.route('/status')
def status():
    return render_template('status.html')



@app.route('/upload')
def upload():
    return render_template('upload.html')



@app.route('/api/buy', methods=['POST'])
def api_buy():
    
    product = request.form.get('product')
    quantity = int(request.form.get('quantity'))

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

    if not data:
        return json('Please provide required fields'), 400


    # here call functions by goncalo

    response = {
        'message': f'Your order has been received.',
    }

    return jsonify(response), 200


@app.route('/api/upload', methods=['POST'])
def api_upload():

    if 'file' not in request.files:
        return json('No file part in the request'), 400

    file = request.files['file']

    if file.filename == '':
        return json('No selected file'), 400

    file_content = file.read().decode('utf-8')  # assuming the file is text-based

    # Return a success response with the file content
    response = {
        'message': f'File "{file.filename}" read successfully!{file_content}',
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)