public class visibilidade {
    public static void main(String[] args) {
        Caneta c1 =  new Caneta();
        c1.modelo = "BIC"; //v ai funcionar pq é publica
        c1.cor = "Azul"; // tbm vai funcionar pq é publica
//        c1.ponta = 0.5f;
        c1.carga = 80; //vai fduncionar pqe está dentro de uma classe que utiliza a classe Caneta
//        c1.tampa = false;
        c1.tampar();
        c1.status();
        c1.rabiscar();
    }
}
