package pratica01;

public class Livro implements Publicacao {
    //* Atributos
    private String titulo;
    private String autor;
    private int totPag;
    private boolean aberto;
    private int pagAtual;
    private Pessoa leitor;

    //* Metodos Publicos

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getTotPag() {
        return totPag;
    }

    public void setTotPag(int totPag) {
        this.totPag = totPag;
    }

    public int getPagAtual() {
        return pagAtual;
    }

    public void setPagAtual(int pagAtual) {
        this.pagAtual = pagAtual;
    }

    public boolean getAberto() {
        return aberto;
    }

    public void setAberto(boolean aberto) {
        this.aberto = aberto;
    }

    public Pessoa getLeitor() {
        return leitor;
    }

    public void setLeitor(Pessoa leitor) {
        this.leitor = leitor;
    }

    //* Metodos Especiais

    public String detalhes() {
        return "========= DETALHES =========" + "\n" +
                "Titulo: " + titulo + "\n" +
                "Autor: " + autor + "\n" +
                "Qtde de Pags: " + totPag + "\n" +
                "Pagina Atual: " + pagAtual + "\n" +
                "Aberto?: " + aberto + "\n"+
                "Leitor: " + leitor.getNome() + "\n"+
                "Idade: " + leitor.getIdade() + "\n"+
                "Sexo: " + leitor.getNome() + "\n" +
                "===========================";
    }
    //* Metodos Abstratos

    @Override
    public void abrir() {
        if(!this.getAberto()){
            System.out.println("Abrindo o livro: " + this.getTitulo() + " de " +  this.getLeitor().getNome());
            this.setAberto(true);
        }
        else {
            System.out.println("Livro já está aberto!");
        }
    }

    @Override
    public void fechar() {
        if(this.getAberto()){
            System.out.println("Fechando...");
            this.setAberto(false);
            this.setPagAtual(0);
        }
        else {
            System.out.println("Esse livro já está fechado");
        }
    }

    @Override
    public void folhear(int p) {
        if(this.getAberto()){
            System.out.println("Folheando...");
            if(p > this.getTotPag()){
                System.out.println("Acabou o livro!");
                fechar();
            }
            else {
                this.setPagAtual(p);
                System.out.println("Voce folheou: " + p + " paginas");
                System.out.println("Estamos na pagina: " + this.getPagAtual());
            }
        }
        else{
            System.out.println("Livro está fechado!");
        }
    }

    @Override
    public void avancarPag(int p) {
        if(this.getAberto()){
            System.out.println("Avançando pagina...");
            if (this.getPagAtual() < this.getTotPag()) {
                this.setPagAtual(this.getPagAtual() + p);
            } else  {
                System.out.println("Acabou o livro!");
                fechar();
            }
        }
        else{
            System.out.println("Livro está fechado!");
        }
    }

    @Override
    public void voltarPag(int p) {
        if(this.getAberto()){
            System.out.println("Voltando pagina...");
            if (p <= this.getTotPag()) {
                this.setPagAtual(this.getPagAtual() - p);
            }
            else if(p > this.getPagAtual()) {
                System.out.println("Acabou o livro!");
                fechar();
            }
        }
        else{
            System.out.println("Livro está fechado!");
        }
    }

    public Livro(String titulo, String autor, int totPag, Pessoa leitor) {
        this.titulo = titulo;
        this.autor = autor;
        this.totPag = totPag;
        this.leitor = leitor;
        this.pagAtual = 0;
        this.aberto = false;
    }
}
