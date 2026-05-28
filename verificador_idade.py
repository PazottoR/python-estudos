from datetime import date  # biblioteca para trabalhar com datas

nome = input("Digite seu nome completo: ")
nascimento = input("Qual é sua data de nascimento? (DD/MM/AAAA): ")
cpf = input("Qual é o seu CPF: ")

try:
    dia, mes, ano = map(int, nascimento.split("/"))  # separa e converte "10/02/2008" em números
    data_nascimento = date(ano, mes, dia)
    hoje = date.today()

    # desconta 1 ano se o aniversário ainda não passou neste ano
    idade = hoje.year - data_nascimento.year - (
        (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
    )

    if idade >= 18:
        print(f"Tudo bem, {nome}! Você tem {idade} anos, seja bem-vindo(a)!")
    else:
        print(f"Poxa, {nome}! Você tem {idade} anos e é menor de idade, não será possível ter acesso!")

except ValueError:
    print("Data inválida! Use o formato DD/MM/AAAA (exemplo: 10/02/2008).")
