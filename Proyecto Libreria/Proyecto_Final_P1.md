Proyecto 1: Sistema de Gestión de Biblioteca:
1.	codigoSQL.sql: Contiene el código SQL necesario para crear las tablas y realizar la carga de datos iniciales.
2.	conexion.py: Archivo Python para manejar la conexión con la base de datos.
3.	Carpeta entidades: Incluye archivos relacionados con la lógica de las entidades del sistema, contiene libro.py, pago.py, préstamo.py, usuario.py.
4.	menu.py: Código de Python que implementa el menú interactivo de la CLI.
5.	tablasDBdiagram.io.png: Imagen que representa el esquema de las tablas de la base de datos.
6.	TablasDBdiagram.io.txt: Descripción textual del esquema de tablas con dbdiagram.com.

1. Archivo codigoSQL.sql
Este archivo contiene:
•	Creación de la Base de Datos: Define la base BDbiblioteca y sus tablas principales: Usuarios, Libros, Préstamos, y Pagos.
•	Esquema Normalizado: Las tablas están normalizadas al menos hasta la 3NF, eliminando redundancias y asegurando la integridad de los datos.
•	Restricciones de Integridad: Se definen llaves primarias (Id) y restricciones como NOT NULL y valores predeterminados (por ejemplo, EstadoCuota para los usuarios).
•	Estructura Relacional: Las tablas están diseñadas con relaciones adecuadas para reflejar los casos de uso del sistema, como la conexión entre Usuarios y Préstamos.
•	Compatibilidad con Operaciones Avanzadas: Proporciona una base para implementar operaciones con JOIN, índices, y procedimientos almacenados necesarios.

2. Archivo menu.py
Implementa el menú CLI, ofreciendo una interfaz interactiva que permite:
•	Gestión de Usuarios: Agregar, ver, actualizar y eliminar usuarios.
•	Gestión de Libros: Registrar, editar y eliminar libros.
•	Manejo de Préstamos: Incluye opciones para calcular multas por retrasos.
•	Reporte de Morosos: Lista usuarios con cuotas pendientes, utilizando datos de la base de datos.
•	Modificación de Cuotas: Ajusta el valor de las cuotas mensuales según las necesidades.


3. Archivo conexion.py
Este archivo gestiona la conexión con la base de datos MySQL mediante mysql.connector.
•	Módulo Centralizado: Facilita la reutilización de la lógica de conexión en todos los módulos del proyecto.
•	Operaciones Robustas: Incluye métodos para conectar y desconectar la base de datos, asegurando un manejo adecuado de recursos.

Este diseño permite una interacción entre Python y la base de datos, cumpliendo con los requisitos de integración.


4. Archivo tablasDBdiagram.io.png
La imagen del diseño de la base de datos proporciona:
•	Esquema Visual: Representa las entidades principales, sus relaciones, y las cardinalidades, facilitando la comprensión del modelo.
•	Soporte para Desarrollo: Permite verificar que el diseño cumple con los principios de normalización y las relaciones necesarias para las operaciones exigidas.

5. Carpeta entidades
Contiene módulos para manejar las entidades clave del sistema (Libro, Usuario, Préstamo, Pago).

**Dependencias Funcionales (DFs)**
1.	Usuarios:
>	Id → (Nombre, Dirección, Teléfono, FechaRegistro, EstadoCuota)

2.	Libros:
>	Id → (Título, Autor, Año, Categoría)

3.	Préstamos:
>	(IdUsuario, IdLibro) → (FechaPréstamo, FechaDevolución, Multa)

4.	Pagos:
>	IdPago → (IdUsuario, FechaPago, Monto)

Estas dependencias aseguran que cada atributo depende completamente de la clave principal.

**Claves Candidatas**
•	Usuarios: Id (única).
•	Libros: Id (única).
•	Préstamos: Compuesta por (IdUsuario, IdLibro).
•	Pagos: IdPago.
Las claves candidatas estan seleccionadas para evitar redundancias y cumplir las dependencias funcionales mínimas.

**Normalización hasta 3NF**
1.	1NF (Forma Normal 1):
-	Cada tabla tiene atributos atómicos.
-	No hay valores repetidos ni grupos de atributos.

2.	2NF (Forma Normal 2):
-	Cada atributo no clave depende completamente de la clave principal.
-	Las tablas con claves compuestas eliminan dependencias parciales.

3.	3NF (Forma Normal 3):
-	Los atributos no clave son independientes entre sí.
-	Ejemplo: En la tabla Usuarios, EstadoCuota depende únicamente de Id.

Resultado: El diseño elimina redundancias y garantiza integridad de datos.

**Funcionamiento del Proyecto**
1.	Menú CLI Interactivo:
>	Gestión de usuarios y libros.
>	Manejo de préstamos (con cálculo de multas).
>	Modificación de cuotas.
>	Reportes (morosos y filtrados).
2.	Base de Datos:
>	Relaciona las entidades Usuarios, Libros, Préstamos y Pagos para consultas avanzadas.
>	Incluye restricciones como FOREIGN KEY, índices, y operaciones en cascada (ON DELETE y ON UPDATE).
3.	Cálculos Automatizados:
>	Multas calculadas dinámicamente (3% de la cuota mensual por día de retraso).
4.	Conexión Python-MySQL:
>	Gestión robusta mediante mysql.connector (conexión, desconexión y consultas).

**Manejo de Archivos**
1.	codigoSQL.sql:
o	Define el esquema y carga inicial.
2.	menu.py y conexion.py:
o	Implementan el funcionamiento interactivo del proyecto.
3.	Carpeta entidades:
o	Organización modular para manejar lógica específica de cada entidad.
4.	Esquema Visual (tablasDBdiagram.io.png):
o	Soporte gráfico del diseño.


Conclusión
1  Diseño y normalización del modelo de base de datos.
2 Integración funcional entre Python y MySQL.
3 Implementación completa del menú CLI con las operaciones requeridas.
4 Generación de documentación visual para el esquema de tablas.
