from datetime import datetime
from data import config
from mysql.connector import connect, Error


class SQLighter:

    def __init__(self) -> None:
        try:
            self.myconn=connect(
                host = config.HOST,
                user = config.USER,
                password = config.PASSWORD,
                database = config.DB,
            )
            self.cur = self.myconn.cursor()
            print('connect to DB')
        except Error as e:
            print(e)


    def get_date_start(self):
        self.myconn.close()
        self.__init__()
        self.cur.execute("SELECT MIN(time_start) FROM `schedule`;")
        self.result = self.cur.fetchone()
        return self.result[0]

    
    def get_date_end(self):
        self.myconn.close()
        self.__init__()
        self.cur.execute("SELECT MAX(time_end) FROM schedule;")
        self.result = self.cur.fetchone()
        return self.result[0]


    # Методы извлечения данных
    def what_now_db(self, tdate):
        """Возвращает пользователю список кортежей с мероприятиями

        Args:
            tdate (datetime): текущее время и дата

        Returns:
            list: список кортежей с мероприятиями
        """
        self.myconn.close()
        self.__init__()
        self.cur.execute("SELECT name, time_start, time_end "
                        "FROM schedule INNER JOIN event ON schedule.event_name_id = event.id "
                        "WHERE time_start <= '%s' AND time_end >= '%s'" % (tdate, tdate))
        self.result = self.cur.fetchall()
        return self.result


    def what_next_db(self, tdate):
        self.myconn.close()
        self.__init__()
        self.cur.execute("SELECT `name`, `time_start` "
                        "FROM `schedule` INNER JOIN `event` " 
                        "ON `schedule`.`event_name_id` = `event`.`id` "
                        "WHERE `time_start` > '%s' " 
                        "ORDER BY `time_start` "
                        "LIMIT 2;"%(tdate))
        self.result = self.cur.fetchall()
        return self.result


SQL = SQLighter()