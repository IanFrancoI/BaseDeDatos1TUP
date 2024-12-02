CREATE DATABASE IF NOT EXISTS BDbiblioteca2;
USE BDbiblioteca2;

CREATE TABLE Usuarios (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Direccion VARCHAR(200),
    Telefono VARCHAR(15) NOT NULL,
    FechaRegistro DATE NOT NULL,
    EstadoCuota ENUM('Paga', 'Impago') DEFAULT 'Impago',
    INDEX idx_nombre (Nombre)
);

CREATE TABLE Libros (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Titulo VARCHAR(200) NOT NULL,
    Autor VARCHAR(100) NOT NULL,
    Anio INT NOT NULL,
    Categoria VARCHAR(50),
    Estado ENUM('Disponible', 'No disponible') DEFAULT 'Disponible',
    INDEX idx_titulo (Titulo)
);

CREATE TABLE Prestamos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    UsuarioId INT,
    LibroId INT,
    FechaPrestamo DATE NOT NULL,
    FechaDevolucion DATE,
    Multa DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (UsuarioId) REFERENCES Usuarios(Id) ON DELETE CASCADE,
    FOREIGN KEY (LibroId) REFERENCES Libros(Id) ON DELETE CASCADE
);

CREATE TABLE Pagos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    UsuarioId INT,
    FechaPago DATE NOT NULL,
    Monto DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (UsuarioId) REFERENCES Usuarios(Id) ON DELETE CASCADE
);

INSERT INTO Usuarios (Nombre, Direccion, Telefono, FechaRegistro, EstadoCuota)
VALUES
('Juan Perez', 'Calle Falsa 123', '123456789', '2023-01-15', 'Paga'),
('María López', 'Av. Siempreviva 742', '987654321', '2023-02-20', 'Impago'),
('Carlos García', 'Av. Mitre 456', '112233445', '2022-12-10', 'Paga'),
('Ana González', 'Calle San Martín 987', '998877665', '2023-03-01', 'Impago'),
('Laura Fernández', 'Bv. Rivadavia 678', '123412341', '2022-09-15', 'Paga'),
('Roberto Sánchez', 'Pasaje Mitre 55', '987654320', '2023-04-20', 'Paga'),
('Sofía Morales', 'Calle Independencia 222', '876543210', '2022-08-05', 'Paga'),
('Martín Romero', 'Av. Belgrano 789', '223344556', '2023-01-25', 'Paga'),
('Gabriela Vázquez', 'Calle Los Aromos 333', '554433221', '2022-11-11', 'Paga'),
('Andrés Castillo', 'Bv. Urquiza 444', '667788990', '2023-05-01', 'Impago');


INSERT INTO Libros (Titulo, Autor, Anio, Categoria, Estado)
VALUES
('Cien Años de Soledad', 'Gabriel García Márquez', 1967, 'Novela', 'Disponible'),
('El Principito', 'Antoine de Saint-Exupéry', 1943, 'Infantil', 'Disponible'),
('1984', 'George Orwell', 1949, 'Distopía', 'Disponible'),
('Orgullo y Prejuicio', 'Jane Austen', 1813, 'Romance', 'Disponible'),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, 'Clásico', 'Disponible'),
('Crónica de una Muerte Anunciada', 'Gabriel García Márquez', 1981, 'Novela', 'Disponible'),
('Harry Potter y la Piedra Filosofal', 'J.K. Rowling', 1997, 'Fantasía', 'Disponible'),
('El Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasía', 'Disponible'),
('La Metamorfosis', 'Franz Kafka', 1915, 'Novela', 'Disponible'),
('Rayuela', 'Julio Cortázar', 1963, 'Experimental', 'Disponible');

INSERT INTO Prestamos (UsuarioId, LibroId, FechaPrestamo, FechaDevolucion, Multa)
VALUES
(1, 1, '2023-05-01', '2023-05-15', 0), 
(2, 2, '2023-04-25', '2023-05-10', 0), 
(3, 3, '2023-05-05', '2023-05-20', 5.00), 
(8, 4, '2023-04-15', '2023-05-15', 0), 
(5, 5, '2023-05-02', '2023-05-16', 0), 
(6, 6, '2023-04-28', '2023-06-02', 10.00); 

INSERT INTO Pagos (UsuarioId, FechaPago, Monto)
VALUES
(1, '2023-06-01', 60), 
(3, '2023-06-10', 65), 
(5, '2023-07-15', 60), 
(7, '2023-07-20', 60), 
(9, '2023-08-05', 60),   
(6, '2023-07-25', 70), 
(8, '2023-08-10', 60); 