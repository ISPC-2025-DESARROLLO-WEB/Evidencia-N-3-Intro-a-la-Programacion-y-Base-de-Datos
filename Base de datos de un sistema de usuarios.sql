CREATE DATABASE IF NOT EXISTS sistema_usuarios;
USE sistema_usuarios;

-- 1. Crear la tabla Rol primero
CREATE TABLE Rol (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(20) UNIQUE
);
-- 2. Insertar los roles
INSERT INTO Rol (nombre_rol) VALUES ('administrador'), ('estandar');
 
 -- 3. Crear la tabla Usuario, que referencia a Rol
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    contraseña VARCHAR(100),
	id_rol INT,
    FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);

-- Crud de Usuario-------

-- CREATE (insertar usuario)
INSERT INTO Usuario (nombre, email, contraseña, id_rol) VALUES
('Pablo Romero', 'pablolihuenromero@gmail.com', 'ej_contraseña123', 1),
('Ezequiel Gimenez', 'exequielgimenez@gmail.com', 'ej_contraseña321', 2),
('Franco Gimenez', 'francogimenez@gmail.com', 'ej_contraseña432', 1),
('Guadalupe Turri', 'guadalupeturri@gmail.com', 'ej_contraseña543', 2),
('Ivana Salinas', 'ivanasalinas@gmail.com', 'ej_contraseña654', 1),
('Claudia Mansilla', 'claudiamansilla@gmail.com', 'ej_contraseña765', 2);

-- READ (consultar usuarios)
SELECT * FROM Usuario;

-- Ver uno por id:
SELECT * FROM Usuario WHERE id_usuario = 1;

-- UPDATE (actualizar datos)
-- Ejemplo: cambiar el rol del usuario con id 1
UPDATE Usuario
SET id_rol = 2
WHERE id_usuario = 1;

-- Ejemplo: cambiar contraseña del usuario con id 1
UPDATE Usuario
SET contraseña = 'nueva_contraseña123'
WHERE id_usuario = 1;

-- DELETE (eliminar usuario)
DELETE FROM Usuario WHERE id_usuario = 1;
