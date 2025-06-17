class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña, rol):
        
        self.__id_usuario = id_usuario  
        self.__nombre = nombre            
        self.__email = email              
        self.__contraseña = contraseña  
        self.__rol = rol                  

    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_contraseña(self):
        return self.__contraseña
    
    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña

    def get_rol(self):
        return self.__rol
    
    def set_rol(self, rol):
        self.__rol = rol
    
    def ver_datos(self):
        print("----------- INFORMACIÓN PERSONAL ----------")
        return (
            f"Id_Usuario: {self.get_id_usuario()}\n"
            f"Nombre: {self.get_nombre()}\n"
            f"Email: {self.get_email()}\n"
            f"Contraseña: {self.get_contraseña()}\n"
            f"Rol: {self.get_rol()}\n"
        )

   
    