
package Clase11Ejercicio3;

import java.util.Scanner;

public class Clase11Ejercicio3 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite dos numeros: ");
        var num1 = Integer.parseInt(entrada.nextLine());
        var num2 = Integer.parseInt(entrada.nextLine());
        
        if (num1 == num2){
            int resultado = num1 * num2;
            System.out.println("resultado = " + resultado);
        }
        else if (num1 > num2){
            int resultado = num1 - num2;
            System.out.println("resultado = " + resultado);
        }
        else{
            int resultado = num1 + num2;
            System.out.println("resultado = " + resultado);
        }
    }

}
