var nombre = 'Pablo';
var apellido = ' Aparicio';
var nombreCompleto = nombre+' '+apellido; //Primera Concatenación
console.log(nombreCompleto);
var nombreCompleto2 = 'Pablo'+' '+'Paez'//Segunda Concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izq a der siguiendo la cadena lee el número como string
console.log(juntos)
juntos = nombre + (78 + 17);// Lee primero el nombre y luego de la suma
console.log(juntos);
juntos = 78 + 17 + nombre
console.log(juntos) // Contexto String o Contexto Cadena


nombre += apellido; //Concatenamos usando el operador simplificado
console.log(nombre);

// hoy ya no se usa varm se utiliza let y const
let nombre2 = 'Nicolas';
console.log(nombre2);

const apellido2 = 'Paez';
//apellido2 = 'Paez'; una constante no puede ser modificada
console.log(apellido2);

let x,  y; // Se pueden crear varias variables dentro de una misma línea
x = 18, y = 21; // Se puede hacer asignación de varias variables dentro de la misma línea
let z = x + y; // Se asigna el valor de la operación
console.log(z)

 let _1num = 31; // No utilizar número como primer caracter de una variable
 let rompiendo = 'rompe'; // No utilizar palabras reservadas para una variable
 console.log(_1num);
 console.log(rompiendo);
