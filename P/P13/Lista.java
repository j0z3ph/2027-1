import java.io.File;

public class Lista {
    public static void main(String[] args) {
        File archi = new File("../");
        String[] lista = archi.list();

        for (String string : lista) {
            System.out.println(string);
        }
    }
}
