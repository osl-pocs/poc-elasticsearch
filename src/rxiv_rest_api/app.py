from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['http://es:9200'])

@app.route('/article')
def search_article():
    query = request.args.get('q')
    response = es.search(index="your_index", body={"query": {"match": {"content": query}}})
    return jsonify(response['hits']['hits'])


@app.route('/list')
def search_list():
    query = request.args.get('q')
    response = es.search(index="your_index", body={"query": {"match": {"content": query}}})
    return jsonify(response['hits']['hits'])


# @app.route('/dataload', methods=['GET'])
# def dataload():
#     data_source_url = "data_source_url"  # Replace with your data source URL
#     response = requests.get(data_source_url)
#     if response.status_code == 200:
#         data = response.json()
#         # Assuming `data` is a list of documents
#         for doc in data:
#             res = es.index(index="your_index", document=doc)
#         return jsonify({"message": "Data loaded successfully"}), 200
#     else:
#         return jsonify({"error": "Failed to fetch data"}), 500


@app.route('/')
def main():
    # swagger
    return jsonify({"message": "not available"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
