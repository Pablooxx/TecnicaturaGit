
package Clase11Ejercicio2;

import java.util.Scanner;


public class Clase11Ejercicio2 {
        public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la cantidad a pagar: ");
        var compra = Float.parseFloat(entrada.nextLine());
        
        if (compra > 100){
            float compraDes = compra*0.2F;
            System.out.println("compra = " + (compra - compraDes));
        }
        else
            System.out.println("compra = " + compra);
    }

}
