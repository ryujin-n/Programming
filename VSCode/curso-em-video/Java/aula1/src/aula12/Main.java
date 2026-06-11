package aula12;

public class Main {
    public static void main(String[] args) {
        Mamifero m1 = new Mamifero();
        Reptil r1 = new Reptil();
        Peixe p1 = new Peixe();
        Ave a1 = new Ave();

//        m1.alimentar();
//        m1.locomover();
//        m1.emitirSom();
//
//        System.out.println("-------------------");
//
//        r1.alimentar();
//        r1.locomover();
//        r1.emitirSom();
//
//        System.out.println("-------------------");
//
//        p1.alimentar();
//        p1.locomover();
//        p1.emitirSom();
//
//        System.out.println("-------------------");
//
//        a1.alimentar();
//        a1.locomover();
//        a1.emitirSom();

        Canguru cg = new Canguru();
        Cachorro ch = new Cachorro();
        Cobra co = new Cobra();
        Tartaruga tar = new Tartaruga();
        GoldFish gf = new GoldFish();
        Arara ar = new Arara();

        cg.locomover();
        ch.locomover();
        co.locomover();
        tar.locomover();
        gf.locomover();
        ar.locomover();

        System.out.println("-------------------");

        cg.emitirSom();
        ch.emitirSom();
        co.emitirSom();
        tar.emitirSom();
        gf.emitirSom();
        ar.emitirSom();

    }
}
