# 接收一个影厅ID，返回该影厅下的所有座位信息
from flask import request
from tigereye.api import ApiView

from tigereye.models.cinema import Cinema
from tigereye.models.hall import Hall
from tigereye.helpers.code import Code
from tigereye.models.seat import Seat,SeatType

class HallView(ApiView):

    def all(self):
        return Hall.query.all()

    def seat(self):
        hid = request.args['hid']
        # 接受影厅id,找到这个影厅
        hall = Hall.get(hid)
        if not hall:
            return Code.hall_does_not_exist
        hall.seats = Seat.query.filter(Seat.hid==hid,Seat.seat_type != SeatType.road.value).all()
        # hall.seats_num = Seat.query.filter_by(hid=hid).all()
        # cinema.halls = Hall.query.filter_by(cid=cid).all()
        return hall