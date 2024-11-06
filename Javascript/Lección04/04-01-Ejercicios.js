//Ampliando el uso de var let y const
/* 
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
un error es que se sobreescriba
*/
/*
var nombre = 'Pablo';
nombre = 'Nicolas';
console.log(nombre);

function saludar(){
    var nombre = 'Natalia';
    console.log(nombre);
}
console.log(nombre); // El problema aqui es que no lee la variable de la funcion

if (true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo

/*
Let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una función
*/
/*
function saludar2(){
    let nombre2 = 'Pablo';
    console.log(nombre2);
}
if (true){
    let edad2 = 33;
    console.log(edad2)
}
//console.log(edad2);
*/
/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/
/*
const fechaNacimiento = 2006;
console.log(fechaNacimiento);
fechaNacimiento = 2003;
console.log(fechaNacimiento) //Solo se ejecuta el console anterior 
*/
//Ejercicio 1: Calcular estación del año

let mes = 6;
let estacion; //Undefined
if (mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if (mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño"
}
else if (mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor Incorrecto"
}
console.log("El valor corresponde a la estación de: "+estacion);

//Ejercicio 2: Hora del Día
let horaDia = 13;
let mensaje;
if(horaDia >= 0 && horaDia <= 9){
    mensaje = "durmiendo";
}
else if(horaDia >= 10 && horaDia <= 11){
    mensaje = "Desayunando";
}
else if(horaDia >= 12 && horaDia <= 15){
    mensaje = "Trabajando";
}
else if (horaDia >= 16 && horaDia <= 17){
    mensaje = "Almorzando";
}
else if (horaDia >= 18 && horaDia <= 20){
    mensaje = "Trabajando";
}
else if (horaDia >= 21 && horaDia <= 23){
    mensaje = "Descansando";
}
else{
    mensaje = "valor incorrecto";
}
console.log(mensaje);

// Estructura Switch(la sintaxis es igual a Java)
switch(mes){ //no solo se puede utilizar números, tambien cadenas
    case 1: case 2: case 12:
    estacion = "Verano"
    break;
    case 3: case 4: case 5:
    estacion = "Otoño"
    break;
    case 6: case 7: case 8:
    estacion = "Invierno"
    break;
    case 9: case 10: case 11:
    estacion = "Primavera"
    break;
    default:
        estacion = "Valor Incorrecto";
}
console.log("Bienvenido a la estación de: "+estacion)

//Ampliando el uso de var let y const
/*
con var puede reasignar en cualquier momento
este forma parte del ambito global
un error es que se sobreescriba
*/

var nombre = "Ariel";
nombre  = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia"
    console.log(nombre3);
}
//console.log(nombre3); //Aqui no lee el dato den la funcion


if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo


/*
let: esta puede ser reasiganada en cualquier momento
la difrerencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion 
*/

function saludar2(){
    let nombre2 = "Ariel";
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
const: se utiliza para valores constantes que no puede ser reasignadas
*/ 

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); // solo se ejecuta el console anterior

//Evitar repetir tu codigo
//Dry don't repeat yourself
//let days = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"];
let days = 4;
switch (days) {
    case 1:
        console.log("hoy es Lunes");
        break;
    case 2:
        console.log("hoy es Martes");
        break;
    case 3:
        console.log("hoy es Miercoles");
        break;
    case 4:
        console.log("hoy es Jueves");
        break;
    case 5:
        console.log("hoy es Viernes");
        break;
    case 6:
        console.log("hoy es Sabado");
        break;
    case 7:
        console.log("hoy es Domingo");
        break;
    
    default:
        console.log("Error en el ingreso del dia de la semana")
        break;
}
let days2 = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"];
function getDays(n){
    if(n < 1 || n > 7){
        throw new Error("out of range");
    }
    return days2[n-1];
}

console.log(getDays(5));

let mess = 6;
switch (mess) {
    case 1:
        console.log("El mes es Enero");
        break;
    case 2:
        console.log("El mes es Febrero");
        break;
    case 3:
        console.log("El mes es Marzo");
        break;
    case 4:
        console.log("El mes es Abril");
        break;
    case 5:
        console.log("El mes es Mayo");
        break;
    case 6:
        console.log("El mes es Junio");
        break;
    case 7:
        console.log("El mes es Julio");
        break;
    case 8:
        console.log("El mes es Agosto");
        break;
    case 9:
        console.log("El mes es Septiembre");
        break;
    case 10:
        console.log("El mes es Octubre");
        break;
    case 11:
        console.log("El mes es Noviembre");
        break;
    case 12:
        console.log("El mes es Diciembre");
        break;
    
    default:
        console.log("Error en el ingreso del mes del año");
        break;
}
let messs = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

function getMesss(n) {
    if (n < 1 || n > 12) {
        throw new Error("out of range");
    }
    return messs[n - 1];
}

console.log(getMesss(6)); // 