from flask import Flask
import logging
from elasticsearch import Elasticsearch

logging.basicConfig(level=logging.INFO)

class ElasticsearchHandler(logging.Handler):
    def __init__(self, hosts):
        super().__init__()
        self.client = Elasticsearch(hosts=hosts)
        self.index_name = "backend-logs"
        self.create_index_if_not_exists()

    def create_index_if_not_exists(self):
        if not self.client.indices.exists(index=self.index_name):
            self.client.indices.create(index=self.index_name, body={})
            print(f"Index {self.index_name} created")

    def emit(self, record):
        log_entry = self.format(record)
        try:
            response = self.client.index(index=self.index_name, document={
                "message": log_entry
            })
            print("Log entry successfully indexed:", response)
        except Exception as e:
            print("Error indexing log entry:", e)

app = Flask(__name__)

es_handler = ElasticsearchHandler(hosts=['http://elasticsearch:9200'])
es_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
es_handler.setFormatter(formatter)
app.logger.addHandler(es_handler)

@app.route('/')
def hello_world():
    app.logger.info('Main page was accessed')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

