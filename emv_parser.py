def extrair_dados_pix(codigo):
    dados = {}
    i = 0
    while i < len(codigo):
        try:
            id = codigo[i:i+2]
            tamanho = int(codigo[i+2:i+4])
            valor = codigo[i+4:i+4+tamanho]
            i += 4 + tamanho

            if id == '59':
                dados['nome'] = valor
            elif id == '60':
                dados['cidade'] = valor
            elif id == '01':
                dados['chave_pix'] = valor
            elif id == '52':
                dados['categoria'] = valor
            elif id == '53':
                dados['moeda'] = valor
            elif id == '54':
                dados['valor'] = valor
        except:
            break

    if 'chave_pix' in dados:
        if '@' in dados['chave_pix']:
            dados['tipo_chave'] = 'e-mail'
        elif len(dados['chave_pix']) == 11:
            dados['tipo_chave'] = 'CPF'
        elif len(dados['chave_pix']) == 14:
            dados['tipo_chave'] = 'CNPJ'
        else:
            dados['tipo_chave'] = 'Desconhecida'

    return dados
