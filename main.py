from base_datos.conexion import Conexion

base_datos="base_datos/usuarios.db"
conexion=Conexion(base_datos)
conexion.crear_tabla_usuario()
conexion.insertar_usuario(1223347,"Gio", "gvielza","consultand")
usuarios=conexion.mostrar_usuarios()
#Mostrar clientes
for fila in usuarios:
    print(fila)
#dni_eliminar=1223346
#conexion.eliminar_usuario(dni_eliminar)

#conexion.editar_usuario(1223347,"Geo","gvielza","programador")
conexion.cerrar_conexion()