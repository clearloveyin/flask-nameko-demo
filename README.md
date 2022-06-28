# flask+nameko+rabbitMQ实现python微服务web方案
nameko作为微服务生产者，项目中order和user模块分别为用订单服务，用户服务。启动方式使用容器注册的方式，方便一块启动  
flask作为消费者（客户端），对外提供接口服务
rabbitMQ作为消息中间件
# 启动nameko
nameko run main
# 启动flask
export PYTHONPATH='.'  
export FLASK_APP=manger  
flask run
# 请求接口示例
http://localhost:5000/create/order  
http://localhost:5000/login

