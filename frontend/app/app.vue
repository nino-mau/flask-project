<template>
  <UApp>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </UApp>
</template>

<script setup lang="ts">
const rc = useRuntimeConfig();

// const dataTwice = await $fetch(rc.public.apiBase + '/hello');
const data = await $fetch('/api/hello');
console.log(data);
</script>
