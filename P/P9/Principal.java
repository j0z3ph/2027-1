import java.util.Scanner;

public class Principal implements Interfaz {

    @Override
    public void abstracto() {
        System.out.println("Hola");
    }

    public void abstracto(String s) {
        System.out.println(s);
    }
    
    public static void main(String[] args) {
        Principal p = new Principal();
        p.abstracto(null);
        p.metodo();

        Scanner s = new Scanner(System.in);
    }
}
