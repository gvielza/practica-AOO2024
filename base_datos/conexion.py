import sqlite3


class Conexion:
    def __init__(self, nombre_bd):
        self.nombre_bd=nombre_bd
        self.conexion=sqlite3.connect(nombre_bd)
        self.cursor=self.conexion.cursor()

    def crear_tabla_usuario(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(dni INT, nombre TEXT, usuario TEXT, rol TEXT)")
        self.conexion.commit()

    def insertar_usuario(self,dni,nombre,usuario, rol):
        self.cursor.execute("INSERT INTO usuarios VALUES(?,?,?,?)",(dni,nombre,usuario,rol))
        self.conexion.commit()

    def editar_usuario(self,dni,nombre,usuario,rol):
        self.cursor.execute("UPDATE usuarios SET dni=?, nombre=?,usuario=?, rol=? WHERE dni=?", (dni,nombre,usuario,rol,dni))
        self.conexion.commit()

    def mostrar_usuarios(self):
        self.cursor.execute("SELECT *FROM usuarios")
        usuarios=self.cursor.fetchall()
        return usuarios

    def eliminar_usuario(self,dni):
        self.cursor.execute("DELETE FROM usuarios WHERE dni=?",(dni,))  
        self.conexion.commit()
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()