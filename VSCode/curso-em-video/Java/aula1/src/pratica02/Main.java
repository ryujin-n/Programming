package pratica02;

public class Main {
    public static void main(String[] args) {
        Video[] v = new Video[3];
        v[0] = new Video("Aula1");
        v[1] = new Video("Aula2");
        v[2] = new Video("Aula3");

        Gafanhoto[] g = new Gafanhoto[2];
        g[0] = new Gafanhoto("Miles",22,"M","mimi");
        g[1] = new Gafanhoto("Joao",12,"M","jojo");


        Visualizacao[] vis = new Visualizacao[5];
        vis[0] = new Visualizacao(g[0],v[0]);
        vis[0].avaliar();
        System.out.println(vis[0].toString());

        vis[1] = new Visualizacao(g[0],v[1]);
        vis[1].avaliar(87);
        System.out.println(vis[1].toString());
    }
}
