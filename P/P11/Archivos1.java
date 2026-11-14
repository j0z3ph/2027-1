import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Archivos1 {

    public static void main(String[] args) {
        File archi = new File("archivo.txt");
        FileWriter fw;
        String cadenaUsuario;

        IO.print("Querido usuario, escribe algo: ");

        cadenaUsuario = IO.readln();

        try {
            archi.createNewFile();
            // Ya existe el archivo
            fw = new FileWriter(archi);

            fw.write(cadenaUsuario);

            fw.close();
        } catch (IOException e) {
            System.out.println("Uppsi, no furulo");
        }

    }
}
