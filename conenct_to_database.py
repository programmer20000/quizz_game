import mysql.connector
from config import *

class DB:
    def __init__(self) -> None:
        self.connect_to_database()

    def connect_to_database(self):
        try:
            self.connect = mysql.connector.connect(
                host=localhost,
                user=user,
                passwd=password,
                database=name_database
            )
            print("connect to database is successful")

            with self.connect.cursor() as cursor:
                select_all_from_database = "show tables;"
                cursor.execute(select_all_from_database)
                result = cursor.fetchall()
                print(result)

        except Exception as _ex:
            print("connect to database not successful")


    def add_dates(self,data):
        insert_in_database = f"""
        insert into Question(question) values("{data[0]}");
insert into Answers(answers,question_id) values("{data[1]}",(select question_id from Question where question ="{data[0]}"));
insert into Answers(answers,question_id) values("{data[2]}",(select question_id from Question where question ="{data[0]}"));
"""
        self.connect.cursor().execute(insert_in_database)