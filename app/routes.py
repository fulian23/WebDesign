from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from app.models import db, Articles, Comments

import time

news = Blueprint('news', __name__, url_prefix='/news')


@news.route('/search')
def search_articles():
    # 获取搜索关键词（重要：需做输入过滤）
    keyword = request.args.get('q', '').strip()

    # 基本参数校验
    if not keyword:
        return render_template('search.html', error="请输入搜索关键词")

    search_pattern = f"%{keyword}%"
    query = Articles.query.filter(
        Articles.title.ilike(search_pattern)
    ).order_by(Articles.timestamp.desc())

    # 分页处理
    page = request.args.get('page', 1, type=int)
    pagination = query.paginate(page=page, per_page=2)
    return render_template('search.html',
                           results=pagination.items,
                           pagination=pagination,
                           keyword=keyword)


@news.route('/<int:news_id>')
def article_detail(news_id):
    # 获取文章并预加载关联数据
    article = Articles.query.options(
        db.joinedload(Articles.comments)  # 加载评论
        .joinedload(Comments.commenter)  # 加载评论者信息
    ).get_or_404(news_id)

    # 分页参数处理
    page = request.args.get('page', 1, type=int)
    per_page = 10  # 每页评论数

    # 获取分页对象
    comments_query = Comments.query.filter_by(article_id=article.id)
    comments_pagination = comments_query.order_by(
        Comments.timestamp.desc()
    ).paginate(page=page, per_page=10)

    return render_template(
        'news_detail_page.html',
        article=article,
        comments=comments_pagination.items,
        pagination=comments_pagination
    )


@news.route('/<int:news_id>/comment', methods=['POST'])
@login_required
def post_comment(news_id):
    # 获取文章对象
    article = Articles.query.get_or_404(news_id)

    # 获取并验证评论内容
    content = request.form.get('content', '').strip()
    if not content:
        flash('评论内容不能为空', 'error')
        return redirect(url_for('article_detail', news_id=article.id))

    # 创建评论对象
    new_comment = Comments(
        content=content,
        user_id=current_user.id,
        article_id=article.id,
        timestamp=int(time.time())
    )

    # 数据库操作
    try:
        db.session.add(new_comment)
        db.session.commit()
        flash('评论发布成功', 'success')
    except Exception as e:
        db.session.rollback()
        flash('评论发布失败，请稍后重试', 'error')

    return redirect(url_for('news.article_detail', news_id=article.id))



