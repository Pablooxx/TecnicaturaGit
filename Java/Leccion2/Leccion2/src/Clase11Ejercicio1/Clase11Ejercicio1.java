
package Clase11Ejercicio1;

import java.util.Scanner;

public class Clase11Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite las notas: ");
        var nota1 = Float.parseFloat(entrada.nextLine());
        var nota2 = Float.parseFloat(entrada.nextLine());
        var nota3 = Float.parseFloat(entrada.nextLine());
        var promedio = ((nota1 + nota2 + nota3)/3);
        System.out.println("promedio = " + promedio);
    }

}
