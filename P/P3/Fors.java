public class Fors {
    public static void main(String[] args) {
        float[] arreglo = new float[5];
        arreglo[0] = 8;
        arreglo[1] = 6;
        arreglo[2] = 4;
        arreglo[3] = 2;
        arreglo[4] = 1000;

        int i = 0;
        for ( ;i < arreglo.length;) {
            //continue;
            IO.print(arreglo[i] + ", ");
            i++;
            
        }

        System.out.println();

        for (float val : arreglo) {
            IO.print(val + ", ");
        }

    }
}
