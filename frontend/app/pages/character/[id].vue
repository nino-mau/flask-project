<template>
  <div
    v-if="characterStore.character"
    class="size-full flex flex-col items-center justify-center"
  >
    <!-- Button: Back to Gallery -->
    <UButton
      size="xl"
      variant="soft"
      to="/characters"
      label="Back to Gallery"
      icon="i-lucide-arrow-left"
      class="absolute top-5 left-5"
    />

    <CardCharacter3 :character="characterStore.character" />
    <div class="flex flex-row gap-5 mt-15">
      <!-- Button: Export -->
      <UButton
        size="xl"
        variant="solid"
        label="Export"
        icon="i-lucide-download"
      />
      <!-- Button: Delete -->
      <UButton
        size="xl"
        variant="subtle"
        color="error"
        icon="i-lucide-trash-2"
        label="Delete"
        @click="[characterStore.delete(characterId), navigateTo('/characters')]"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();
const characterStore = useCharacterStore();

const characterId = ref(route.params.id as string);

// Update character store
await characterStore.get(characterId.value);
</script>
