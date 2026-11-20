import java.io.File;

public class Borra {
    public static void main(String[] args) {
        File archi = new File("prueba.txt");
        archi.delete();
    }   
}
