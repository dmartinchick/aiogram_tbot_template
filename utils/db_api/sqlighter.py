from datetime import datetime
from data import config
from mysql.connector import connect, Error


class SQLighter:

    def __init__(self) -> None:
        try:
            self.myconn=connect(
                host = config.HOST,
                user = config.USER,
                pasword = config.PASSWORD,
                database = config.DB,
            )
            self.cur = self.myconn.cursor()
            print('connect to DB')
        except Error as e:
            print(e)


    # Методы извлечения данных
    def what_now_db(self):
        self.myconn.close()
        self.__init__()
        self.tdate = datetime.today()
        self.cur.execute("SELECT name, time_start, time_end, address, contains "
                        "FROM schedule INNER JOIN event ON schedule.name_id = event.id "
                        "WHERE time_start <= '%s' AND time_end >= '%s'" % (self.tdate, self.tdate))
        self.result = self.cur.fetchall()
        return self.result
