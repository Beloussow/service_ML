from flask import Flask, request, jsonify
import pickle


with open('./models/model.pickle', 'rb') as f:
    model = pickle.load(f)


app_api = Flask(__name__)

@app_api.route('/knn', methods=['POST'])
def knn():
    data = request.get_json()
    return jsonify(answer=str(model.predict(data['query'])[0]))

@app_api.route('/', methods=['POST', 'GET'])
def hello():
    return jsonify(answer='Hello!!!')


if __name__ == '__main__':
    app_api.run(debug=False)

