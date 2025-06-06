class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña, rol): #Creación de una instancia para la clase usuario, utilizando el constructor "__init__". Datos que se deben proporcionar para crear el objeto
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email #Asignar el valor del parametro email al atributo email del objeto
        self.contraseña = contraseña
        self.rol = rol

    def ver_datos(self): #Definimos el metodo Ver_datos
        print("----------- INFORMACION PERSONAL ----------")
        return (
            f"Id_Usuario: {self.id_usuario}\n"
            f"Nombre: {self.nombre}\n" 
            f"Email: {self.email}\n" 
            f"Contraseña: {self.contraseña}\n"
            f"Rol: {self.rol}\n"
            )
    
class Sistema_De_Usuarios:
    def __init__(self):
        self.usuarios = [] #Creamos una lista para almacenar los usuarios

    def registrar_usuario(self, id_usuario, nombre, email, contraseña, rol): #Definimos el metodo para registrar un nuevo usuario
         if id_usuario <= 0 or nombre == "" or email == "" or contraseña == "" or rol == "":
            return "ERROR!! Hay algunos campos invalidos."
         
         if contraseña != "" and len(contraseña) < 6:
            return "INVALIDA!! La contraseña debe contener como mínimo 6 caracteres."
        
         nuevo_usuario = Usuario(id_usuario, nombre, email, contraseña, rol) #Si las validaciones son correctas, crea unanueva instancia de usuario usando los datos proporcionados
         self.usuarios.append(nuevo_usuario) #Agrega el nuevo usuario a la lista de usuarios regsitrados
         return "EXCELENTE!! Usuario registrado."
        
    def iniciar_sesion(self, email, contraseña):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.contraseña == contraseña: #Verifica si el email y la contraseña coinciden con los de un usuario registrado
                print("--------------------------")
                print(f"Inicio de sesión exitoso!! Bienvenido {usuario.nombre}")
                return usuario
            
        print("ERROR!! Contraseña u email incorrectos.")
        
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


sistema = Sistema_De_Usuarios()

def menu_principal():
    while True:
        print("----------- MENU PRINCIPAL ----------")
        print("[1] Registrar Usuario.") 
        print("[2] Iniciar Sesion.")
        print("[3] Salir del Menu Principal.")
        opcion = input("Seleccione una de las opciones: ")

        match opcion:
            case "1":
                 ingresar_id_usuario = int(input("Ingrese su Id_Usuario: "))
                 ingresar_nombre = input("Ingrese su Nombre: ")
                 ingresar_email = input("Ingrese su email: ")
                 ingresar_contraseña = input("Ingrese una contraseña: ")
                 ingresar_rol = input("Ingrese su rol: ")
                 print(sistema.registrar_usuario(ingresar_id_usuario, ingresar_nombre, ingresar_email, ingresar_contraseña, ingresar_rol)) #llama al metodo registrar_usuario del objeto sistema para intentar crear el usuario con los datos ingresados

            case "2":
                 ingresar_email = input("Ingrese su email: ")
                 ingresar_contraseña = input("Ingrese una contraseña: ")
                 usuario = sistema.iniciar_sesion(ingresar_email, ingresar_contraseña)
                 if usuario:
                    sistema.menu_interno(usuario)
            
            case "3":
                 print("Usted Salio del Menu Prinicipal.")
                 break
            
            case _:
                print("ERROR!! Usted ingreso una opcion no valida.")

menu_principal()


#Implementar condicion para que solo acepte los roles (Administrador o Estandar)
#Implemnetar condicion para que no se pueda iniciar sesion sin completar los campos (campos vacios)
#Implementar condicion para que dos usuarios no posean el mismo id_usuario.






