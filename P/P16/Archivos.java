import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Archivos {
    public static void main(String[] args) {
        try (FileReader fr = new FileReader("archi.txt")) {
            fr.read();
        } catch (IOException e) {
            
            e.printStackTrace();
        }

    }
}
