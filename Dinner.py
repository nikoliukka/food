

class Dinner:

    def __init__(self, dbConnection):
        self.__dbConnection = dbConnection
        self.__create_table()

    def __create_table(self):
        cursor = self.__dbConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Dinner (Description TEXT, UNIQUE(Description));")
        self.__dbConnection.commit()

    def insert(self, description):
        cursor = self.__dbConnection.cursor()
        cursor.execute("INSERT OR IGNORE INTO Dinner VALUES (?);", (description,))
        self.__dbConnection.commit()

    def getRandom(self):
        cursor = self.__dbConnection.cursor()
        cursor.execute("SELECT * FROM Dinner WHERE rowid IN (SELECT rowid FROM Dinner ORDER BY RANDOM() LIMIT 1)")
        dinner = cursor.fetchone()
        return dinner[0]
