<template>
  <div
    v-if="characterStore.character"
    class="size-full flex flex-col items-center justify-center"
  >
    <UModal v-model:open="screenshotModalOpen" :dismissible="true">
      <template #body>
        <div class="flex flex-col items-center w-full gap-5">
          <NuxtImg v-if="screenshotUrl" class="size-fit" :src="screenshotUrl" />
          <UButton
            size="xl"
            label="Download"
            icon="i-lucide-download"
            @click="screenshotWrapper()"
          />
        </div>
      </template>
    </UModal>

    <!-- Button: Back to Gallery -->
    <UButton
      size="xl"
      variant="soft"
      to="/characters"
      label="Back to Gallery"
      icon="i-lucide-arrow-left"
      class="absolute top-5 left-5"
    />

    <div id="card_character" class="card_character">
      <CardCharacter
        id="card_character"
        ref="characterCard"
        :character="characterStore.character"
      />
    </div>
    <div class="flex flex-row gap-5 mt-10">
      <!-- Button: Download -->
      <UButton
        :loading="characterStore.isScreenshotLoading"
        size="xl"
        variant="solid"
        label="Download"
        icon="i-lucide-download"
        @click="screenshotWrapper()"
      />
      <!-- Button: Delete -->
      <UButton
        size="xl"
        variant="outline"
        color="error"
        icon="i-lucide-trash-2"
        label="Delete"
        @click="
          async () => {
            await characterStore.delete(characterId);
            navigateTo('/characters');
          }
        "
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();
const characterStore = useCharacterStore();

const characterId = ref(route.params.id as string);

const screenshotModalOpen = ref(false);
const screenshotUrl = ref<undefined | string>(undefined);

const screenshotWrapper = async () => {
  const res = await characterStore.screenshot(characterId.value);
  screenshotUrl.value = res;
  downloadFile(res);
};

const downloadScreenshot = () => {
  if (screenshotUrl.value) {
    downloadFile(screenshotUrl.value);
  }
};

defineShortcuts({
  o: () => (screenshotModalOpen.value = !screenshotModalOpen.value)
});

// Update character store
await characterStore.get(characterId.value);
</script>
