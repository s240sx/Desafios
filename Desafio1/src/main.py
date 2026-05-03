# Importando as funções do módulo dentro da pasta utils
from utils.funcoes import calcular_salarios, gerar_relatorio_texto, salvar_em_arquivo

def main():
    lista_funcionarios = []

    while True:
        print("\n1. Cadastrar | 2. Relatório | 3. Salvar | 4. Sair [cite: 14]")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                nome = input("Nome: ").strip()
                if not nome: raise ValueError("Nome não pode ser vazio [cite: 35]")
                
                tipo = input("Tipo (estagiario/clt/freelancer): ").lower().strip()
                if tipo not in ['estagiario', 'clt', 'freelancer']: 
                    raise ValueError("Tipo inválido [cite: 36]")

                if tipo == 'freelancer':
                    h = float(input("Horas: "))
                    v = float(input("Valor/Hora: "))
                    res = calcular_salarios(tipo, h, v)
                else:
                    s = float(input("Salário/Bolsa: "))
                    res = calcular_salarios(tipo, s)

                # Organiza os dados em um dicionário [cite: 95]
                lista_funcionarios.append({
                    "nome": nome, "tipo": tipo.capitalize(),
                    "bruto": res[0], "inss": res[1], "irrf": res[2], "liquido": res[3]
                })
                print("Funcionário cadastrado!")

            except ValueError as e:
                print(f"Erro de entrada: {e} [cite: 39]")

        elif opcao == '2':
            print("\n" + gerar_relatorio_texto(lista_funcionarios))

        elif opcao == '3':
            texto = gerar_relatorio_texto(lista_funcionarios)
            salvar_em_arquivo(texto)

        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()