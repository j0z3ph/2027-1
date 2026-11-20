import java.io.File;
import java.io.FilenameFilter;
import java.util.Date;

public class ConFiltro {
    public static void main(String[] args) {
        File archi = new File(".");

        File[] lista = archi.listFiles(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String name) {
                return !name.endsWith(".class");
            }

        });

        for (File file : lista) {
            System.out.print((file.isDirectory() ? "d" : "-"));
            System.out.print((file.canRead() ? "r" : "-"));
            System.out.print((file.canWrite() ? "w" : "-"));
            System.out.print((file.canExecute() ? "x" : "-"));

            Date d = new Date(file.lastModified());
            System.out.print("\t" + d.toString()); 

            System.out.println("\t" + file.getName());
        }

    }
}
