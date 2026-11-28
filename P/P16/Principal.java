public class Principal {
    public static void main(String[] args) {
        Persona p = new Persona();
        try {
            p.setEdad(5);
            p.setNombre("      ");
        } catch (EdadInvalidaException e) {
            IO.println("Ja, eso no se puede");
        } finally {
            IO.println("Prueba");
        }
    }
}
