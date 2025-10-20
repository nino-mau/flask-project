<template>
  <div class="max-w-7xl mx-auto px-8 py-10 flex flex-col gap-8">
    <!-- Grid -->
    <TransitionGroup
      v-if="charactersStore.characters"
      :key="$route.path"
      name="flip"
      tag="ul"
      class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
      appear
    >
      <li
        v-for="(character, index) in charactersStore.characters"
        :key="character.id || index"
        :style="{ transitionDelay: `${Math.floor(index / 2) * 150}ms` }"
      >
        <CardCharacterSmall :character="character" />
      </li>
    </TransitionGroup>

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
    </div>
  </div>
</template>

<script setup lang="ts">
const charactersStore = useCharactersStore();
charactersStore.get();
</script>

<style scoped></style>
