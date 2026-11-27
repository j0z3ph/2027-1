public class NoVerificada {
    public static void main(String[] args) throws Exception {
        try {
            System.out.println(5/0);
        } catch (ArithmeticException e) {
            IO.println("Upssss, que tontito, no se puede dividir entre cero 😹");
            throw new Exception("LOL");
        }
        
    }
}
