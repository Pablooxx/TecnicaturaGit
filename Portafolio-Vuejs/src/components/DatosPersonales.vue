<script setup>
const title = 'Pablo Aparicio';
const descripcion = 'Quality Assurance - UTN';
const residencia = 'San Miguel de Tucumán, Tucumán, Argentina';
const presentacion = 'Hola, Bienvenido a mi portafolio de proyectos. Soy un Quality Assurance que esta aprendiendo programación en la UTN.';
const redesSociales = [
  { id: 1, name: 'linkedin', src: '/src/assets/linkedin_icon.svg', url: 'https://www.linkedin.com/in/pabloaparicio7/' },
  { id: 2, name: 'instagram', src: '/src/assets/instagram_icon.svg', url: 'https://www.instagram.com/pabloaparicio7/' },
  { id: 3, name: 'github', src: '/src/assets/github_icon.svg', url: 'https://github.com/Pablooxx' },
  { id: 4, name: 'curriculum', src: '/src/assets/cv_resume_icon.svg', url: '' }
];
const telefono = '+54 9 381-6173497';

</script>

<template>
<section class="datos-personales">
  <div class="card">
    <h1>{{ title }}</h1>
    <h2>{{ descripcion }}</h2>
    <p>{{ presentacion }}</p>
    <ul class="container-lista">
      <li v-for="red in redesSociales" :key="red.id">
        <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
      </li>
    </ul>
    <h3>📞 Mi Teléfono personal: {{ telefono }}</h3>
    <h4>{{ residencia }}</h4>
  </div>
</section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card {
  background-color: rgb(61, 61, 61);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(219, 219, 219, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(255, 255, 255);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}
</style>
