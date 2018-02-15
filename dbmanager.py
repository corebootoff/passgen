import sqlite3

class DBManager(object):
    __instance = None

    def __init__(self, db_name):
        raise NotImplementedError
        #self._connection = sqlite3.connect(db_name)

    @classmethod
    def get_instance(cls, db_name):
        if not cls.__instance:
            cls.__instance = cls.__new__(cls )
            cls._connection = sqlite3.connect(db_name)

        return cls.__instance

    def _get_cursor(self):
        return sqlite3.Cursor(self._connection)

    def create(self, name, *columns):
        cursor = self._get_cursor()
        raw_sql = 'CREATE TABLE {name} ({colums})'
        colums_str = ', '.join(columns)
        sql = raw_sql.format(name=name, colums=colums_str)
        cursor.execute(sql)

    def insert(self, table, **values):
        cursor = self._get_cursor()
        raw_sql = 'INSERT INTO {table} ({names}) VALUES ({values})'
        names_str = ', '.join(values.keys())

        values_lst = [
            '%s' % value if isinstance(value, int)
            else '"%s"' % value
            for value in values.values()
        ]
        values_str = ', '.join(values_lst)
        sql = raw_sql.format(table=table, names=names_str, values=values_str)

        if not values:
            sql = 'INSERT INTO %s (id) VALUES (NULL)' % table
        cursor.execute(sql)
    def update(self, table, *condition, **values):
        pass

    def delete(self, table, *condition):
        pass

    def all(self, table):
        pass

    def search(self, table, column, name):
        cursor = self._get_cursor()
        sql = 'SELECT * FROM {table} WHERE {column} = {name}'.format(table=table, column=column, name=name)
        collection = cursor.execute(sql)
        return collection.fetchall()

    def commit(self):
        self._connection.commit()
        self._connection.close()

    def cancel(self):
        self._connection.rollback()
        self._connection.close()