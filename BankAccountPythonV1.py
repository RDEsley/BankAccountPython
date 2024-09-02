class BankAccount:
    def __init__(self, name, balance=2547.0):
        self.name = name
        self.balance = balance
        self.account_type = None

    def authenticate(self, password, max_attempts=3):
        for attempt in range(1, max_attempts + 1):
            input_password = input("Digite sua senha: (Tente '123456') \n")
            if input_password == password:
                return True
            elif attempt < max_attempts:
                print(f"Senha incorreta! Você tem mais {max_attempts - attempt} chances!")
            else:
                print("Senha incorreta! Você atingiu o número máximo de tentativas. \nConta Bloqueada.")
                return False

    def select_account_type(self):
        while True:
            try:
                print(f"\nBem-vindo de volta, {self.name}!\nTipo de Conta: \n[1] - Conta Corrente")
                self.account_type = int(input("Escolha o tipo de conta: "))
                if self.account_type == 1:
                    return
                else:
                    print("Opção inválida! Tente novamente...")
            except ValueError:
                print("Opção inválida! Por favor, digite um número.")

    def show_balance(self):
        print(f"O saldo atual é R$ {self.balance:.2f}")

    def transfer(self):
        try:
            value = float(input("Qual é o valor que você deseja transferir: "))
            if value > self.balance:
                print(f"Valor Insuficiente!\nSeu saldo é: R$ {self.balance:.2f}")
            else:
                self.balance -= value
                print(f"O valor foi transferido com sucesso!\nSeu saldo atual é agora: R$ {self.balance:.2f}")
        except ValueError:
            print("Valor inválido! Por favor, insira um número.")

    def receive(self):
        try:
            value = float(input("Valor recebido: "))
            self.balance += value
            print(f"O valor foi adicionado ao seu saldo com sucesso!\nSeu saldo atual é agora: R$ {self.balance:.2f}")
        except ValueError:
            print("Valor inválido! Por favor, insira um número.")

    def show_menu(self):
        menu = ("\nOperações:\n"
                "[1] - Verificar saldo\n"
                "[2] - Transferir valor\n"
                "[3] - Receber valor\n"
                "[4] - Sair\n"
                "===========================================")
        while True:
            print(menu)
            try:
                choice = int(input("Qual é a escolha desejada? "))
                if choice == 1:
                    self.show_balance()
                elif choice == 2:
                    self.transfer()
                elif choice == 3:
                    self.receive()
                elif choice == 4:
                    print("Saindo... Até logo!")
                    break
                else:
                    print("Opção inválida! Tente novamente...")
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")


def main():
    name = input("Digite o seu primeiro nome: \n")
    account = BankAccount(name)

    if account.authenticate(password="123456"):
        account.select_account_type()
        account.show_menu()


if __name__ == "__main__":
    main()
