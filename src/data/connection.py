from django.db import connection

class DB(object):
    """ Clase para obtener instancia de base de datos """
    
    def get_connection(self):
        try:
            c = connection.cursor()
            c.execute('SELECT current_time')
            c.fetchone()
        except:
            connection.close()


    def get_close_connection(self):
        connection.close()
