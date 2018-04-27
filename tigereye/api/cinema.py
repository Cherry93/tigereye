from flask import request
from tigereye.api import ApiView

from tigereye.models.cinema import Cinema
from tigereye.models.hall import Hall
from tigereye.helpers.code import Code
from tigereye.helpers.vaildator import Validator

class CinemaView(ApiView):

    def all(self):
        return Cinema.query.all()
    @Validator(cid = int)
    def halls(self):
        cid = request.params['cid']
        cinema = Cinema.get(cid)
        if not cinema:
            return Code.cinema_does_not_exist
        cinema.halls = Hall.query.filter_by(cid=cid).all()
        return cinema
