import java.util.Scanner

public class Main {
    public static void main(String[] args) {
        //criando objeto scanner
        Scanner sc = new Scanner(System.in);

        //criando obj da classe conta

        Conta c1 = new Conta();

        System.out.println("Digite o nome do conta: ");
        c1.setTitular(sc.next());
        System.out.println("Digite o numero do conta: ");
        c1.setSaldo(sc.nextInt());
        System.out.println("Digite a agencia da conta: ");
        c1.setAgencia(sc.nextInt());
        System.out.println("Digite o valor do conta: ");
        c1.setSaldo(sc.nextFloat());

    }
}
