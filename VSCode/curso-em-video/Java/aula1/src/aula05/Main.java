package aula05;

public class Main {

   public static void main(String[] args) {
//      Caneta c1 = new Caneta();
//      c1.setModelo("BIC");
//      c1.modelo = "BIC";
//
//      c1.setPonta(0.5f);
//      c1.ponta = 0.5f;
//      c1.status();
//      System.out.println("Tenho uma caneta: " +c1.getModelo() + " de ponta: " + c1.getPonta());

//--- com Construtor

//      Caneta c1 = new Caneta("BIC",0.4f,"Amarela" );
//      c1.status();
//
//      Caneta c2 = new Caneta("NIC",0.3f,"Preto" );
//      c2.status();

//      Teclado t1 = new Teclado("Epomaker", "Preto", "Marrom","Fio", 70);
//      t1.status();

      Banco b1 = new Banco(1111,"Jubileu");
      b1.abrirConta("cc");
      b1.depositar(500);
      b1.sacar(550);
      b1.fecharConta();
      b1.sts();

      Banco b2 = new Banco(2222,"Creuza");
      b2.abrirConta("cp");
      b2.depositar(500);
      b2.sacar(100);
      b2.sts();
   }
}
