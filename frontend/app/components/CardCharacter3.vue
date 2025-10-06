<template>
  <UPageCard
    variant="subtle"
    :highlight="false"
    class="w-fit max-w-[500px] rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm"
    :ui="{ container: '!p-0' }"
  >
    <template #body>
      <div class="flex flex-col gap-4">
        <!-- Image / Name Row -->
        <div class="flex items-start gap-4 p-4 pb-0">
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

        <!-- Description -->
        <p class="px-4 italic text-base leading-relaxed">
          {{ character?.description }}
        </p>

        <!-- Abilities (Expanded Descriptions) -->
        <div v-if="character" class="flex flex-col gap-4 p-4 pt-0">
          <div v-if="character.ability1_description" class="text-sm text-muted">
            <div class="flex flex-row gap-1 text-secondary items-center mb-2">
              <UIcon name="i-lucide-sword" class="size-[16px]" />
              <span class="font-medium">{{ character.ability1 }}</span>
            </div>
            {{ character.ability1_description }}
          </div>
          <div v-if="character.ability2_description" class="text-sm text-muted">
            <div class="flex flex-row gap-1 text-primary items-center mb-2">
              <UIcon name="i-lucide-scroll" class="size-[16px]" />
              <span class="font-medium">{{ character.ability2 }}</span>
            </div>
            {{ character.ability2_description }}
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
