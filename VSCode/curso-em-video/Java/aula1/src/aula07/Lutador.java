package aula07;

public class Lutador {
    //* Atributos
    private String nome, nacionalidade, categoria;
    private int idade, vitorias, derrotas, empates;
    private float peso, altura;

    //* Metodos Publicos
    public void apresentar(){
        System.out.println("----------------------------------------------------------");
        System.out.println("Chegou a hora, apresentamos o lutador " + this.getNome());
        System.out.println("Diretamente de " + this.getNacionalidade());
        System.out.println("com " + this.getIdade() + " anos de idade");
        System.out.println("Pesando " + this.getPeso() + "kg");
        System.out.println("Com " + this.getVitorias() + " vitorias");
        System.out.println(this.getDerrotas() + " derrotas");
        System.out.println("e " + this.getEmpates() + " empates");


    }
    public void status(){
        System.out.println("----------------------------------------------------------");
        System.out.println("Lutador " + this.getNome() + " é um peso " + this.getCategoria());
        System.out.println("Ganhou: "+ this.getVitorias() + " lutas");
        System.out.println("Perdeu: "+ this.getDerrotas() + " lutas");
        System.out.println("Empatou: "+ this.getEmpates() + " lutas");
    }
    public void ganharLuta(){
        this.setVitorias(this.getVitorias() + 1);
    }
    public void perderLuta(){
        this.setDerrotas(this.getDerrotas() + 1);
    }
    public void empatarLuta(){
        this.setEmpates(this.getEmpates() + 1);
    }

    //* Metodos Especiais

    public Lutador(String no, String na, int id, int vi, int de, int em, float pe, float al) {
        this.nome = no;
        this.nacionalidade = na;
        this.idade = id;
        this.vitorias = vi;
        this.derrotas = de;
        this.empates = em;
        this.setPeso(pe);
        this.altura = al;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public String getCategoria() {
        return categoria;
    }

    private void setCategoria() {
        if(this.peso< 52.2){
            this.categoria = "Inválido";
        } else if(this.peso <= 70.3){
            this.categoria = "Leve";
        } else if(this.peso <= 83.9){
            this.categoria = "Medio";
        } else if(this.peso <= 102.2){
            this.categoria = "Pesado";
        } else{
            this.categoria = "Inválido";
        }
    }


    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public int getVitorias() {
        return vitorias;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        this.setCategoria();
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }
}
