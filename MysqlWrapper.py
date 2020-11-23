import mysql.connector

class MySQLWrapper:

    def connectDB(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
        return mydb

    def __init__(self, host, user, passwd, database):
        super().__init__()
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def login(self, user):
        status = False
        mydb = self.connectDB()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `user` WHERE username='{}' AND password='{}'".format(user['username'], user['password']))
        myresult = mycursor.fetchall()
        result = {}
        if len(myresult):
            result = {
                'id': myresult[0][0],
                'username': myresult[0][1],
                'password': myresult[0][2],
                'admin': True if myresult[0][2] == '1' else False
            }
            status = True
        return result, status
    
    def register(self, user):
        mydb = self.connectDB()
        mycursor = mydb.cursor()

        sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
        val = (user['username'], user['password'])
        mycursor.execute(sql, val)

        mydb.commit()
        return mycursor.lastrowid


