public class Conta {
    private String titular;
    private int nro_conta, agencia;
    private float saldo;

    //getters

    public String getTitular() {
        return titular;
    }
    public int getNro_conta() {
        return nro_conta;
    }
    public int getAgencia() {
        return agencia;
    }
    public float getSaldo() {
        return saldo;
    }

    //setters
    public void setTitular(String titular) {
        this.titular = titular;
    }
    public void setNro_conta(int nro_conta) {
        this.nro_conta = nro_conta;
    }
    public void setAgencia(int agencia) {
        this.agencia = agencia;
    }
    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public void depositar(float valor) {
        this.saldo += valor;
    }

    public void sacar(float valor) {
        this.saldo -= valor;
    }
    public void MostrarDados(){
        System.out.println("==== Dados da Conta ====");
        System.out.println("Titular: " + this.titular);
        System.out.println("Nro Conta: " + this.nro_conta);
        System.out.println("Agencia: " + this.agencia);
        System.out.println("Saldo: " + this.saldo);
    }
}
