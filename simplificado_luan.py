
# definimos o dicionário (base de dados)
preco_frutas ={
    'maçã':2.5,
    'banana':1.8,
    'laranja':3.0
}

# Definimos qual fruta queremos procurar 
fruta_desejada = 'maçã'

# Fazemos a busca direta usando o método .get()
# O .get () tenta encontrar uma fruta; se não achar, mostra 'Fruta não encontrada'
resultado = preco_frutas.get(fruta_desejada,'Fruta não')

#Exibimos o resultado
print(f"o preço da{fruta_desejada}é R${resultado}")