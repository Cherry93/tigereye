from tigereye.api import ApiView
from flask import request
from tigereye.helpers.vaildator import Validator,multi_int
from tigereye.models.play import Play
from tigereye.models.seat import PlaySeat
from tigereye.helpers.code import Code
from tigereye.models.order import Order,OrderStatus
from flask_classy import route


class SeatView(ApiView):

    @Validator(pid=int,sid=multi_int,price=int,orderno=str)
    @route('/lock/',methods=['POST'])
    def lock(self):
        pid = request.params['pid']
        sid = request.params['sid']
        price = request.params['price']
        orderno = request.params['orderno']
        play = Play.get(pid)
        if not play:
            return Code.play_does_not_exist
        if price < play.lowest_price:
            return Code.prcice_less_than_the_lowest_price
        lockes_seats_num = PlaySeat.lock(orderno,pid,sid)
        if not lockes_seats_num:
            return Code.seat_lock_failed
        order = Order.create(play.cid,pid,sid)
        order.seller_order_no=orderno
        order.status=OrderStatus.locked.value
        order.tickets_num=lockes_seats_num
        order.save()
        return {'locked_seats_num':lockes_seats_num}

    @Validator(pid=int, sid=multi_int, orderno=str)
    @route('/unlock/', methods=['POST'])
    def unlock(self):
        pid = request.params['pid']
        sid = request.params['sid']
        orderno = request.params['orderno']
        order = Order.getby_orderno(orderno)
        if not order:
            return Code.order_does_not_exist
        if order.status !=OrderStatus.locked.value:
            return Code.order_status_error
        unlock_seats_num = PlaySeat.unlock(order,pid,sid)
        if not  unlock_seats_num:
            return Code.seat_lock_failed
        order.status = OrderStatus.unlocked.value
        order.save()
        return {'unlock_seats_num':unlock_seats_num}


