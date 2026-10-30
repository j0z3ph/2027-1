import java.io.Console;

public class App3 {
    public static void main(String[] args) {
        Console c = System.console();
        String cadena = c.readLine();
        char[] password = c.readPassword();

        System.out.println(cadena);
        System.out.println(password);
    }
}
