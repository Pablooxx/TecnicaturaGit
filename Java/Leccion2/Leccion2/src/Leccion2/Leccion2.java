
package Leccion2;

import java.util.Scanner;


public class Leccion2 {
    public static void main(String[] args) {
        var condicion = true;
        if(condicion){
            System.out.println("Condicion Verdadera");//Condicional Simple
            
        }
        else{
            System.out.println("Condicion Falsa"); //Condicional Doble
        }
        /*
        var numero = 10;
        var numeroTexto = "Numero Desconocido";
        if(numero == 1)
            numeroTexto = "Numero uno";
        else if(numero == 2)
            numeroTexto = "Numero Dos";
        else if (numero == 3)
            numeroTexto = "Numero Tres";
        else if (numero == 4)
            numeroTexto = "Numero Cuatro";
        else
            numeroTexto = "Numero no encontrado";
        System.out.println("numeroTexto = " + numeroTexto);
        */
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch (numero){
            case 1:
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;    
            case 3:
                numeroTexto = "Numero Tres";
                break;
            case 4:
                numeroTexto = "Numero Cuatro";
                break;
            default:    
                numeroTexto = "Caso no Encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
        
        
    }
}
