public class Persona {
    protected String nombre;
    protected int edad;

    // Constructores 

    Persona() {

    }

    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    Persona(String nombre){
        this.nombre = nombre;
        this.edad = 0;
    }

    // Getters
    public int getEdad() {
        return edad;
    }

    public String getNombre() {
        return nombre;
    }

    // Setters

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }



    
}
