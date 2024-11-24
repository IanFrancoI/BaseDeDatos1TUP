CREATE TABLE Pedidos (
    PedidoId INT PRIMARY KEY auto_increment,
    ClienteId INT NOT NULL,
    FechaPedido DATE NOT NULL,
    TotalPedido DECIMAL(10,2) NOT NULL,
    Facturado BIT DEFAULT 0
);

CREATE TABLE Facturas (
    FacturaId INT PRIMARY KEY auto_increment,
    PedidoId INT,
    FechaFactura DATE NOT NULL,
    MontoFacturado DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (PedidoId) REFERENCES Pedidos(PedidoId)
);