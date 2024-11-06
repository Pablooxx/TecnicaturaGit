
package Clase12Ejercicio1;

import java.util.Scanner;

public class Clase12Ejercicio1 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el numero total de horas: ");
        var horas = Integer.parseInt(entrada.nextLine());
        var dias = (horas / 24);
        var semanas = (dias / 7);
        var diasRes = (dias % 7);
        var horasRes = (horas % 24);
        System.out.println("Tiempo total = " + semanas + " Semanas" + " " + diasRes +" "+"Dias" + " " + horasRes + " " + "Horas");
    }

}
