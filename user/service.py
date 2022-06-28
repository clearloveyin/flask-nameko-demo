from nameko.rpc import rpc


class UserSvc(object):
    name = "user_service"

    @rpc
    def login(self, phone):
        return '登陆成功，手机号：{}'.format(phone)