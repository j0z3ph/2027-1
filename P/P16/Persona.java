public class Persona {
    private String nombre;
    private int edad;

    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) throws NombreVacioException {
        if(nombre.isEmpty() || nombre.isBlank()) {
            throw new NombreVacioException();
        }
        this.nombre = nombre.trim().toUpperCase();
    }
    public int getEdad() {
        return edad;
    }
    public void setEdad(int edad) throws EdadInvalidaException {
        if(edad <= 0 || edad > 100) {
            throw new EdadInvalidaException();
        }
        this.edad = edad;
    }
    
}
