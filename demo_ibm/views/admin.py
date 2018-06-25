from flask import Blueprint, jsonify, request

from server.UserServ import UserServer
from views.form.user_form import LoginForm, SignInForm, BindUserForm

bp = Blueprint('admin', __name__)

# from . import login


@bp.route('sign_in', methods=['POST'])
def create_user():
    form = SignInForm()
    data = form.data_with_csrf()
    # print(data)
    with UserServer() as s:
        s.create_user(**data)
    return jsonify(code=0, msg='success')


@bp.route('login', methods=['POST'])
def login():
    form = LoginForm()
    data = form.data_with_csrf()
    # print(data)
    with UserServer() as s:
        flag = s.login(**data)
        print(flag)
        if flag:
            return jsonify(code=0, data=dict(id=flag.id,
                                             user_name=flag.user_name,
                                             role=flag.role))
    return jsonify(code=1, data=None)


@bp.route('add_robot')
def add_robot():
    with UserServer() as s:
        rid = s.create_robot()
    return jsonify(code=0, data=rid)


@bp.route('sub_robot')
def sub_robot():
    with UserServer() as s:
        s.kill_robot()
    return jsonify(code=0)




@bp.route('all_robot')
def all_robot():
    with UserServer() as s:
        r = s.all_robot()
    return jsonify(code=0, data=dict(total=len(r),
                                     robol=[dict(
                                         id=i.id,
                                         place=i.place,
                                         status=i.status,
                                     ) for index, i in enumerate(r)]))


@bp.route('use_robot')
def use_robot():
    uid = request.args['uid']
    with UserServer() as s:
        rid = s.create_robot_msg(uid)
    return jsonify(code=0, data=rid)


@bp.route('get_resident')
def get_resident():
    with UserServer() as s:
        r = s.get_resident(**request.args.to_dict())
    return jsonify(code=0, data=[dict(id=rr.id,
                                      building=rr.building,
                                      address=rr.address,
                                      true_name=rr.true_name,
                                      telephone=rr.telephone,
                                      user_name=rr.user_id and s.get_name(rr.user_id),
                                      sex=rr.sex,)
                                 for index, rr in enumerate(r)])


@bp.route('bind_user', methods=['POST'])
def bind_user():
    form = BindUserForm()
    data = form.data_with_csrf()
    with UserServer() as s:
        s.bind_user(**data)
    return jsonify(code=0)


@bp.route('find_name')
def find_name():
    with UserServer() as s:
        n = s.find_name(**request.args.to_dict())
    return jsonify(code=0, data=n)


@bp.route('get_role')
def get_role():
    with UserServer() as s:
        n = s.get_role()
        d = {}
        for x in n:
            d[x.id] = x.role \
                      and [dict(id=k, name=s.get_name(k))
                           for k in x.role.split(';')] or []
    return jsonify(code=0, data=d)


@bp.route('del_role')
def del_role():
    with UserServer() as s:
        s.del_role(**request.args.to_dict())
    return jsonify(code=0)

