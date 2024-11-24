DELIMITER //

CREATE PROCEDURE GenerarFacturas()
BEGIN
    START TRANSACTION;

    INSERT INTO Facturas (PedidoId, FechaFactura, MontoFacturado)
    SELECT PedidoId, ClienteId, CURDATE(), TotalPedido
    FROM Pedidos
    WHERE Facturado = 0;

    UPDATE Pedidos
    SET Facturado = 1
    WHERE PedidoId IN (SELECT PedidoId FROM Facturas WHERE FechaFactura = CURDATE());

    COMMIT;
END //

DELIMITER ;