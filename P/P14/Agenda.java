import java.util.ArrayList;

public class Agenda {
    private ArrayList<Contacto> lista;

    public Agenda() {
        this.lista = new ArrayList<>();
    }

    void agregarContacto(Contacto contacto) {
        this.lista.add(contacto);
    }

    void eliminarContacto(String telefono) {
        for (Contacto contacto : this.lista) {
            if (contacto.getTelefono().equals(telefono)) {
                this.lista.remove(contacto);
                break;
            }
        }
    }

    /**
     * Busca un contacto por nombre
     * 
     * @param nombre El nombre del contacto a buscar
     * @return Null si no se encuentra, Contacto en calquier otro caso.
     */
    Contacto buscarContactoXNombre(String nombre) {
        for (Contacto contacto : this.lista) {
            if (contacto.getNombre().equals(nombre)) {
                return contacto;
            }
        }
        return null;
    }

    /**
     * Busca un contacto por nombre
     * 
     * @param telefono El nombre del contacto a buscar
     * @return Null si no se encuentra, Contacto en calquier otro caso.
     */
    Contacto buscarContactoXTelefono(String telefono) {
        for (Contacto contacto : this.lista) {
            if (contacto.getTelefono().equals(telefono)) {
                return contacto;
            }
        }
        return null;
    }

    ArrayList<Contacto> listar() {
        return this.lista;
    }
}
