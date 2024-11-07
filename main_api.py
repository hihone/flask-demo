from flask import Flask
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app, prefix='/app/', version='1.0', title='API', description='api 文档')

demo = Namespace('demo', description='测试')

@demo.route('')
class Index(Resource):
    def get(self):
        return {'code': 0, 'message': 'hello world'}

@demo.route('/info/<id>')
class Detail(Resource):
    def get(self, id):
        data = {
            'id': id,
            'title': '详情页面',
        }
        return {'code': 0, 'message': '请求成功', 'data': data}

api.add_namespace(demo, '/index')
api.add_namespace(demo, '/info/<id>')

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)