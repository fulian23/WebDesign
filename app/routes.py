from flask import Blueprint, render_template

from app.models import db, Articles

import time,json
news = Blueprint('news', __name__, url_prefix='/news')

def timestamp_format(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t)))

@news.route('/<id>')
def news_page(id):
    print(id)
    article = db.session.query(Articles).filter(Articles.id == id).first().content
    # article={"title":"中国互联网协会、中国信息通信研究院共同发布《互联网信息服务算法推荐合规自律公约》","content":["为进一步贯彻落实《中华人民共和国网络安全法》《中华人民共和国数据安全法》《互联网信息服务管理办法》《电信和互联网个人信息保护规定》《互联网信息服务算法推荐管理规定》等相关法律法规，保障用户合法权益，促进互联网信息服务行业健康发展，在工业和信息化部信息通信管理局的指导下，中国互联网协会联合中国信息通信研究院研究起草了《互联网信息服务算法推荐合规自律公约》（以下简称《公约》），得到相关单位的积极响应。","<img src='../static/image/test.png'>","7月11日，《公约》发布仪式在2024（第二十三届）中国互联网大会闭幕式上举行。工业和信息化部信息通信管理局服务监督处相关负责人、中国互联网协会副秘书长裴玮、中国信息通信研究院技术与标准研究所所长张海懿与公约签署单位代表一同发布了《公约》。","<img src='../static/image/example.webp'>","张海懿介绍了《公约》研制背景，从保护用户隐私权、知情权、选择权、公平交易权等角度出发解读了《公约》的发起愿景和主要内容，并提出了行业可持续发展建议。她指出，信息服务算法推荐合规工作处于国家重视、人民关切的重要地位，需要行业内各单位提高政治站位、强化责任意识、建立规范体系、构建长效机制。"]}

    return render_template('news_detail_page.html', article=article)



