import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.ByteBuffer;

public class Archivos2 {

    public static void main(String[] args) {
        File archi = new File("archivo1");
        int a = 1;
        byte[] b = ByteBuffer.allocate(4).putInt(1).array(); 

        try {
            archi.createNewFile();
            
            DataOutputStream dos = new DataOutputStream(new FileOutputStream(archi));

            dos.writeInt(a);

            dos.close();

            //OutputStream os = new FileOutputStream(archi);
            //os.write(b);
            //os.close();

        } catch (IOException e) {
            System.out.println("Uppsi, no furulo");
        }

    }
}
