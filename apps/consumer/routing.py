from apps.consumer.blueprint import bp
from apps.consumer.handlers import ConsumerView, login, register


bp.add_route(ConsumerView.as_view(), '<id:int>/', name='consumer')
bp.add_route(login, 'login/', methods=['POST'], name='login')
bp.add_route(register, 'register/', methods=['POST'], name='register')