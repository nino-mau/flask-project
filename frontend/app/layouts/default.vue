<script setup lang="ts">
const isLoading = useState('isLoading', () => false);
</script>

<template>
  <div class="w-full h-screen flex flex-col">
    <div v-if="!isLoading" class="h-[100px]">
      <NavbarMain />
    </div>
    <div class="w-full grow">
      <slot />
    </div>
  </div>
</template>
