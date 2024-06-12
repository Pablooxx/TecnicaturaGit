// Tipos de Datos en Javascript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/
//Tipos de Objetos

var nombre = 'Pablo'; //Tipo str
console.log(nombre);

nombre = 7;
console.log(nombre);

nombre = 12.7;
console.log(nombre);

var numero = 3000; // Tipo num
console.log(numero);

var objeto = {  //Tipo objeto
    nombre : "Pablo",
    apellido: "Aparicio",
    telefono: "3816173497"
}
console.log(objeto);

//Tipo de dato Boolean
var bandera = true;
console.log(bandera);

// Tipo de dato Función 
function mifuncion(){};
console.log(typeof mifuncion);

// TIpo de Dato Symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato Clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log (typeof Persona)

// TIpo de dato undefined
var x;
console.log(x);

var x = undefined;
console.log(typeof x);

// null : sisgnifica ausencia de valor
var y = null; //null no es un tipo de dato, pero es tipo object
console.log(typeof y);

// Tipo de dato array y Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de datos es:

var z = '';
console.log(z) //Esto se refiere a que es una cadena vacía:
console.log(typeof z);

