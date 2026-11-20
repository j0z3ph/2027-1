import java.io.File;

public class Permisos {
    public static void main(String[] args) {
        File archi = new File("Lista.java");

        if (!archi.exists()) {
            System.err.println("No existe el archivo");
            System.exit(1);
        }

        if (!archi.isFile()) {
            System.err.println("Upss, no es un archivo");
            System.exit(1);
        }

        System.out.print((archi.isDirectory() ? "d" : "-"));
        System.out.print((archi.canRead() ? "r" : "-"));
        System.out.print((archi.canWrite() ? "w" : "-"));
        System.out.print((archi.canExecute() ? "x" : "-"));

        System.out.println("\tLista.java");
    }
}
