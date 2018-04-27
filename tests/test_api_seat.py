from tigereye.models.seat import SeatStatus
from tigereye.helpers.code import Code
from .helper import FlaskTestBase


class TestApiSeat(FlaskTestBase):

    pid = 1
    sid_list = [1, 2]
    sid = ','.join([str(i) for i in sid_list])
    price = 5000
    orderno = 'test-%s-%s' % (pid, sid)

    def test_seat1_lock(self):
        locked_seats_num = len(self.sid_list)
        rv = self.get_succ_json('/seat/lock/', method='POST',
                                orderno=self.orderno,
                                pid=self.pid,
                                price=self.price,
                                sid=self.sid
                                )
        self.assertEqual(rv['data']['locked_seats_num'], locked_seats_num)

        # 确认座位图已经发生改变
        rv = self.get_succ_json('/play/seat/', pid=self.pid)
        succ_count = 0
        for seat in rv['data']:
            if seat['orderno'] == self.orderno:
                self.assertEqual(seat['status'], SeatStatus.locked.value)
                succ_count += 1
        self.assertEqual(succ_count, locked_seats_num)
        # 再请求一次，确认锁座失败
        rv = self.get_json('/seat/lock/', method='POST',
                                orderno=self.orderno,
                                pid=self.pid,
                                price=self.price,
                                sid=self.sid
                                )
        self.assertEqual(rv['rc'], Code.seat_lock_failed.value)

    def test_seat2_unlock(self):
        # 传递各种参数
        locked_seats_num = len(self.sid_list)
        rv = self.get_succ_json('/seat/lock/', method='POST',
                                orderno=self.orderno,
                                pid=self.pid,
                                price=self.price,
                                sid=self.sid
                                )
    def test_seat1_unlock(self):
        locked_seats_num = len(self.sid_list)
        rv = self.get_succ_json('/seat/lock/', method='POST',
                                orderno=self.orderno,
                                pid=self.pid,
                                price=self.price,
                                sid=self.sid
                                )
        self.assertEqual(rv['data']['locked_seats_num'], locked_seats_num)

        # 确认座位图已经发生改变
        rv = self.get_succ_json('/seat/unlock', method='POST',
                                orderno=self.orderno,
                                pip=self.pid,
                                sid=self.sid
                                )
        self.assertEqual(rv['data']['unlock_seats_num'],locked_seats_num)

        rv = self.get_succ_json('play/seats',pid=self.pid)
        succ_count=0
        for seat in rv['data']:
            if seat['sid'] in self.sid_list:
                self.assertEqual(succ_count,seat)




