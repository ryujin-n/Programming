package aula11;

public class Tecnico extends Aluno{
    private int registro;

    public void praticar(){
        System.out.println("O registro "+ this.getRegistro() + " esta praticando!");
    }

    public int getRegistro() {
        return registro;
    }

    public void setRegistro(int registro) {
        this.registro = registro;
    }
}
