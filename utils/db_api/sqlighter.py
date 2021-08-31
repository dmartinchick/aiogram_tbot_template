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


    def reconnect(self):
        self.myconn.close()
        self.__init__()

    # Методы извлечения данных
    def get_date_start(self):
        self.reconnect()
        self.cur.execute("SELECT MIN(time_start) FROM `schedule`;")
        self.result = self.cur.fetchone()
        return self.result[0]

    
    def get_date_end(self):
        self.reconnect()
        self.cur.execute("SELECT MAX(time_end) FROM schedule;")
        self.result = self.cur.fetchone()
        return self.result[0]


    def what_now_db(self, tdate):
        """Возвращает пользователю список кортежей с мероприятиями

        Args:
            tdate (datetime): текущее время и дата

        Returns:
            list: список кортежей с мероприятиями
        """
        self.reconnect()

        self.cur.execute("SELECT name, time_start, time_end "
                        "FROM schedule INNER JOIN event ON schedule.event_name_id = event.id "
                        "WHERE time_start <= '%s' AND time_end >= '%s'" % (tdate, tdate))
        self.result = self.cur.fetchall()
        return self.result


    def what_next_db(self, tdate):
        self.reconnect()

        self.cur.execute("SELECT `name`, `time_start` "
                        "FROM `schedule` INNER JOIN `event` " 
                        "ON `schedule`.`event_name_id` = `event`.`id` "
                        "WHERE `time_start` > '%s' " 
                        "ORDER BY `time_start` "
                        "LIMIT 2;"%(tdate))
        self.result = self.cur.fetchone()
        return self.result
    

    def contests_db_list(self):
        self.reconnect()

        self.cur.execute("SELECT `name`, `name_en` "
                        "FROM `event` "
                        "WHERE `name_en` IS NOT NULL;")
        self.result = self.cur.fetchall()
        return self.result


    def contests_db(self, name_en):
        self.reconnect()

        self.cur.execute("SELECT `name`, `type`, `coefficient`, `rule`, `composition`, `time_start` " 
                        "FROM `schedule` INNER JOIN `event` "
                        "ON `schedule`.`event_name_id` = `event`.`id` "
                        "WHERE `event`.`name_en` = '%s';"%(name_en))
        self.result = self.cur.fetchone()
        return self.result


    def get_users(self):
        self.reconnect()

        self.cur.execute("SELECT user_id FROM users;")
        self.result = self.cur.fetchall()
        return self.result

    
    def get_users_subs(self, user_id):
        self.reconnect()

        self.cur.execute("SELECT `team`.`name`, `event`.`name` FROM `subscriptions` "
                        "JOIN `team` ON `subscriptions`.`team_id` = `team`.`id` "
                        "JOIN `event` ON `subscriptions`.`event_id` = `event`.`id` "
                        "WHERE `subscriptions`.`user_id` = %s"%user_id)
        self.result = self.cur.fetchall()
        return self.result

    def get_team_subs(self, user_id):
        self.reconnect()

        self.cur.execute("SELECT `team`.`name` FROM `subscriptions` "
                        "JOIN `team` ON `subscriptions`.`team_id` = `team`.`id` "
                        "WHERE `subscriptions`.`user_id` = %s"%user_id)
        self.result = self.cur.fetchall()
        return self.result


    def get_event_subs(self, user_id):
        self.reconnect()

        self.cur.execute("SELECT `event`.`name` FROM `subscriptions` "
                        "JOIN `event` ON `subscriptions`.`event_id` = `event`.`id` "
                        "WHERE `subscriptions`.`user_id` = %s"%user_id)
        self.result = self.cur.fetchall()
        return self.result


    # Методы добавления данных
    def set_user(self,user_id):
        self.reconnect()

        self.cur.execute("INSERT INTO users (user_id, team_subs, event_subs) "
                        "VALUES (%s,NULL, NULL);"%(user_id))
        self.myconn.commit()


    # TODO: Проверить реализацию функции добавления подписки на команду
    def set_team_subs(self,user_id, team):
        self.reconnect()

        self.cur.execute("INSERT INTO `subscriptions` (user_id, team_id) VALUES "
                        "(%s,(SELECT id FROM team WHERE name=%s));"%(user_id, team))
        self.myconn.commit()

SQL = SQLighter()
"""
rq_li = ['by.Cord','Прокат']
SQL.set_team_subs(466138751,rq_li)
#SQL.set_team_subs(466138751,'Прокат')
rq = SQL.get_team_subs(466138751)
print(list(rq))"""