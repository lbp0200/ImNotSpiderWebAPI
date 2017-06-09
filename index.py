from flask import Flask, jsonify, request
from ImNotSpider import ImNotSpider as imsp

app = Flask(__name__)


@app.route('/')
def index():
    func = request.args.get('func', 'random')
    num = request.args.get('num', 1)
    try:
        num = int(num)
    except:
        num = 1
    ins = imsp.ImNotSpider()
    if num > 1:
        ua_list = []
        i = 0
        while i < num:
            ua_list.append(getattr(ins, func)())
            i += 1
        return jsonify(ua_list)
    else:
        return getattr(ins, func)()


if __name__ == '__main__':
    app.run()
