public class Caneta {
    public String modelo;
    public String cor;
    private float ponta;
    protected int carga;
    private boolean tampa;

    public void status(){
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Uma caneta " + this.cor);
        System.out.println("ponta " + this.ponta);
        System.out.println("carga: " + this.carga);
        System.out.println("está tampada? " + this.tampa);
    }

    public void rabiscar(){
        if (this.tampa == true){
            System.out.println("Erro, não vou rabiscar");
        } else  {
            System.out.println("Estou rabiscando");
        }
    }

    protected void tampar(){
        this.tampa = true; // "this"é referenciado ao objeto que chamou a classe
    }
    protected void destampar(){
        this.tampa = false;
    }
}
