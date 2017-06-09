# ImNotSpiderWebAPI 浏览器User Agent生成器的Web接口

## 部署
```bash
virtualenv -p python3 im_not_spider
cd im_not_spider
source bin/activate
pip install flask
pip install git+https://github.com/lbp0200/ImNotSpider.git
git clone https://github.com/lbp0200/ImNotSpiderWebAPI
cd ImNotSpiderWebAPI
FLASK_APP=index.py flask run -h 0.0.0.0
```
访问[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

http://127.0.0.1:5000/?func=wap&num=5

调用ImNotSpider的wap方法，生成UserAgent数量为5
