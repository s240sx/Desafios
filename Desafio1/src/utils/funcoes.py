import os

def calcular_salarios(tipo, valor1, valor2=0):
    """Calcula os descontos e o salário líquido com base no tipo[cite: 79, 81]."""
    inss, irrf = 0.0, 0.0
    
    if tipo == 'clt':
        bruto = valor1 # valor1 é o salário fixo [cite: 26]
        inss = bruto * 0.08 # 8% de INSS [cite: 27]
        if bruto > 2000:
            irrf = bruto * 0.10 # 10% de IRRF se > 2000 [cite: 28]
            
    elif tipo == 'freelancer':
        bruto = valor1 * valor2 # horas * valor/hora [cite: 31]
        inss = bruto * 0.05 # Desconto fixo de 5% [cite: 32]
        
    else: # estagiario
        bruto = valor1 # salário fixo [cite: 22]
        # Sem descontos de INSS ou IRRF [cite: 23]
        
    liquido = bruto - inss - irrf
    return bruto, inss, irrf, liquido

def gerar_relatorio_texto(funcionarios):
    """Cria a string formatada do relatório[cite: 88, 89]."""
    if not funcionarios:
        return "Nenhum funcionário cadastrado."

    txt = "=== Relatório de Folha de Pagamento ===\n"
    total = 0
    for f in funcionarios:
        txt += f"Nome: {f['nome']}\nTipo: {f['tipo']}\n"
        txt += f"Salário Bruto: R$ {f['bruto']:.2f}\n"
        txt += f"Líquido: R$ {f['liquido']:.2f}\n"
        txt += "-" * 30 + "\n"
        total += f['liquido']
    txt += f"Total pago pela empresa: R$ {total:.2f}"
    return txt

def salvar_em_arquivo(conteudo):
    """Tenta salvar o relatório em um arquivo TXT[cite: 90, 91]."""
    try:
        with open("relatorio_folha.txt", "w", encoding="utf-8") as arq:
            arq.write(conteudo)
        print(f"Arquivo salvo com sucesso em: {os.getcwd()}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e} [cite: 76]")