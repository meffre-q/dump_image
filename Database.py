from sqlalchemy import create_engine

class Database:
    def __init__(self, user, password, host, port, database):
        eng = create_engine('mysql://{user}:{password}@{host}:{port}/{database}'.format(user=user, password=password, host=host, port=port, database=database))
        try:
            self.con = eng.connect()
        except:
            print ('Connection to database failed.')
            raise
        print ('Connection to database success.')

    def get_link(self, table, column):
        query = """SELECT {} FROM {};""".format(column, table)
        data = self.con.execute(query)
        for link in data.fetchall():
            yield link[0]
