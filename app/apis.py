from flask import Blueprint, request, redirect, url_for, flash
import os, hashlib, time

from app.models import db, Users

api = Blueprint('search', __name__, url_prefix='/api')

def md5(name):
    m = hashlib.md5()
    m.update(name.encode('utf-8'))
    return m.hexdigest()

@api.route('/uploadAvatar', methods=['POST'])
def upload_avatar():
    image = request.files['avatar']
    ext = image.filename.split('.')[-1]
    if ext not in ['jpg', 'png', 'jpeg']:
        return {"message": "图片格式错误"}, 400
    filename = md5(image.filename+str(time.time()))+'.'+ext
    image.save(os.path.join('static', 'avatars', filename))
    db.session.query(Users).filter_by(username=request.form.get("username")).first().avatar=filename
    db.session.commit()
    return redirect(url_for('dashboard'))
@api.route('/changeUsername', methods=['POST'])
def change_username():
    if Users.query.filter_by(username=request.json.get("username")).first():
        return {"message": "用户名已被使用"}, 409
    else:
        db.session.query(Users).filter_by(username=request.json.get("username")).first().username=request.json.get("new_username")
        db.session.commit()
        return redirect(url_for('dashboard'))
@api.route('/changePassword', methods=['POST'])
def change_password():
    db.session.query(Users).filter_by(username=request.json.get("username")).first().password=request.json.get("new_password")
    db.session.commit()
    return redirect(url_for('dashboard'))
