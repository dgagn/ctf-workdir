import java.security.MessageDigest;
import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.PBEParameterSpec;

public class Decrypter {
    public static String PWD = "We couldn't leak the password...";
    public static int COUNT = 11542142;

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage : java -jar stinkhorn_decrypter.jar <id>");
        } else {
            // la transaction a decrypter dans mycellium 
            String toDecrypt = "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";
            String id = args[0];
            id = id + "padddddd";
            id = id.substring(0, 8);
            try {
                // on lui passe le id passe en args    
                System.out.println(decrypt(toDecrypt, id));
            } catch (Exception e) {
                // ...
            }
        }
    }

    public static String decrypt(String data, String id) {
        byte[] decodedData = Base64.getDecoder().decode(data);
        try {
            String method = "PBEWithMD5AndDES";
            SecretKeyFactory kf = SecretKeyFactory.getInstance(method);
            PBEKeySpec keySpec = new PBEKeySpec(PWD.toCharArray());
            SecretKey key = kf.generateSecret(keySpec);
            Cipher cipher = Cipher.getInstance(method);
            PBEParameterSpec params = new PBEParameterSpec(id.getBytes(), COUNT);
            cipher.init(Cipher.DECRYPT_MODE, key, params);
            return new String(cipher.doFinal(decodedData));
        } catch (Exception var10) {
            throw new RuntimeException(var10.getMessage());
        }
    }
}