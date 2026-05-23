public class Teclado {
    String modelo;
    String cor;
    String switches;
    String conectividade;
    int tamanho;
    boolean ligado;

    public void digitar(){
        if (this.ligado){
            System.out.println("Digitando...");
        }else {
            System.out.println("Não estou ligado");
        }
    }

    public void ligar(){
        ligado = true;
    }

    public void desligar(){
        ligado = false;
    }

    public void status(){
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Cor do teclado: " + this.cor);
        System.out.println("Tamanho do teclado: " + this.tamanho);
        System.out.println("Ligado? " + this.ligado);
    }

}
