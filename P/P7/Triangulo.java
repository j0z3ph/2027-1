public class Triangulo {
    private double base;
    private double altura;

    Triangulo(double base, double altura){
        this.base = base;
        this.altura = altura;
    }

    public double area() {
        return (this.base * this.altura) / 2.0;
    }

    public double getBase() {
        return base;
    }
    public void setBase(double base) {
        this.base = base;
    }
    public double getAltura() {
        return altura;
    }
    public void setAltura(double altura) {
        this.altura = altura;
    }
    

}
