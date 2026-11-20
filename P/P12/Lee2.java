import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Lee2 {
    public static void main(String[] args) throws FileNotFoundException {
        File archi = new File("prueba.txt");

        if (!archi.exists()) {
            System.err.println("Lastima");
            System.exit(1);
        }

        Scanner s = new Scanner(archi);
        while (s.hasNext())
            System.out.println(s.nextLine());

        s.close();
    }
}
