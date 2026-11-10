import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Principal {

    public static void main(String[] args) {
        List<Integer> lista = new ArrayList<Integer>();

        List<Integer> lista2 = new LinkedList<>();

        String[] arreglo = new String[100];

        System.out.println(arreglo[-101]);

        lista2.add(4);
        lista2.add(4);
        lista2.add(4);
        lista2.add(4);
        lista2.add(4);
        lista2.add(4);
        lista2.add(4);
        lista2.add(4);
        lista2.add(4);

        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        lista.add(1);
        
        Persona p = new Persona();
        p.metodo();
    }

}
