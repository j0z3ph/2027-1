import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Verificada {
    public static void main(String[] args) {
        try {
            FileReader fw = new FileReader("archi.txt");
            fw.readAllLines();
            fw.close();
        } catch (FileNotFoundException fe) {
            IO.println("Upssss, no se encontro el archivo 🤑");
        } catch (IOException ioe) {
            IO.println("Upsss, no se pudo leer 🐧");
        }

    }
}
