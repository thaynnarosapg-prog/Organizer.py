
print("======================================")
print("       MY ORGANIZER")
print("======================================")
print("Bem-vindo!")
print("Vamos organizar seus estudos e prazos!")

nome = input("Olá, qual seu nome? ")

print("Bem vindo(a),", nome, "!")
print("Vamos organizar sua vida acadêmica.")

atividades = []
continuar = "s"

while continuar == "s":

    print("\n--- NOVA ATIVIDADE ---")

    materia = input("Qual a matéria? ")
    atividade = input("Qual o nome da atividade ou projeto? ")
    data_entrega = input("Data de entrega: ")
    horário = input("Qual o horário da entrega? ")

    print("Deseja adicionar alguma observação?")
    obs = input("Digite aqui: ")

    status = input("A atividade já foi concluída? (s/n): ")

    if status == "s":
        status = "Concluída"
    else:
        status = "Pendente"

    lembrete = {
        "materia": materia,
        "atividade": atividade,
        "data": data_entrega,
        "horario": horário,
        "observacao": obs,
        "status": status
    }

    atividades.append(lembrete)

    print("\nAtividade cadastrada com sucesso!")

    continuar = input("Deseja cadastrar outra atividade? (s/n): ")

print("\n======================================")
print("       RESUMO DAS SUAS ATIVIDADES")
print("======================================")
print("Estudante:", nome)

for lembrete in atividades:
    print("\n------------------------------")
    print("Matéria:", lembrete["materia"])
    print("Atividade:", lembrete["atividade"])
    print("Data de entrega:", lembrete["data"])
    print("Horário:", lembrete["horario"])
    print("Observação:", lembrete["observacao"])
    print("Status:", lembrete["status"])

print("\nTotal de atividades cadastradas:", len(atividades))
print("Obrigado por usar o Organizador Acadêmico!")
