<template>
  <UPageCard
    variant="subtle"
    class="size-fit rounded-xl hover:scale-105 transition-transform duration-500 overflow-hidden"
    :ui="{ container: '!p-0' }"
  >
    <template #body>
      <div class="flex flex-col gap-4">
        <!-- Image / Name Row -->
        <div class="flex items-start gap-4 p-4">
          <div
            class="w-25 h-25 shrink-0 rounded-lg overflow-hidden bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700"
          >
            <NuxtImg
              v-if="character?.image_hash"
              :src="character.image_hash"
              :alt="character?.name || 'Character image'"
              class="size-full object-cover"
            />
            <NuxtImg
              v-else
              src="https://placehold.co/300x300/png"
              alt="Placeholder"
              class="size-full object-cover"
            />
          </div>
          <div class="flex flex-col gap-1 min-w-0">
            <!-- Character Name -->
            <h2
              class="font-poppins font-semibold text-2xl tracking-tight text-highlighted truncate"
            >
              {{ character?.name }}
            </h2>
            <div class="flex flex-wrap gap-2">
              <UBadge
                v-if="character?.ability1"
                leading-icon="i-lucide-sword"
                variant="soft"
                color="secondary"
                :label="character?.ability1"
              />
              <UBadge
                v-if="character?.ability2"
                leading-icon="i-lucide-scroll"
                variant="soft"
                color="primary"
                :label="character?.ability2"
              />
            </div>
          </div>
        </div>
      </div>
    </template>
  </UPageCard>
</template>

<script setup lang="ts">
import type { Character } from '~/types/character';

interface Props {
  character?: Character;
}

const props = defineProps<Props>();
const { character } = toRefs(props);
</script>

<style scoped></style>
