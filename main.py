import os
from usuario import Usuario
from dados_usuarios import lista_de_usuarios

tentativas = 0
max_tentativas = 5
usuario_logado = None
logout = False
destinatario_usuario = None
valor_transferencia = None
opcoes_main_menu = ["1 - Depositar","2 - Sacar","3 - Transferir","4 - Histórico de transações","0 - Log out"]
opcoes = ["1","2","3","4","9","0"]
op_cancelada = "Operação cancelada: Muitas tentativas.\n"

os.system("cls")
while True:
    exibir_saldo = False
    login = input("Login: ")
    input_senha_login = input("Senha: ")
    for u in lista_de_usuarios:
        if u.login == login and u.verificar_senha_login(input_senha_login):
            usuario_logado = u

    if usuario_logado:
        os.system("cls")
        while True:
            usuario_logado.saudacao()
            main_menu = False
            tentativas = 0
            tipo_operacao = None
            if exibir_saldo == False:
                print("Saldo atual: ***\n")
                print(*opcoes_main_menu[0:4],"9 - Revelar saldo",*opcoes_main_menu[4:],sep="\n")
            else:
                print(f"Saldo atual: R${usuario_logado.get_saldo():.2f}\n")
                print(*opcoes_main_menu[0:4],"9 - Esconder saldo",*opcoes_main_menu[4:],sep="\n")

            opcao = input("\nO que deseja fazer? ")
            if opcao == "9":
                if exibir_saldo == False:
                    exibir_saldo = True
                    os.system("cls")

                else:
                    exibir_saldo = False
                    os.system("cls")

            if opcao == "1":
                tipo_operacao = "Depósito"
                os.system("cls")
                while True:
                    try:
                        print("Digite 'sair' para voltar.\n")
                        print(f"Saldo disponível: R${usuario_logado.get_saldo():.2f}")
                        valor_deposito = input("Qual valor deseja depositar? R$ ")

                        if valor_deposito == 'sair':
                            os.system("cls")
                            break

                        valor_deposito = float(valor_deposito)
                        if valor_deposito > 0:
                            os.system("cls")
                            while True:
                                print("Digite 'sair' para voltar.\n")
                                print(f"Valor do depósito: R${valor_deposito:.2f}\n")
                                input_senha_cartao = input("Digite a senha: ")
                                if input_senha_cartao == "sair":
                                    os.system("cls")
                                    break

                                if usuario_logado.verificar_senha_cartao(input_senha_cartao):
                                    os.system("cls")
                                    main_menu = True
                                    usuario_logado._saldo += valor_deposito
                                    num_transacao = usuario_logado.registrar_transacao(valor_deposito,tipo_operacao,0)
                                    print("Depósito realizado com sucesso!\n")
                                    break

                                else:
                                    os.system("cls")
                                    tentativas += 1
                                    print(f"Senha inválida. Tentativas restantes: {max_tentativas-tentativas}\n")
                                    if tentativas == max_tentativas:
                                        os.system("cls")
                                        main_menu = True
                                        print(op_cancelada)
                                        break

                            if main_menu == True:
                                main_menu = False
                                break

                        else:
                            os.system("cls")
                            print("Depósito inválido: menor ou igual à 0.\n")

                    except ValueError:
                        os.system("cls")
                        print(f"Valor inválido: '{valor_deposito}'\n")
                        pass

            if opcao == "2":
                tipo_operacao = "Saque"
                os.system("cls")
                while True:
                    try:
                        print("Digite 'sair' para voltar.\n")
                        print(f"Saldo disponível: R${usuario_logado._saldo:.2f}")
                        valor_saque = input("Qual valor deseja sacar? R$ ")
                        if valor_saque == 'sair':
                            os.system("cls")
                            break

                        valor_saque = float(valor_saque)
                        if valor_saque > 0 and valor_saque <= usuario_logado._saldo:
                            os.system("cls")
                            while True:
                                print("Digite 'sair' para voltar.\n")
                                print(f"Valor do saque: R${valor_saque:.2f}\n")
                                input_senha_cartao = input("Digite a senha: ")
                                if input_senha_cartao == "sair":
                                    os.system("cls")
                                    break

                                if usuario_logado.verificar_senha_cartao(input_senha_cartao):
                                    os.system("cls")
                                    main_menu = True
                                    usuario_logado._saldo -= valor_saque
                                    num_transacao = usuario_logado.registrar_transacao(valor_saque,tipo_operacao,0)
                                    print("Saque realizado com sucesso!\n")
                                    break

                                else:
                                    os.system("cls")
                                    tentativas += 1
                                    print(f"Senha inválida. Tentativas restantes: {max_tentativas-tentativas}\n")
                                    if tentativas == max_tentativas:
                                        os.system("cls")
                                        main_menu = True
                                        print(op_cancelada)
                                        break

                            if main_menu == True:
                                main_menu = False
                                break
                        
                        if valor_saque >= usuario_logado._saldo:
                            os.system("cls")
                            print("Saque inválido: saldo insuficiente.\n")
                        
                        if valor_saque < 0:
                            os.system("cls")
                            print("Saque inválido: menor ou igual à 0.\n")

                    except ValueError:
                        os.system("cls")
                        print(f"Valor inválido: '{valor_saque}'\n")
                        pass
            
            if opcao == "3":
                tipo_operacao = "Transferência"
                os.system("cls")
                while True:
                    if main_menu == True:
                        break
                    print("Digite 'sair' para voltar.\n")
                    destinatario_chave = str(input("Digite a chave para transferência (CPF, e-mail ou n° de telefone): "))
                    if destinatario_chave == 'sair':
                        os.system("cls")
                        break
                    
                    for u in lista_de_usuarios:
                        if usuario_logado.email == destinatario_chave or usuario_logado.telefone == destinatario_chave or usuario_logado.verificar_cpf(destinatario_chave):
                            os.system("cls")
                            print("Você não pode realizar transferências para si mesmo.\n")
                            break
                        if u.email == destinatario_chave or u.telefone == destinatario_chave or u.verificar_cpf(destinatario_chave):
                            destinatario_usuario = u
                            os.system("cls")
                            while True:
                                try:
                                    if main_menu == True:
                                        break
                                    print("Digite 'sair' para voltar.\n")
                                    print(f"Destinatário:")
                                    print(f"  Nome: {destinatario_usuario.nome} {destinatario_usuario.sobrenome}")
                                    print(f"  CPF: {destinatario_usuario.get_cpf_censurado()}\n")
                                    print(f"Saldo disponível: R${usuario_logado._saldo:.2f}")
                                    valor_transferencia = input("Qual valor deseja transferir? R$ ")
                                    if valor_transferencia == 'sair':
                                        os.system("cls")
                                        break

                                    valor_transferencia = float(valor_transferencia)
                                    if valor_transferencia > 0 and valor_transferencia <= usuario_logado._saldo:
                                        os.system("cls")
                                        while True:
                                            print("Digite 'sair' para voltar.\n")
                                            print(f"Valor da transferência: R${valor_transferencia:.2f}\n")
                                            input_senha_cartao = input("Digite a senha: ")
                                            if input_senha_cartao == "sair":
                                                os.system("cls")
                                                break

                                            if usuario_logado.verificar_senha_cartao(input_senha_cartao):
                                                os.system("cls")
                                                main_menu = True
                                                usuario_logado._saldo -= valor_transferencia
                                                destinatario_usuario._saldo += valor_transferencia
                                                num_transacao = usuario_logado.registrar_transacao(valor_transferencia,tipo_operacao,f"{destinatario_usuario.nome} {destinatario_usuario.sobrenome}")
                                                print("Transferência realizada com sucesso!\n")
                                                break

                                            else:
                                                os.system("cls")
                                                tentativas += 1
                                                print(f"Senha inválida. Tentativas restantes: {max_tentativas-tentativas}\n")
                                                if tentativas == max_tentativas:
                                                    os.system("cls")
                                                    main_menu = True
                                                    print(op_cancelada)
                                                    break
                                        
                                    else:
                                        os.system("cls")
                                        print("Transferência inválida: saldo insuficiente.\n")

                                except ValueError:
                                    os.system("cls")
                                    print(f"Valor inválido: '{valor_transferencia}'\n")

                        if valor_transferencia == "sair":
                            valor_transferencia = None
                            break

                        if main_menu == True:
                            break
                                                
                        else:
                            os.system("cls")
                            print(f"Usuário não encontrado: '{destinatario_chave}'\n")
                    
                    if main_menu == True:
                        main = False
                        break

            if opcao == "4":
                os.system("cls")
                if not usuario_logado.transacoes:
                    print("Nenhuma transação encontrada.")

                else:
                    print("Histórico de transações:\n")
                    for t in usuario_logado.transacoes:
                        if t["operacao"] == "Transferência":
                            print(f"Transação ID {t["numero"]}: {t["operacao"]} de R${t["valor"]:.2f} para {t["destinatario"]}")
                        
                        else:
                            print(f"Transação ID {t["numero"]}: {t["operacao"]} de R${t["valor"]:.2f}")

                input("\nDigite qualquer tecla para sair ")
                os.system("cls")
                pass

            if opcao == "0":
                os.system("cls")
                usuario_logado = None
                break

            if opcao not in opcoes:
                os.system("cls")
                print(f"Opção inválida: '{opcao}'\n")

    else:
        os.system("cls")
        print("Usuário inválido.\n")