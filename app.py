from flask import Flask, render_template, request, jsonify
import os
import functions as fc
import parse as ps
app = Flask(__name__)



PRODUCTS = ["T-Shirts", "Calcões", "Camisolas", "Calças"]
SIZES = ['XS', 'S', 'M', 'L', 'XL']

######## GENERAL FUNCTIONS

def json(message):
    return jsonify({'message': message})


manager = fc.StockManager()



##########################

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS, sizes=SIZES)

@app.route('/status')
def status():
    return render_template('status.html')



@app.route('/upload')
def upload():
    return render_template('upload.html')



@app.route('/format')
def format():
    return render_template('format.html')


@app.route('/api/buy', methods=['POST'])
def api_buy():
    
    product = request.form.get('product')
    
    
    quantity = int(request.form.get('quantity'))
    size = request.form.get('size')


    if not product or not quantity or not size:
        return json('Please provide all required fields'), 400
    if product in PRODUCTS:
        productid = PRODUCTS.index(product)
    if size in SIZES:
        sizeid = SIZES.index(size)

    if quantity <= 0:
        return json('Invalid'), 400
    
    manager.manage_order([{'type': productid, 'qty': quantity,'size': sizeid}])

    response = {
        'message': f'Your order for {quantity}x{product} has been received.',
    }

    return jsonify(response), 200


@app.route('/api/date', methods=['POST'])
def api_date():
    date = manager.date
    print(date)
    return jsonify({'date': date}), 200


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

    manager.manage_order(ps.parse_content(file_content))

    response = {
        'message': f'File "{file.filename}" read successfully! {file_content}',
    }
    return jsonify(response), 200


@app.route('/api/history', methods=['GET'])
def api_history():

    return jsonify(manager.history)

@app.route('/api/encomenda', methods=['GET'])
def api_encomenda():
    return jsonify(manager.encomendas)


@app.route('/api/atual', methods=['GET'])
def api_atual():
    return jsonify(manager.stock_levels)




if __name__ == '__main__':
    app.run(debug=True)