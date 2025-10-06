<script setup lang="ts">
// const isLoading = useState('isLoading', () => false);
const characterStore = useCharacterStore();
</script>

<template>
  <div class="w-full h-screen flex flex-col">
    <div v-if="!characterStore.isLoading">
      <NavbarMain />
    </div>
    <div class="w-full relative grow">
      <slot />
    </div>
  </div>
</template>
