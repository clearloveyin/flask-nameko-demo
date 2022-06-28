from nameko.rpc import rpc


class OrderSvc(object):
    name = "order_service"

    @rpc
    def create_order(self, order_no):
        return '订单创建成功，订单号：{}'.format(order_no)