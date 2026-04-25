public class Main {
    public static void main(String[] args) {
       Caneta c1 = new Caneta();
       c1.modelo = "BIC";
       c1.cor = "Azul";
       c1.ponta = 0.5f;
       c1.tampar();
       c1.status();
       c1.rabiscar();

       System.out.println("----------------");

       Caneta c2 = new Caneta();
       c2.modelo = "Nanquin";
       c2.cor = "Preta";
       c2.destampar();
       c2.status();
       c2.rabiscar();

       System.out.println("----------------");

       Teclado t1 = new Teclado();
       t1.modelo = "Akko";
       t1.cor = "preto";
       t1.switches = "marrom fodinha";
       t1.conectividade = "wireless";
       t1.tamanho = 60;
       t1.ligar();

       t1.status();
       t1.digitar();

       System.out.println("----------------");

       Treinar tr1 = new Treinar();
       tr1.musculo = "triceps";
       tr1.exercicio = "triceps na barra";
       tr1.sets = 3;
       tr1.repeticao = 12;
       tr1.peso = 45.4f;

       tr1.exercitar();

    }
}
