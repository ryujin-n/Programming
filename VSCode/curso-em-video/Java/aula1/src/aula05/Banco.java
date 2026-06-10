package aula05;

public class Banco {
    public int numConta;
    protected String tipo;
    private String dono;
    private double saldo;
    private boolean status;
    public String sts;



    public int getNumConta() {
        return numConta;
    }

    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getDono() {
        return dono;
    }

    public void setDono(String dono) {
        this.dono = dono;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    public void setStatus(boolean status) {
        this.status = status;
    }

    public boolean getStatus() {
        return status;
    }

    ///////////////////////////////////////////////

    public void abrirConta(String t) {
        this.setTipo(t);
        this.setStatus(true);
        if (t.equals("cc")){
            this.setSaldo(50);
            System.out.println("=================================");
            System.out.println("Conta Corrente aberta com sucesso");
            System.out.println("=================================");
        }
        else if(t.equals("cp")){
            this.setSaldo(150);
            System.out.println("=================================");
            System.out.println("Conta Poupança aberta com sucesso");
            System.out.println("=================================");
        }
        else{
            System.out.println("Insira um tipo corretamente (CC/CP)");
        }
    }
    public void fecharConta(){
        if(this.getStatus()){
            if(this.getSaldo() > 0){
                System.out.println("Ainda há saldo, Conta permanecerá aberta até todo o saldo ser sacado");
            }
            else if(this.getSaldo() < 0){
                System.out.println("Conta em debito");
            }
            else{
                this.setStatus(false);
                System.out.println("Conta fechada com sucesso!");
            }
        }
        else {
            System.out.println("Erro ao fechar a conta!");
        }
    }

    public void depositar(double v){
        if (this.getStatus()){
            this.setSaldo(this.getSaldo() + v);
            System.out.println("Depositado com sucesso! na conta de: "+this.getDono());
        }
        else {
            System.out.println("Erro ao depositar!");
        }
    }

    public void sacar(double vSaque) {
        if (this.getStatus()) {
            if (this.getSaldo() >= vSaque) {
                this.setSaldo(this.getSaldo() - vSaque);
                System.out.println("Sacado com sucesso na conta de: "+this.getDono());
            }
            else {
                System.out.println("Saldo insuficiente!");
            }
        }
        else  {
            System.out.println("Erro ao sacar!");
        }
    }

    public void pagarMensal(){
       int v;

       if (this.getTipo().equals("cc")) {
           v = 12;
       }
       else{
           v = 20;
       }
       if (this.getStatus()) {
           if (this.getSaldo() > v) {
               this.setSaldo(this.getSaldo() - v);
               System.out.println("Mensalidade paga com sucesso por: "+this.getDono());
           }
           else {
               System.out.println("Saldo insuficiente!");
           }
       }
       else{
           System.out.println("Erro ao pagar!");
       }
    }

    public Banco(int conta, String dono) {
        this.saldo = 0;
        this.status = false;
        this.numConta = conta;
        this.dono = dono;
    }

    public void sts(){
        System.out.println("Conta: " + this.getNumConta());
        System.out.println("Tipo: " + this.getTipo());
        System.out.println("Dono: " + this.getDono());
        System.out.println("Saldo: " + this.getSaldo());
        System.out.println("Status: " + this.status);
    }

}
