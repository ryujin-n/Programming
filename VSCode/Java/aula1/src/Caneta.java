public class Caneta {
    String modelo;
    String cor;
    float ponta;
    boolean tampa;

    void status(){
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Uma caneta " + this.cor);
        System.out.println("ponta " + this.ponta);
        System.out.println("está tampada? " + this.tampa);
    }

    void rabiscar(){
        if (this.tampa == true){
            System.out.println("Erro, não vou rabiscar");
        } else  {
            System.out.println("Estou rabiscando");
        }
    }

    void tampar(){
        this.tampa = true; // this é referenciado ao objeto que chamou a classe
    }
    void destampar(){
        this.tampa = false;
    }
}
