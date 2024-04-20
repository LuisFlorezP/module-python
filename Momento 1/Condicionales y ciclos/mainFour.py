codigo = '2045'
articulos_vendidos = 100 
valor_articulo = 4500
total_venta = articulos_vendidos * valor_articulo

descuento = total_venta * 0.1 if articulos_vendidos >= 50 else 0

print(f' - Código: {codigo}\n - Total venta: ${total_venta}\n - Descuento: ${descuento}')