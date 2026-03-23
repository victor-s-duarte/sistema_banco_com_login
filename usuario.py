class Usuario:
    def __init__ (self, login, nome, sobrenome, saldo, senha_login, senha_cartao, email, cpf, telefone):
        self.login = login
        self.nome = nome
        self.sobrenome = sobrenome
        self._saldo = saldo
        self.__senha_login = senha_login
        self.__senha_cartao = senha_cartao
        self.email = email
        self.__cpf = cpf
        self.telefone = telefone

        self.transacoes = []
    
    num_transacao = 0

    def saudacao(self):
        print(f"Olá, {self.nome}!\n")
    
    def get_saldo(self):
        return self._saldo

    def verificar_senha_cartao(self, vrf_senha_cartao):
        return vrf_senha_cartao == self.__senha_cartao

    def verificar_senha_login(self, vrf_senha_login):
        return vrf_senha_login == self.__senha_login
    
    def verificar_cpf(self, vrf_cpf):
        return vrf_cpf == self.__cpf
        
    def registrar_transacao(self, valor, operacao, destinatario):
        Usuario.num_transacao += 1
        numero = f"{Usuario.num_transacao:06d}"
        self.transacoes.append({
            "numero": numero,
            "valor": valor,
            "operacao": operacao,
            "destinatario": destinatario
            })
        return numero

    def get_cpf_censurado(self):
        return f"{self.__cpf[:3]}.***.***-{self.__cpf[-2:]}"
