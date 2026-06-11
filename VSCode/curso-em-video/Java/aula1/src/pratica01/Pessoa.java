package pratica01;

public class Pessoa {
    //* Atributos
    private String nome;
    private int idade;
    private String sexo;

    //* Metodos Publicos
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    //? Construtor

    public Pessoa(String nome, int idade, String sexo) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
    }

    //* Metodos Especiais
    public void fazerAniversario(){
        System.out.println("Parabens, é seu aniversario");
        setIdade(getIdade() + 1);
        System.out.println(this.getNome() + " tem " + this.getIdade() + " anos!");
    }
}
