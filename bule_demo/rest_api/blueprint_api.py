from flask import jsonify, Blueprint, request
from flask_restx import Api, Resource

doc_config = dict(
    doc='/swagger/',
    version='1.0',
    title='api 接口文档',
    description='api 接口文档',
    default="API",
    default_label="/api/v1",
    swagger="2.0"
)

mod = Blueprint('api_demo', __name__, url_prefix='/api/demo/v1')
api = Api(mod, **doc_config)

@api.route('/health/check')
class Health(Resource):
    def get(self):
        return jsonify(code=0)


@api.route('/index')
class Index(Resource):
    def get(self):
        return jsonify(code=0)

    post_parser = api.parser()
    post_parser.add_argument('name', type=str, location='form', required=True)
    post_parser.add_argument('nickname', type=str, location='form', required=True)

    @api.expect(post_parser)
    @api.doc(description='方法备注')
    def post(self):
        return jsonify(code=0, data={
            'total': 0,
            'data': {
                'name': request.form.get('name'),
                'nickname': request.form.get('nickname'),
            },
        })
