Ejercicio: Talleres de autos 

Esquema de BD: TALLER< codigoSucursal, domicilioSucursal, telefonoSucursal, codigoFosa, anchoFosa, largoFosa, patenteAuto, marcaAuto, modeloAuto, dniCliente, nombreCliente, celularCliente, dniMecanico, nombreMecanico, emailMecanico > 

CÓDIGO TABLA TALLER ORIGINAL: 

Table "TALLER" { 

  "codigoSucursal" INT [not null] 

  "domicilioSucursal" VARCHAR 

  "telefonoSucursal" INT 

  "codigoFosa" INT [not null] 

  "anchoFosa" FLOAT 

  "largoFosa" FLOAT  

  "patenteAuto" VARCHAR [not null] 

  "marcaAuto" VARCHAR 

  "modeloAuto" VARCHAR 

  "dniCliente" INT [primary key] 

  "nombreCliente" VARCHAR 

  "celularCliente" INT 

  "dniMecanico" INT [not null] 

  "nombreMecanico" VARCHAR 

  "emailMecanico" VARCHAR 

} 

 

Paso 1: Determinar las Dependencias Funcionales (DFs) 

A partir del esquema y las restricciones dadas, podemos determinar las siguientes dependencias funcionales: 

codigoSucursal -> domicilioSucursal, telefonoSucursal: Cada sucursal puntual tiene un número de teléfono y un código propio que la identifica, por lo tanto domicilioSucursal y telefonoSucursal dependen funcionalmente de codigoSucursal.  

patenteAuto -> marcaAuto, modeloAuto, dniCliente: Cada auto tiene una marca, modelo y cliente. Un se registra con un único cliente, pero este último puede tener más de un auto. Por lo tanto marcaAuto, modeloAuto y dniCliente dependen funcionalmente de patenteAuto.  

codigoSucursal, codigoFosa -> anchoFosa, largoFosa: Las sucursales puede compratir el mismo código de fosa, pero ser fosas distintas, por lo tanto anchoFosa y largoFosa dependen funcionalmente de codigoSucursal y codigoFosa.  

 

Paso 2: Determinar las Claves Candidatas 

La combinación de codigoSucursal, codigoFosa, patenteAuto, dniCliente y dniMecanico es suficiente para identificar de forma única cada registro en la tabla, ya que: 

- CodigoSucursal identifica la sucursal. 

- CodigoFosa identifica la fosa de la sucursal. 

- PatenteAuto identifica el auto que se va a arreglar. 

- DniCliente identifica al cliente que lleva su auto. 

- DniMecanico identifica al mecánico que va a arreglar el auto del cliente. 

Por lo tanto, la clave candidata es: (codigoSucursal, codigoFosa, patenteAuto, dniCliente y dniMecanico). 

 

Paso 3: Diseño en Tercera Forma Normal (3FN) 

Para llevar el esquema a la Tercera Forma Normal (3FN), necesitamos eliminar dependencias transitivas y asegurarnos de que cada atributo no clave dependa únicamente de la clave primaria completa. Esto implica dividir la tabla en varias tablas relacionadas para reducir la redundancia y asegurar la integridad de los datos. 

La tabla original fue dividida en 6 tablas como se muestra a continuación, evitando redundancias y dando más consistencia a la base de datos:
Tabla Sucursal  

Tabla Sucursal
- codigoSucursal  (clave primaria). Justificación: el atributo codigoSucursal es único e identifica cada sucursal los demás atributos dependen funcionalmente de este.  
- domicilioSucursal 
- TelefonoSucursal 


Tabla Fosa 

- codigoSucursal (clave foránea que referencia a Sucursal) 
- codigoFosa 
- largoFosa 
- anchoFosa 
- clave primaria compuesta (codigoSucursal, codigoFosa) 


Tabla Auto 

- patenteAuto (clave primaria). Justificación: el atributo patenteAuto identifica de manera única cada auto y nos permite saber quién es su propietario (dniCliente).  
- marcaAuto 
- modeloAuto 
- dniCliente (clave foránea que referencia a Cliente) 

 

Tabla Cliente 

- dniCliente (clave primaria). Justificación: el atributo dniCliente identifica de manera unica a cada cliente del taller. 
- nombreCliente  
- celularCliente 
 

Tabla Mecanico 

- dniMecanico (clave primaria) Justificación: el atributo dniMecanico identifica de manera única a cada mecánico del taller. 
- nombreMecanico 
- emailMecanico 


Tabla Trabajo 

- codigoSucursal (clave foránea que referencia a Sucursal) 
- codigoFosa (clave foránea que referencia a Fosa) 
- patenteAuto (clave foránea que referencia a Auto) 
- dniMecanico (clave foránea que referencia a Mecánico) 
- Clave primaria compuesta (codigoSucursal, codigoFosa, patenteAuto, dniMecanico) 

Código tablas 3FN: 

Table Sucursal { 

codigoSucursal int [primary key]                                                                                                              domicilioSucursal varchar                                                          
telefonoSucursal varchar 

} 

Table Fosa { 

codigoSucursal int [ref: > Sucursal.codigoSucursal]                   
codigoFosa int                                                                                
largoFosa float                                                                                         
anchoFosa float                                                                                               
primary key (codigoSucursal, codigoFosa) 

} 

Table Auto { 

patenteAuto varchar [primary key]                                                              
marcaAuto varchar                                                                                     
modeloAuto varchar                                                                                               
dniCliente int [ref: > Cliente.dniCliente] 

} 

Table Cliente { 

dniCliente int [primary key]                                                                         
nombreCliente varchar                                                                   
celularCliente varchar 

}  

Table Mecanico { 

dniMecanico int [primary key]                                                                 
nombreMecanico varchar                                                                   
emailMecanico varchar 

} 

Table Trabajo { 

codigoSucursal int [ref: > Sucursal.codigoSucursal]                            
codigoFosa int [ref: > Fosa.codigoFosa]                                                
patenteAuto varchar [ref: > Auto.patenteAuto]                                            
dniMecanico int [ref: > Mecanico.dniMecanico]                                          
primary key (codigoSucursal, codigoFosa, patenteAuto, dniMecanico) 

} 