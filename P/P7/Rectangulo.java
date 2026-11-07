public class Rectangulo extends Figura {
    Rectangulo(double base, double altura){
        super(base, altura);
        this.base = base;
        this.altura = altura;
    }

    @Override 
    public double area(){
        return this.base * this.altura;
    }

    
}
