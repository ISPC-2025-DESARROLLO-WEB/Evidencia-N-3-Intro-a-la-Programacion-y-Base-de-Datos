from modulo_usuario import Usuario

class Sistema_De_Usuarios:
    def __init__(self):
        self.usuarios = [] #Creamos una lista para almacenar los usuarios

    def registrar_usuario(self, id_usuario, nombre, email, contraseña, rol): #Definimos el metodo para registrar un nuevo usuario
         if id_usuario <= 0 or nombre == "" or email == "" or contraseña == "" or rol == "":
            return "ERROR!! Hay algunos campos invalidos."
         
         if rol != "Administrador" and rol != "Estandar":
             return "Rol no reconocido"
         
         if contraseña != "" and len(contraseña) < 6:
            return "INVALIDA!! La contraseña debe contener como mínimo 6 caracteres."
         
         for usuario in self.usuarios:
             if usuario.id_usuario == id_usuario:
                 return "ERROR!! Ya existe un usuario con ese ID."
             
         for usuario in self.usuarios:
             if usuario.email == email:
                 return "ERROR!! Ya existe un usuario registrado con ese email."
        
         nuevo_usuario = Usuario(id_usuario, nombre, email, contraseña, rol) #Si las validaciones son correctas, crea unanueva instancia de usuario usando los datos proporcionados
         self.usuarios.append(nuevo_usuario) #Agrega el nuevo usuario a la lista de usuarios regsitrados
         return "EXCELENTE!! Usuario registrado."
        
    def iniciar_sesion(self, email, contraseña):
        if email == "" or contraseña == "":
            print("No se puede Iniciar Sesion. Campos Incompletos")
            return None
        
        for usuario in self.usuarios:
            if usuario.email == email and usuario.contraseña == contraseña: #Verifica si el email y la contraseña coinciden con los de un usuario registrado
                print("--------------------------")
                print(f"Inicio de sesión exitoso!! Bienvenido {usuario.nombre}")
                return usuario
            
            print("ERROR!! Contraseña u email incorrecto.")    
            return None
        
    def mostrar_usuarios(self):
        if self.usuarios == []:
            print("No se ha registrado ningun usuario.")
        
        else:
            print("---------- Listado de Usuarios ----------")
            for usuario in self.usuarios:
                print(usuario.ver_datos()) #Imprime los datos del usuario, utilizando el metodo ver_datos()

    def cambiar_rol(self, id_usuario, nuevo_rol):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario: #Compara el id_usuario actual con el id_usuario proporcionado
               usuario.rol = nuevo_rol #Cambia el atributo Rol del usuario por el nuevo valor
               print(f"{nuevo_rol} es el nuevo rol del usuario {usuario.nombre} con numero de ID: {id_usuario}")
               return
        print("ERROR!! Usuario no registrado")
        
    def eliminar_usuario(self, id_usuario):
        for x, usuario in enumerate(self.usuarios):
            if usuario.id_usuario == id_usuario:
               eliminado = self.usuarios.pop(x)
               print (f"Se elimino al Usuario: {eliminado.nombre} con numero de ID: {usuario.id_usuario}.")
               return

        else:
            print (f"El Id_usuario: {id_usuario} no se encuentra registrado.")
    
     
    def menu_interno(self, usuario):
        while True:
            print("---------- MENU PRINCIPAL ----------")
            if usuario.rol == "Estandar":
                print("[1] Ver Informacion Persoal.")
                print("[2] Salir del Menu.")
                opcion = input("Seleccione una de las opciones: ")

                match opcion:
                    case "1":
                         print(usuario.ver_datos())

                    case "2":
                         print("Usted salio del Menu.")
                         break
                    
                    case _:
                        print("ERROR!! Usted ingreso una opcion no valida.")

            elif usuario.rol == "Administrador":
                print("[1] Ver Informacion Personal.")
                print("[2] Ver el Listado de Usuarios Registrados: ")
                print("[3] Cambiar el rol a un usuario.")
                print("[4] Eliminar a un usuario.")
                print("[5] Salir del Menu.")
                opcion = input("Seleccione una opción: ")

                match opcion:
                    case "1":
                         print(usuario.ver_datos())

                    case "2":
                         self.mostrar_usuarios()

                    case "3":
                         id_usuario = int(input("Ingrese el Id del usuario a buscar: "))
                         nuevo_rol = input("Ingrese el rol que le desea asiganr al usuario: ")
                         self.cambiar_rol(id_usuario, nuevo_rol)

                    case "4":
                         id_usuario = int(input("Ingrese el Id del usuario a eliminar: "))
                         self.eliminar_usuario(id_usuario)
 
                    case "5":
                         print("Usted Salio del Menu.")
                         break

                    case _:
                         print("ERROR!! Usted ingreso una opcion no valida.")