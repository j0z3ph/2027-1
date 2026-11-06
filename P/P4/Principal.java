public class Principal {
    
    public static void main(String[] args) {
        Persona p1 = new Persona("");
        Alumno al = new Alumno();
        al.setNombre("Richi");

        System.out.println(al.getNombre());
        
        p1.setEdad(-20);

        System.out.println(p1.getEdad());
    }
}
