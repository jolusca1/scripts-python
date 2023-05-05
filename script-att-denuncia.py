import xlwings as xw
import pandas as pd

sheet = xw.Book('tb_denuncia - Copia.xls').sheets[0]
sheet2 = xw.Book('sitac_relatorios_relatorio_generico_02-05-2023-09_16_59.xls').sheets[0]

var = sheet.range("A2:K2536").value
var2 = sheet2.range("A2:K172").value
b = []
for i in var2:
    for k in var:
        if i[0] == k[0]:
            continue
    if i[0] != k[0]:
        b.append(k[0])

print(b)