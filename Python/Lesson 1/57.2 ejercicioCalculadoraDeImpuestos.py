pago_sin_impuesto = float(input('Ingrese el total antes de impuestos: $'))
iva = float(input('Ingrese el porcentaje de impuesto agregado: %'))

def calcular_total (iva, pago_sin_impuesto):
    iva = ((iva * pago_sin_impuesto) /100 )
    precio_total = (pago_sin_impuesto + iva)
    print(f'Total por iva: {iva}')
    print(f'Total a pagar despues de impuestos:$ {precio_total}')
calcular_total(iva, pago_sin_impuesto)

    

