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

    <CardCharacter ref="characterCard" :character="characterStore.character" />
    <div class="flex flex-row gap-5 mt-10">
      <!-- Button: Export -->
      <UButton
        size="xl"
        variant="solid"
        label="Export"
        icon="i-lucide-download"
        @click="exportCard()"
      />
      <!-- Button: Delete -->
      <UButton
        size="xl"
        variant="outline"
        color="error"
        icon="i-lucide-trash-2"
        label="Delete"
        @click="[characterStore.delete(characterId), navigateTo('/characters')]"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { toPng } from 'html-to-image';

const route = useRoute();
const characterStore = useCharacterStore();

const characterId = ref(route.params.id as string);
const characterCard = useTemplateRef('characterCard');

const exportCard = async () => {
  if (!characterCard.value?.$el) {
    console.error('[Export Card] Node is null');
  }
  const dataUrl = await toPng(characterCard.value?.$el);

  console.log(dataUrl);

  const link = document.createElement('a');
  link.download = 'character-card.png';
  link.href = dataUrl;
  link.click();
};

// Update character store
await characterStore.get(characterId.value);

const { exportElement } = useExportImage();
const save = () => exportElement(characterCard.value?.$el, 'png');
</script>
