<template>
  <div class="max-w-7xl mx-auto px-6 py-10 flex flex-col gap-8">
    <!-- Content -->
    <transition name="fade" mode="out-in">
      <!-- Loading Skeletons -->
      <div
        v-if="pending"
        key="loading"
        class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
      >
        <div
          v-for="n in 8"
          :key="n"
          class="rounded-xl border border-gray-200 dark:border-gray-800 p-4 flex flex-col gap-4"
        >
          <USkeleton class="w-20 h-20 rounded-lg" />
          <USkeleton class="h-5 w-3/4" />
          <div class="flex gap-2">
            <USkeleton class="h-5 w-16" />
            <USkeleton class="h-5 w-20" />
          </div>
        </div>
      </div>

      <!-- Grid -->
      <div
        v-else-if="characters.length"
        key="grid"
        class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
      >
        <CardCharacterSmall
          v-for="(character, index) in characters"
          :key="character.id || index"
          :character="character"
        />
      </div>

      <!-- Empty State -->
      <div
        v-else
        key="empty"
        class="flex flex-col items-center justify-center py-24 gap-4"
      >
        <UIcon
          name="i-lucide-user-x"
          class="size-12 text-gray-400 dark:text-gray-600"
        />
        <p class="text-center max-w-sm text-gray-500 dark:text-gray-400">
          No characters match your search.
        </p>
        <UButton
          variant="soft"
          color="primary"
          icon="i-lucide-undo-2"
          @click="clearSearch"
          >Reset filters</UButton
        >
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
const search = ref('');
const sortKey = ref('name-asc');

const { data, pending, error, refresh } = await useAsyncData('characters', () =>
  $fetch('/api/characters')
);

const characters = computed(() => data.value?.characters || []);

const errorMessage = computed(() => {
  if (!error.value) return '';
  return (error.value as any)?.message || 'Unknown error';
});

function clearSearch() {
  search.value = '';
  sortKey.value = 'name-asc';
  refresh();
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
