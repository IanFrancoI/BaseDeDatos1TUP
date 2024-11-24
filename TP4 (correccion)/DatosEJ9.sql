INSERT INTO Pedidos (ClienteId, FechaPedido, TotalPedido, Facturado)
VALUES
(101, '2024-10-01', 250.75, 1),
(102, '2024-10-02', 100.00, 0),
(103, '2024-10-03', 75.50, 1),
(104, '2024-10-03', 450.00, 1);

INSERT INTO Facturas (PedidoId, FechaFactura, MontoFacturado)
VALUES
(1, '2024-10-02', 250.75),
(3, '2024-10-04', 75.50),
(4, '2024-10-05', 450.00);