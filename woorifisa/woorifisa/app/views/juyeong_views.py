from flask import Blueprint

juyeong = Blueprint('juyeong', __name__, url_prefix='/juyeong')

@juyeong.route('/about_me')
def about_me():
    return f'저는 {__name__}입니다'

@juyeong.route('/hello')
def hello():
    return f'안녕하세요'

@juyeong.route('/bye')
def bye():
    return f'잘 가세요'