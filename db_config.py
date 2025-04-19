class Config:
    # 基础配置
    SECRET_KEY = "test"

    # MySQL 数据库配置
    USERNAME = 'webdesign'  # 数据库账号
    PASSWORD = 'Fl231027'  # 数据库密码
    HOST = '39.96.125.213'  # 数据库服务器地址
    PORT = '3306'  # 数据库端口
    DATABASE = 'webdesign'  # 数据库名称
    CHARSET = 'utf8mb4'  # 字符编码

    # SQLAlchemy 配置
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset={CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False