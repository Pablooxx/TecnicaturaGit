
import java.util.Scanner;


public class HolaMundo {

    public static void main(String[] args) {
        /* System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos Creciendo en programacion";
        System.out.println(miVariableCadena);
         */
        // var - Inferencia de tipos en Java
        /*
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos Estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tav
        //Reglas para definir una variable en Java
        //1-Usar tipo camelcase para las variables la primera letra en minuscula
         */
        /*
        var usuario = "Pablo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicio Caracteres Especiales con Java
        var nombre = "Nicolas";
        System.out.println("Nueva Linea: \n" + nombre); // Diagonal inversa y letra n
        System.out.println("Tabulador: \t" + nombre); //Tabulador, espacio para centrar
        System.out.println("\t.:Menu:.");
        System.out.println("Retroceso: \b"+nombre);//Caracter de Retroceso
        System.out.println("comillas simples: \'"+ nombre +"\'" );//contenido entre comillas simples
        System.out.println("comillas dobles: \""+nombre+"\"");//contenido entre comillas dobles
        */
        //Clase Scanner
        /*
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
        */
        /*byte numEnteroByte = (byte)127; //Maximo
        System.out.println("numEnteroByte: "+numEnteroByte);
        System.out.println("Valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor Maximo del Byte: "+ Byte.MAX_VALUE);
     
        short numEnteroShort = (short)127;  
        System.out.println("numEnteroShort: "+numEnteroShort);
        System.out.println("Valor minimo del Short: "+ Short.MIN_VALUE);
        System.out.println("Valor Maximo del Short: "+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;  
        System.out.println("numEnteroInt: "+numEnteroInt);
        System.out.println("Valor minimo del Int: "+ Integer.MIN_VALUE);
        System.out.println("Valor Maximo del Int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 2147483647;  
        System.out.println("numEnteroLong: "+numEnteroLong);
        System.out.println("Valor minimo del Long: "+ Long.MIN_VALUE);
        System.out.println("Valor Maximo del Long: "+ Long.MAX_VALUE);
        */
        /*
        float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de Float= "+ Float.MIN_VALUE);
        System.out.println("El valor maximo de Float= "+ Float.MAX_VALUE);
        
        double numDouble = 3.4028235E38;
        System.out.println("numFloat = " + numDouble);
        System.out.println("El valor minimo de Double = "+ Double.MIN_VALUE);
        System.out.println("El valor maximo de Double = "+ Double.MAX_VALUE);
        */
        /*
        // Inferencia de Tipos Var y tipos primitivos
        var numEntero = 20;//las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //automaticamente con el punto(del teclado númerico) se transforma en tipo doble
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0; 
        System.out.println("numDouble = " + numDouble);
        */
        //Tipos Primitivos Char
        /*
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024';//Indicamos a Java la asignación con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36 ;//Valor del juego de caracter especial de Unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';//asiganamos como tipo char en codigo duro
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024';//Indicamos a Java la asignación con el codigo unicode
        System.out.println("varCaracter = " + varCaracter1);
        var varCaracterDecimal1 = (char)36 ;//Asigna un valor entero
        System.out.println("varCaracterDecimal = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$';//asiganamos como tipo char en codigo duro
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int varCaractChar = 'b';
        System.out.println("varCaractChar = " + varCaractChar);
        */
        
        //Tipos Primitivos tipos booleanos
        /*
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es Verde");
        }
        else{
            System.out.println("La bandera es Roja");
        }
        
        // Algoritmo: es mayor de edad?
        var edad = 35;
        //var adulto = edad >= 18;
        if(edad >= 18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }
        */
        
        //Conversión de Tipos Primitivos
        /*
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPi = Double.parseDouble("3.1416");
        System.out.println("valorPi = " + valorPi);
        
        //Pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad: ");
        edad = Integer.parseInt(entrada.nextLine()); 
        System.out.println("edad = " + edad);
        */
        var entrada = new Scanner(System.in);
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        var fraseChar = "Programadores".charAt(3);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un Caracter: ");
        fraseChar = entrada.nextLine().charAt(10);
        System.out.println("fraseChar = " + fraseChar);
    
    }           
}
