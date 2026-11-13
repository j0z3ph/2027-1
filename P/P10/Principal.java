import java.io.File;
import java.io.IOException;

import figuras.Figura;
import figuras.dosd.Circulo;
import figuras.tresd.Esfera;

public class Principal {

    public static void main(String[] args) throws IOException {
        Figura f = new Figura();

        File archi = new File("/Users/j0z3ph/Repos/2027-1/P/P10/figuras/tresd/Bien_Facil.txt");
        if (!archi.createNewFile()) {
            System.err.println("Uppsssss, no jalo :(");
        }

        

    }

}
