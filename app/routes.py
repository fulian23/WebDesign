from flask import Blueprint

from app.models import Users

test = Blueprint('test', __name__, url_prefix='/test')

@test.route('/')
async def hello_world():
    a=await Users.get(name="1111")
    print(a)
    return a.passw



