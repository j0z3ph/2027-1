public class Principal {
    public static void main(String[] args) {
        Agenda agenda = new Agenda();

        Contacto c = new Contacto("Brayan", "5610316636");
        agenda.agregarContacto(c);

        agenda.agregarContacto(new Contacto("Richie", "7227975511"));

        for (Contacto contacto : agenda.listar()) {
            IO.println("Nombre: " + contacto.getNombre());
            IO.println("Telefono: " + contacto.getTelefono());
            IO.println("------------------");
        }

        agenda.eliminarContacto("5610316636");

        for (Contacto contacto : agenda.listar()) {
            IO.println("Nombre: " + contacto.getNombre());
            IO.println("Telefono: " + contacto.getTelefono());
            IO.println("------------------");
        }
    }
}
