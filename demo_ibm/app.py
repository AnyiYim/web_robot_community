from flask import Flask, url_for, jsonify
from sqlalchemy import MetaData

from core._mysql import base, engine

# 自动创建表
from views import app

# base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    app.run()
