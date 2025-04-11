from flask import Blueprint, render_template, request

from app.models import db, Articles

import time,json
news = Blueprint('news', __name__, url_prefix='/news')

def timestamp_format(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t)))


@news.route('/search')
def search_articles():
    # 获取搜索关键词（重要：需做输入过滤）
    keyword = request.args.get('q', '').strip()
    print(1111)

    # 基本参数校验
    if not keyword:
        return render_template('search.html', error="请输入搜索关键词")

    search_pattern = f"%{keyword}%"
    query = Articles.query.filter(
        Articles.title.ilike(search_pattern)
    ).order_by(Articles.timestamp.desc())
    print(query.statement)

    # 分页处理
    page = request.args.get('page', 1, type=int)
    pagination = query.paginate(page=page, per_page=2)
    return render_template('search.html',
                           results=pagination.items,
                           pagination=pagination,
                           keyword=keyword)


@news.route('/<id>')
def news_page(id):
    print(id)
    article = db.session.query(Articles).filter(Articles.id == id).first().content
    return render_template('news_detail_page.html', article=article)



