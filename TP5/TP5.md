TP 5: NORMALIZACION 

1). Determinar las DFs: 

codigoSucursal -> domicilioSucursal, telefonoSucursal: Cada sucursal puntual tiene un número de teléfono y un código propio que la identifica, por lo tanto domicilioSucursal y telefonoSucursal dependen funcionalmente de codigoSucursal. 

patenteAuto -> marcaAuto, modeloAuto, dniCliente: Cada auto tiene una marca, modelo y cliente. Un se registra con un único cliente, pero este último puede tener más de un auto. Por lo tanto marcaAuto, modeloAuto y dniCliente dependen funcionalmente de patenteAuto. 

codigoSucursal, codigoFosa -> anchoFosa, largoFosa: Las sucursales puede compratir el mismo código de fosa, pero ser fosas distintas, por lo tanto anchoFosa y largoFosa dependen funcionalmente de codigoSucursal y codigoFosa. 

DniCliente -> nombreCliente, celularCliente:  

 

2). Determinar la/s clave/s candidata/s:  

La clave candidata que relaciona todas las tablas es: (codigoSucursal, codigoFosa, patenteAuto, dniCliente, dniMecanico)  