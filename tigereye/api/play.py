# 写一个接口，接收一个排期ID，返回该排期的所有座位信息（不包含非座位信息）

from flask import request
from tigereye.api import ApiView

from tigereye.models.play import Play
from tigereye.models.hall import Hall
from tigereye.helpers.code import Code
from tigereye.models.seat import Seat,PlaySeat,SeatType
from tigereye.models.cinema import Cinema
from tigereye.helpers.vaildator import Validator


class PlayView(ApiView):

    def all(self):
        return Play.query.all()

    @Validator(pid=int)
    def seat(self):
        pid = request.params['pid']
        if not pid and not pid.isdigit():
            return Code.required_parameter_missing
        # 接受排期id,找到这个排期
        return PlaySeat.query.filter(PlaySeat.pid ==pid, PlaySeat.seat_type !=SeatType.road.value).all()


        # if not playseat:
        #     return Code.play_does_not_exist
        # # 找到这个排期（根据pid)对应的影厅
        # # hall = Hall.query.filter_by(hid=pid).all()
        # # # 根据找到的影厅来找对应的位置
        # # hall.seats_num = Seat.query.filter_by(hid=hall.hid).all()
        #
        # #这个排期的所有排期座位
        # cid = playseat.cid
        # seats = Seat.query.filter_by(cid=cid).all()
        # newlist=[]
        # for seat in seats:
        #     if seat.seat_type !=0:
        #         newlist.append(seat)
        # return newlist