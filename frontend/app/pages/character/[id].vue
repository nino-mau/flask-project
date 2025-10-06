<template>
  <div class="size-full flex flex-col items-center justify-center">
    <CardCharacter3
      v-if="characterStore.character"
      :character="characterStore.character"
    />
    <div class="flex flex-row gap-5 mt-15">
      <UButton
        size="xl"
        variant="solid"
        label="Export"
        icon="i-lucide-download"
      />
      <UButton
        size="xl"
        variant="subtle"
        color="error"
        icon="i-lucide-trash-2"
        label="Delete"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();
const characterStore = useCharacterStore();

console.log(route.params);

if (route.params.id && typeof route.params.id === 'string') {
  await characterStore.get(route.params.id);
  console.log(characterStore.character);
}
</script>
