import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Lee {
    public static void main(String[] args) throws IOException {
        File archi = new File("prueba.txt");
        if(!archi.exists()) {
            System.err.println("No existe el archivo T~T");
            System.exit(1);
        }

        FileReader r = new FileReader(archi);
        String cadena = r.readAllAsString();
        System.out.println(cadena);
        r.close();
    }
}
