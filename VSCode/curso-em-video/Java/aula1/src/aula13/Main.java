package aula13;

public class Main {
    public static void main(String[] args) {
        Mamifero m1 = new Mamifero();
        m1.emitirSom();

        Lobo  lb1 = new Lobo();
        lb1.emitirSom();

        Cachorro c1 = new Cachorro();
        c1.reagir("ola");
        c1.reagir("apanhar");

        c1.reagir(11,45);
        c1.reagir(19,00);

        c1.reagir(true);
        c1.reagir(false);

        c1.reagir(2, 12.5f);
        c1.reagir(12, 4.5f);
    }
}
