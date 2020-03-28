import jwt


def generate_token(login, **info):
    """
    :param login: user login
    :param info: other user info
    :return: token
    """
    info_for_token = {'login': login}
    info_for_token.update(info)
    token = jwt.encode(info_for_token, 'secret', algorithm='HS256')
    return token


def decode_token(token):
    """
    :param token: user token
    :return: info - user info
    """
    info = jwt.decode(bytes(token, encoding='utf-8'), 'secret', algorithms=['HS256'])
    return info
