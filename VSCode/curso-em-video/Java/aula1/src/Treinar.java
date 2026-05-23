public class Treinar {
    String musculo;
    String exercicio;
    int repeticao;
    float peso;
    int sets;

    public void exercitar(){
        System.out.println("Estou exercitando esse músculo: " + this.musculo);
        System.out.println("neste exercicio: " + this.exercicio);
        System.out.println("com " + this.sets + " sets" );
        System.out.println("de "+ this.repeticao + " repetições");
        System.out.println("com "+ this.peso + "kg");
    }
}
