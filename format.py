import locale
locale.setlocale(locale.LC_ALL, "pt_BR")

linha1 = 'Lista de Produtos', 'QTD Entradas', 'QTD Saídas', 'Saldo Estoque', 'Preço Unitário', 'Subtotal'
linha2 = 'Azeite de Oliva - Extra Virgem LAT 500ml', 100, 40, 60, 21.90, 1314.00
linha3 = 'Castanha do Pará - Granel(Gr)', 100, 5, 95, 6.00, 300.0
linha4 = 'Flocos de Aveia CXA', 1000, 200, 800, 10.90, 872.00
linha5 = 'Paçoca de Amendoim - CXA', 100, 8, 92, 1.50, 30.00
linha6 = 'Panetone sem Gluten - CXA 1 Und', 100, 60, 40, 17.30, 692.00
linha7 = 'Pão Sírio Integral - Saco 500g', 100, 70, 30, 5.90, 177.00
linha8 = 'Polpa de Açai Natural PCT 5L', 100, 1, 99, 7.10, 693.00
linha9 = 'Queijo Vegano', 100, 30, 70, 25.00, 1750.00
linha10 = '','','','','TOTAL',5774.00

linhas = linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9

def printlinha():
    print('+'+'-'*20+'+'+'-'*20+'+'+'-'*20 +
          '+'+'-'*20+'+'+'-'*20+'+'+'-'*20+'+')

def printconteudo(a, b, c, d, e, f):
    print('|{:20}|{:>20}|{:>20}|{:>20}|{:>20}|{:>20}|'.format(a[0:20] if len(a)>20 else '', '', '', '', '', ''))
    print('|{:20}|{:>20}|{:>20}|{:>20}|{:>20}|{:>20}|'.format(a[20:40] if len(a)>20 else a, b, c, d, locale.format_string("%.2f", e, grouping=True, monetary=True), locale.format_string("%.2f", f, grouping=True, monetary=True)))
    print('|{:20}|{:>20}|{:>20}|{:>20}|{:>20}|{:>20}|'.format(a[40:60] if len(a)>40 else '', '', '', '', '', ''))

a, b, c, d, e, f = linha1
printlinha()
print('|{:20}|{:>20}|{:>20}|{:>20}|{:>20}|{:>20}|'.format(a, b, c, d, e, f))
printlinha()
for linha in linhas:
    a, b, c, d, e, f = linha
    printconteudo(a, b, c, d, e, f)
    printlinha()
a, b, c, d, e, f = linha10
print('|{:20}|{:>20}|{:>20}|{:>20}|{:>20}|{:>20}|'.format(a, b, c, d, e, locale.format_string("%.2f", f, grouping=True, monetary=True)))
printlinha()