salario_base, horas_extras, bonificacion = input().split()

salario_base = float(salario_base)
horas_extras = float(horas_extras)
bonificacion = float(bonificacion)
valor_por_hora = salario_base / 192

valor_horas_extras=valor_por_hora*1.25

valor_total_hora_extra=horas_extras*valor_horas_extras

valor_bonificacion=0
if(bonificacion==1):
    valor_bonificacion=(salario_base*0.05)

salario_total=(salario_base+valor_total_hora_extra+valor_bonificacion)
salario_con_descuento=(salario_total*(1-0.085))
print(round(salario_con_descuento,1))