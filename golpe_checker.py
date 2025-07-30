def verificar_golpe(dados_pix):
    alertas = []

    nome = dados_pix.get('nome', '').lower()
    tipo = dados_pix.get('tipo_chave', '')
    valor = dados_pix.get('valor', '')
    
    if tipo == 'CPF' or "ltd" not in nome and "ltda" not in nome and "seguros" not in nome:
        alertas.append("⚠️ Nome do recebedor parece ser de pessoa física.")

    if not valor:
        alertas.append("⚠️ Valor do Pix não está definido.")

    if "s1platform" in dados_pix.get("origem_link", ""):
        alertas.append("🚨 Domínio suspeito detectado no link do pagamento.")

    if alertas:
        print("🛑 Possível golpe detectado:")
        for alerta in alertas:
            print(alerta)
    else:
        print("✅ Nenhum indício claro de golpe.")
