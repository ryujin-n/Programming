package pratica02;

public class Gafanhoto extends Pessoa {
    private String login;
    private int totAssistido;

    public Gafanhoto(String nome, int idade, String sexo, String Login) {
        super(nome, idade, sexo);
        this.login = Login;
        this.totAssistido = 0;
    }

    public void maisUm(){
        this.totAssistido++;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public int getTotAssistido() {
        return totAssistido;
    }

    public void setTotAssistido(int totAssistido) {
        this.totAssistido = totAssistido;
    }

    @Override
    public String toString() {
        return "Gafanhoto{" +
                "login='" + login + '\'' +
                ", totAssistido=" + totAssistido +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                ", sexo='" + sexo + '\'' +
                ", experiencia=" + experiencia +
                '}';
    }
}
