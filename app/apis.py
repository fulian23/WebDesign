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
    print("test")
    print(request.files)
    image = request.files['avatar']
    ext = image.filename.split('.')[-1]
    if ext not in ['jpg', 'png', 'jpeg']:
        return {"message": "图片格式错误"}, 400
    filename = md5(image.filename+str(time.time()))+'.'+ext
    image.save(os.path.join('static', 'avatars', filename))
    user = db.session.query(Users).filter_by(username=request.form.get("username")).first()
    print(user.avatar)
    if user.avatar == "/static/avatars/default.jpg":
        user.avatar="/static/avatars/"+filename
    else:
        os.remove(user.avatar[1:])
        user.avatar="/static/avatars/"+filename
    db.session.commit()
    return{"message": "上传成功", "avatar_url": user.avatar}
@api.route('/changeUsername', methods=['POST'])
def change_username():
    if Users.query.filter_by(username=request.json.get("new_username")).first():
        return {"message": "用户名已被使用"}, 409
    else:
        db.session.query(Users).filter_by(username=request.json.get("old_username")).first().username=request.json.get("new_username")
        db.session.commit()
        return {"message": "修改成功"}
@api.route('/changePassword', methods=['POST'])
def change_password():
    print(request.json.get("username"))
    if Users.query.filter_by(username=request.json.get("username")).first().verify_password(request.json.get("new_password")):
        return {"message": "新密码不可与旧密码一致"}, 401
    db.session.query(Users).filter_by(username=request.json.get("username")).first().password=request.json.get("new_password")
    db.session.commit()
    return {"message": "修改成功"}
