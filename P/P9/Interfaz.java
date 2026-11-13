public interface Interfaz {
    
    void abstracto();

    default void metodo() {
        System.out.println("Hola");
    }
}
