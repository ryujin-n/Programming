package aula05;

public class Caneta {
//    String modelo;
//    String cor;
//    float ponta;
//    boolean tampa;
//
//    void status(){
//        System.out.println("Modelo: " + this.modelo);
//        System.out.println("Uma caneta " + this.cor);
//        System.out.println("ponta " + this.ponta);
//        System.out.println("está tampada? " + this.tampa);
//    }
//
//    void rabiscar(){
//        if (this.tampa == true){
//            System.out.println("Erro, não vou rabiscar");
//        } else  {
//            System.out.println("Estou rabiscando");
//        }
//    }
//
//    void tampar(){
//        this.tampa = true; // this é referenciado ao objeto que chamou a classe
//    }
//    void destampar(){
//        this.tampa = false;
//    }

    private String modelo;
    private float ponta;
    private boolean tampa;
    private String cor;

    public Caneta(String modelo, float ponta, String cor) {
        this.modelo = modelo;
        this.ponta = ponta;
        this.cor = cor;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public float getPonta() {
        return ponta;
    }

    public void setPonta(float ponta) {
        this.ponta = ponta;
    }

    public boolean isTampa() {
        return tampa;
    }

    public void setTampa(boolean tampa) {
        this.tampa = tampa;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }
    public void status(){
        System.out.println("CANETA:");
        System.out.println("Modelo: "+this.getModelo());
        System.out.println("Ponta: "+this.getPonta());
        System.out.println("Cor: "+ this.cor);
        System.out.println("Tampada?: "+this.tampa);
    }

}
