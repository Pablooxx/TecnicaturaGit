<script setup>
import { ref } from 'vue';
import FondoLineal from './FondoLineal.vue';

const intereses = ref([
    '* Me apasiona la Calidad: Como QA, mi rol principal es tratar de alcanzar la excelencia en los productos de software y en el cual doy mi maximo esfuerzo para que así sea',
    '* Me gusta aprender: En el rubro de la tecnología es escencial siempre estar en constante aprendizaje, por lo cual uno de mis puntos fuertes es la sed de conocimiento que tengo sobre mi profesión',
    '* Me gusta trabajar en equipo: Para mi, el trabajo en equipo es fundamental, ya que siempre es mejor tener alguien con quien compartir inquietudes, problemas y soluciones, donde todos juntos nos hacemos fuertes y mejoramos como individuos',
    '* Me gustan los desafios: Los desafios son la base fundamental del aprendizaje, donde cada uno sacamos lo mejor, nos ayudan a conocernos un poco mas y a aprender cosas nuevas',

]);
</script>

<template>
    <div class="intereses-contenedor">
        <FondoLineal />
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .intereses-contenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 80%;
    padding: 1rem;
}

.contenedor-lista {
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.1rem;
    text-shadow: 3px 3px 6px rgba(255, 255, 255, 0);
}

.item {
    margin-bottom: 1rem;
}
</style>
