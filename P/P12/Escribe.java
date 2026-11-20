import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

public class Escribe {
    
    public static void main(String[] args) throws IOException {
        File archi = new File("prueba.txt");
        Writer w;

        if(!archi.exists()) {
            archi.createNewFile();
        }

        w = new FileWriter(archi);
        w.write("Holi :D\nAdios D:");
        w.close();
    }
}
