
package Clase12Ejercicio3;

import java.util.Scanner;

public class Clase13Ejercicio3 {
        public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese la calificacion de participacion (10%): ");
        double participacion = Double.parseDouble(entrada.nextLine());

        System.out.print("Ingrese la calificacion del primer examen parcial (25%): ");
        double primerParcial = Double.parseDouble(entrada.nextLine());

        System.out.print("Ingrese la calificacion del segundo examen parcial (25%): ");
        double segundoParcial = Double.parseDouble(entrada.nextLine());

        System.out.print("Ingrese la calificacion del examen final (40%): ");
        double examenFinal = Double.parseDouble(entrada.nextLine());
        
        double calificacionFinal = (participacion * 0.10) + (primerParcial * 0.25) + (segundoParcial * 0.25) + (examenFinal * 0.40);
        System.out.println("La calificacion final del estudiante es: " + calificacionFinal);
    }

}
