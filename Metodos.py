
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
class Metodos():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="", database='estudiantes')
        self.mycursor = self.mydb.cursor()


    def AgregrarEstudiante(self,id,name,apelli,iden,numide,fechaNac,sex):
        cur = self.mydb.cursor()
        sql0 = """SELECT `id` FROM estudiante WHERE `id` = '{}' OR `cedula` = '{}'""".format(id, numide)
        cur.execute(sql0)
        consul = cur.fetchall()
        print(consul)
        if not consul:
            sql = "INSERT INTO estudiante (id,nombre,apellido,identificacion,cedula,fechaNac,sexo) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(id,name,apelli,iden,numide,fechaNac,sex)
            cur.execute(sql)
            self.mydb.commit()
            confirmar = QtWidgets.QMessageBox()
            confirmar.setIcon(confirmar.Warning)
            confirmar.setText("Se agregó con exitó el usuario")
            confirmar.exec_()
        else:
            confirmar = QtWidgets.QMessageBox()
            confirmar.setIcon(confirmar.Warning)
            confirmar.setText("El estudiante ya está registrado")
            confirmar.exec_()

    def BuscarEstudiante(self):
        curso=self.mydb.cursor()
        sql="SELECT *from estudiante"
        curso.execute(sql)
        registro=curso.fetchall()
        return registro

    def FiltroEstudiante(self,filtro,parametro):
        curso = self.mydb.cursor()
        sql = "SELECT *from estudiante WHERE {}={}".format(filtro,parametro)
        curso.execute(sql)
        registroh = curso.fetchall()
        return registroh
    def Filtroid(self,ids):
        curso = self.mydb.cursor()
        sql = "SELECT *from estudiante WHERE id ={}".format(ids)

        curso.execute(sql)
        registroh = curso.fetchall()
        return registroh

    def EliminaEstudiante(self,filt,parametr):
        cur=self.mydb.cursor()
        sql="DELETE FROM estudiante WHERE {}={}".format(filt,parametr)

        cur.execute(sql)
        a = cur.rowcount
        self.mydb.commit()
        cur.close()
        return a

    def ActualizarEstudiante(self, name,apelli,iden,cedula,fechaNac,sex,id):
        cur = self.mydb.cursor()
        sql = '''UPDATE estudiante SET  nombre = '{}', apellido = '{}', identificacion = '{}',cedula='{}',fechaNac='{}',sexo='{}'
           WHERE id = '{}' '''.format(name,apelli,iden,cedula,fechaNac,sex,id)

        cur.execute(sql)
        a = cur.rowcount
        self.mydb.commit()
        cur.close()
        return a
    def ingresar(self,usuario,contas):
        curso = self.mydb.cursor()
        sql = "SELECT nombre,apellido,id from estudiante WHERE id ={} AND cedula= {}".format(usuario,contas)
        curso.execute(sql)
        registroh = curso.fetchall()
        print(registroh)
        if not registroh:
            print("Usuario invalidó")
        else:
            print(registroh[0][0])
        return registroh
    def AgregrarControl(self,idCon,jor,hor,feca,temp,idEst,idEncuesta):
        cur=self.mydb.cursor()
        sql = "INSERT INTO control (idControl,jornada,hora,fecha,temperatura,idEstudiante,idEncuesta) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(idCon,jor,hor,feca,temp,idEst,idEncuesta)
        cur.execute(sql)
        self.mydb.commit()
        cur.close()