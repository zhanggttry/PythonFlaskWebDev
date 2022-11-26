from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    #添加建立网络连接代码

    #主程序循环更新画面
    return 'Hello to the World of Flask!'

if __name__ == '__main__':
    app.run()