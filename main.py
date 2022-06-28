from nameko.runners import ServiceRunner
from order.service import OrderSvc
from user.service import UserSvc

runner = ServiceRunner(config={'AMQP_URI': "amqp://guest:guest@localhost"})
runner.add_service(OrderSvc)
runner.add_service(UserSvc)





