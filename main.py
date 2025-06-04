<<<<<<< HEAD
#Registro de usuario (Adminitsrador o Publico)
=======
class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.rol = rol

    def ver_datos(self):
        return f"Id_Usuario: {self.id_usuario}, Nombre: {self.nombre}, Email: {self.email}, Contraseña: {self.contraseña}, Rol: {self.rol}"
    
class Sistema_De_Usuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, id_usuario, nombre, email, contraseña, rol):
         if id_usuario == 0 or nombre == "" or email == "" or contraseña == "" or rol == "":
            return "ERROR!! Hay algunos campos vacios y/o nulos."
         
         if contraseña != "" and len(contraseña) < 6:
            return "INVALIDA!! La contraseña debe contener como mínimo 6 caracteres."
        
         nuevo_usuario = Usuario(id_usuario, nombre, email, contraseña, rol)
         self.usuarios.append(nuevo_usuario)
         return "EXCELENTE!! Usuario registrado."
        
    def iniciar_sesion(self, email, contraseña):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.contraseña == contraseña:
                print(f"Inicio de sesión exitoso!! Bienvenido {usuario.nombre}")
                return usuario
            
        else:
            return "ERROR!! Contraseña u email incorrectos."
        
    def mostrar_usuarios(self):
        if self.usuarios == []:
            return "No se ha registrado ningun usuario."
        
        else:
            print("---------- Listado de Usuarios ----------")
            for usuario in self.usuarios:
                print(usuario.ver_datos())

    def cambiar_rol(self, id_usuario, nuevo_rol):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
               usuario.rol = nuevo_rol
               print(f"{nuevo_rol} es el nuevo rol del usuario {id_usuario}")

        else:
            print("ERROR!! Usuario no registrado")
        
    def eliminar_usuario(self, id_usuario):
        for x, usuario in enumerate(self.usuarios):
            if usuario.id_usuario == id_usuario:
               eliminado = self.usuarios.pop(x)
               return f"Se elimino al Usuario: {eliminado} con Id_usuario: {usuario.id_usuario}."

        else:
            return f"El Id_usuario: {id_usuario} no se encuentra registrado."
        
    def menu_interno(self, usuario):
        while True:
            print("---------- Seleccione su Rol ----------")
            if usuario.rol == "Estandar":
                print("1. Ver Informacion Persoal.")
                print("2. Salir del Menu.")
                opcion = input("Seleccione una de las opciones: ")

                if opcion == "1":
                    print(usuario.ver_datos())

                elif opcion == "2":
                    print("Usted salio del Menu.")
                    break

            elif usuario.rol == "Administrador":
                print("1. Ver Informacion Personal.")
                print("2. Ver el Listado de Usuarios Registrados: ")
                print("3. Cambiar el rol a un usuario.")
                print("4. Eliminar a un usuario.")
                print("5. Salir del Menu.")
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    print(usuario.ver_datos())

                elif opcion == "2":
                    self.mostrar_usuarios()

                elif opcion == "3":
                    id_usuario = int(input("Ingrese el Id del usuario a buscar: "))
                    nuevo_rol = input("Ingrese el rol que le desea asiganr al usuario: ")
                    self.cambiar_rol(id_usuario, nuevo_rol)

                elif opcion == "4":
                    id_usuario = int(input("Ingrese el Id del usuario a eliminar: "))
                    self.eliminar_usuario(id_usuario)

                elif opcion == "5":
                    print("Usted Salio del Menu.")
                    break

                else:
                    return "ERROR!! Usted ingreso una opcion no valida."


sistema = Sistema_De_Usuarios()

def menu_principal():
    while True:
        print("----------- MENU PRINCIPAL ----------")
        print("1. Registrar Usuario.")
        print("2. Iniciar Sesion.")
        print("3. Salir del Menu Principal.")
        opcion = input("Seleccione una de las opciones: ")

        if opcion == "1":
            ingresar_id_usuario = int(input("Ingrese su Id_Usuario: "))
            ingresar_nombre = input("Ingrese su Nombre: ")
            ingresar_email = input("Ingrese su email: ")
            ingresar_contraseña = input("Ingrese una contraseña: ")
            ingresar_rol = input("Ingrese su rol: ")
            print(sistema.registrar_usuario(ingresar_id_usuario, ingresar_nombre, ingresar_email, ingresar_contraseña, ingresar_rol))

        elif opcion == "2":
            ingresar_email = input("Ingrese su email: ")
            ingresar_contraseña = input("Ingrese una contraseña: ")
            usuario = sistema.iniciar_sesion(ingresar_email, ingresar_contraseña)
            if usuario:
               sistema.menu_interno(usuario)
            
        elif opcion == "3":
             print("¡Hasta luego!")
             break
            
        else:
                 print("Opción inválida.")

menu_principal()

#cambios
>>>>>>> feature/AgustinExequielGimenez
