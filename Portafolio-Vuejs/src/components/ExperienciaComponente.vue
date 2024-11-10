<script setup>
import icono2 from '/src/assets/programmer-svgrepo-com.svg';
import icono1 from '/src/assets/quality-premium-certificate-svgrepo-com.svg'
import { ref } from 'vue';
const titulo = 'Quality Control Analyst';
const fecha = '2022-Actualmente';
const experiencias = ref([
    { id: 1, src: icono1, parrafo: 'Llevo mas de 2 años ejerciendo la profesión en la cual encontré mi pasión.' },
    { id: 2, src: icono2, parrafo: 'Entre las principales tareas de mi puesto esta la de realizar pruebas de software para los requerimientos, que esto nos lleva al como hago esto? En primera medida realizando análisis del requerimiento, creando datos de pruebas, creando casos de pruebas, planes de pruebas. La documentación para la clara compresión de las modificaciones que se realizaron en el requerimiento y al final de todo la "DEMO" que es una presentación al cliente sobre las modificaciones que se realizaron bajo el requerimiento.'}
]);
</script>

<template>
<div class="card">
        <h3 class="titulo">{{titulo.toLocaleUpperCase()}}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experencia in experiencias" :key="experencia.id">
                <img class="imagen-svg" :src="experencia.src" width="45rem" :alt="experencia.parrafo">
                <p>{{ experencia.parrafo }}</p>
            </li>
        </ul>
    </div>

</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: rgb(51, 51, 51);
    border-radius: 15px;
}

.titulo {
    font-size: 1.5rem;
    color: rgb(247, 247, 247);
}

.fecha {
    font-size: 1rem;
    color: hsla(160, 100%, 37%, 0.2);
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
}

.item {
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>
