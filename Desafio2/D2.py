# Aluno: João Víttor (SI - 3º Período)
# Desafio: Sistema de Loja Simples

def cadastrar(produtos):
    try:
        nome = input("Nome do produto: ").strip()
        if not nome:
            return print("O nome não pode ser vazio.")
        
        # checa se o produto ja ta na lista
        for p in produtos:
            if p["nome"].lower() == nome.lower():
                return print("Esse produto já está cadastrado!")
        
        preco = float(input("Preço: R$ "))
        estoque = int(input("Estoque inicial: "))
        
        # validação basica de valores
        if preco <= 0 or estoque < 0:
            print("O preço tem que ser > 0 e estoque >= 0.")
        else:
            # joga o dict na lista
            produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
            print("Produto salvo!")
            
    except ValueError:
        print("Erro: digite apenas números no preço e estoque.")

def vender(produtos, vendas):
    if not produtos:
        return print("Sem produtos pra vender ainda.")
        
    cliente = input("\nNome do cliente: ").strip()
    if not cliente:
        return print("Tem que informar o nome do cliente.")
        
    print("\n--- Produtos ---")
    # lista usando o enumerate pra gerar os indices
    for i, p in enumerate(produtos):
        print(f"{i}. {p['nome']} - R$ {p['preco']:.2f} (Disp: {p['estoque']})")
        
    try:
        idx = int(input("Escolha pelo número: "))
        if idx < 0 or idx >= len(produtos):
            return print("Produto não achado.")
            
        prod = produtos[idx]
        qtd = int(input("Quantidade: "))
        
        if qtd <= 0 or qtd > prod["estoque"]:
            return print("Quantidade inválida ou maior que o estoque.")
            
        # da baixa no estoque
        prod["estoque"] -= qtd
        
        # calculo da grana
        bruto = prod["preco"] * qtd
        desconto = bruto * 0.05 if qtd > 10 else 0.0 # 5% se for mais de 10
        final = bruto - desconto
        
        # salva historico da venda
        vendas.append({
            "cliente": cliente,
            "produto": prod["nome"],
            "qtd": qtd,
            "bruto": bruto,
            "desconto": desconto,
            "final": final
        })
        print("Venda registrada!")
        
    except ValueError:
        print("Erro: digite números válidos nas opções.")

def relatorio(vendas, salvar_txt=False):
    # monta a stringrona de texto do relatorio
    txt = "\n=== Relatório de Vendas ===\n"
    total = 0.0
    
    if not vendas:
        txt += "Nenhuma venda registrada.\n"
    else:
        for v in vendas:
            txt += f"Cliente: {v['cliente']}\n"
            txt += f"Produto: {v['produto']}\n"
            txt += f"Quantidade: {v['qtd']}\n"
            txt += f"Valor Bruto: R$ {v['bruto']:.2f}\n"
            txt += f"Desconto: R$ {v['desconto']:.2f}\n"
            txt += f"Valor Final: R$ {v['final']:.2f}\n"
            txt += "-" * 20 + "\n"
            total += v['final']
            
        txt += f"Total arrecadado pela loja: R$ {total:.2f}\n"
        
    # se a flag de salvar for true, joga pro arquivo
    if salvar_txt:
        try:
            with open("relatorio_vendas.txt", "w", encoding="utf-8") as f:
                f.write(txt)
            print("Relatório salvo em 'relatorio_vendas.txt' com sucesso!")
        except Exception as e:
            print(f"Deu ruim ao salvar o arquivo: {e}")
    else:
        print(txt)

def main():
    # inicia as listas vazias
    produtos = []
    vendas = []
    
    # loop infinito do menu
    while True:
        print("\n=== LOJA ===")
        print("1. Cadastrar produto")
        print("2. Realizar venda")
        print("3. Gerar relatório")
        print("4. Salvar relatório em arquivo")
        print("5. Sair")
        
        op = input(">> ").strip()
        
        if op == '1':
            cadastrar(produtos)
        elif op == '2':
            vender(produtos, vendas)
        elif op == '3':
            relatorio(vendas)
        elif op == '4':
            relatorio(vendas, salvar_txt=True)
        elif op == '5':
            print("Fechando o programa...")
            break
        else:
            print("Opção inválida.")

# chama a main()
if __name__ == "__main__":
    main()