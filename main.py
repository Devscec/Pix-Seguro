from qr_decoder import ler_qr_code
from emv_parser import extrair_dados_pix
from golpe_checker import verificar_golpe

print("🔎 Pix Seguro – Validador de QR Code Pix\n")


caminho_img = input("Digite o caminho da imagem do QR Code: ")


conteudo_pix = ler_qr_code(caminho_img)
print(f"\n📋 Conteúdo do Pix:\n{conteudo_pix}")


dados = extrair_dados_pix(conteudo_pix)

print("\n📌 Dados extraídos:")
for chave, valor in dados.items():
    print(f"- {chave}: {valor}")


print("\n🚨 Análise de golpe:")
verificar_golpe(dados)
