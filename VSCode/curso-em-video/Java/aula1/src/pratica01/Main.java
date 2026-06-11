package pratica01;

public class Main {
    public static void main(String[] args) {
        Pessoa[] p = new Pessoa[4];
        p[0] = new Pessoa("Maria",12, "F");
        p[1] = new Pessoa("Joao",12, "M");
        p[2] = new Pessoa("Luiza",12, "F");
        p[3] = new Pessoa("Marcio",12, "M");


        Livro[] l = new Livro[4];
        l[0] = new Livro("Livro1","Miles",3, p[0]);
        l[1] = new Livro("Livro2","Miles",2, p[1]);
        l[2] = new Livro("Livro3","Miles",4, p[2]);
        l[3] = new Livro("Livro3","Miles",5, p[3]);

        l[0].abrir();
        l[0].folhear(3);
        l[0].fechar();
        System.out.println(l[0].detalhes());
    }
}
