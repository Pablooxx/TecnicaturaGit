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
