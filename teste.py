import datetime
from enum import Enum


class Conta:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.Extrato = Extrato()

    def depositar(self, transacao):
      self.Extrato.salvarTransacao(transacao)
      self.calcularSaldo()


    def sacar(self, transacao):
        if (self.saldo < transacao.valor):
            print("Você não tem saldo suficiente.")
        else:
            self.Extrato.salvarTransacao(transacao)
            self.calcularSaldo()

    def consultaSaldo(self):
        print(f"Saldo de R$ {self.saldo:,.2f}")

    def calcularSaldo(self):
      for transacao in self.Extrato.historico:
        if (transacao.tipo == TipoTransacao.Deposito):
          self.saldo += transacao.valor
          print("entrou no if")
        else:
          self.saldo -= transacao.valor

class Extrato:

  def __init__(self):
    self.historico = []

  def salvarTransacao(self, transacao):
    self.historico.append(transacao)

class TipoTransacao(Enum):
  Deposito = 1
  Saque = 2


class Transacao:
  def __init__(self, valor, tipo):
    self.valor = valor
    self.tipo = tipo
    self.data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
def __str__(self):
   return "errei"

conta_do_rodrigo = Conta("Rodrigo", "15958489245")

transacaoDeposito = Transacao(500, TipoTransacao.Deposito)
transacaoSaque = Transacao(100, TipoTransacao.Saque)
conta_do_rodrigo.depositar(transacaoDeposito)
conta_do_rodrigo.depositar(transacaoDeposito)
conta_do_rodrigo.depositar(transacaoDeposito)
conta_do_rodrigo.depositar(transacaoDeposito)
conta_do_rodrigo.depositar(transacaoDeposito)
conta_do_rodrigo.depositar(transacaoDeposito)

conta_do_rodrigo.sacar(transacaoSaque)
transacaoSaque.valor = 700
conta_do_rodrigo.sacar(transacaoSaque)
conta_do_rodrigo.sacar(transacaoSaque)

conta_do_rodrigo.depositar(transacaoDeposito)
transacaoSaque.valor = 200
conta_do_rodrigo.sacar(transacaoSaque)
conta_do_rodrigo.sacar(transacaoSaque)

for transacao in conta_do_rodrigo.Extrato.historico:
    print(f"valor: R${transacao.valor}")
    print(f"tipo: {transacao.tipo}")
    print(f"data: {transacao.data}")
    print(conta_do_rodrigo.consultaSaldo())

conta_do_rodrigo.consultaSaldo()
#da um crtl + S nos arquivos, dps vc da um git add -A no terminal, git commit "adicionando alterações", git push
