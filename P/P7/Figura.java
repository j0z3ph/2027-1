public abstract class Figura {
    protected  double base;
    protected  double altura;

    Figura(double base, double altura){
        this.base = base;
        this.altura = altura;
    }

    /**
     * Favor de ponerle su formula a cada uno ;)
     * @return
     */
    public abstract double area();

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
