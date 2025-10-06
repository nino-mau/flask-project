<template>
  <UPageCard
    variant="subtle"
    :highlight="true"
    highlight-color="primary"
    class="group w-auto min-w-[350px] overflow-hidden max-w-[550px] h-fit rounded-2xl transition-all duration-300 hover:shadow-2xl hover:scale-[1.02]"
    :ui="{
      container: '!p-0'
    }"
  >
    <template #body>
      <div class="flex flex-col justify-start">
        <div
          class="relative h-[300px] w-full overflow-hidden bg-gradient-to-br from-gray-100 to-gray-200 dark:from-gray-800 dark:to-gray-900"
        >
          <NuxtImg
            v-if="props.character?.image_hash"
            class="size-full object-cover"
            :src="props.character?.image_hash"
            :alt="props.character?.name || 'Character image'"
          />
          <NuxtImg
            v-else
            class="size-full object-cover transition-transform duration-500 group-hover:scale-110"
            src="https://placehold.co/600x400/png"
            alt="Character placeholder"
          />
          <div
            class="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
          />
        </div>

        <div class="flex flex-col gap-6 items-start p-6">
          <div class="w-full border-l-4 border-primary-500 pl-4 -ml-1">
            <!-- Character Name -->
            <h1
              class="text-3xl font-poppins font-bold text-gray-900 dark:text-white uppercase tracking-tight leading-tight"
            >
              {{ props.character?.name }}
            </h1>
          </div>

          <!-- Character Description -->
          <p
            class="text-pretty font-poppins text-gray-700 dark:text-gray-300 leading-relaxed"
          >
            {{ props.character?.description }}
          </p>

          <!-- <div -->
          <!--   class="w-full h-px bg-gradient-to-r from-transparent via-gray-300 dark:via-gray-700 to-transparent" -->
          <!-- /> -->

          <div class="flex flex-col gap-5 items-start w-full">
            <!-- Character Ability 1 -->
            <div
              class="group/ability flex flex-col gap-3 w-full p-4 rounded-xl bg-secondary-50/50 dark:bg-secondary-900/20 border border-secondary-200/50 dark:border-secondary-800/50 transition-all duration-200 hover:bg-secondary-100/70 dark:hover:bg-secondary-900/40 hover:border-secondary-300 dark:hover:border-secondary-700 hover:shadow-md"
            >
              <div class="flex items-center gap-2">
                <div
                  class="w-1.5 h-1.5 rounded-full bg-secondary-500 group-hover/ability:animate-pulse"
                />
                <UBadge
                  size="xl"
                  variant="soft"
                  color="secondary"
                  class="w-fit font-semibold"
                  :label="props.character?.ability1"
                />
              </div>
              <!-- Description -->
              <p
                class="text-pretty font-poppins text-sm text-gray-600 dark:text-gray-400 leading-relaxed pl-3.5"
              >
                {{ props.character?.ability1_description }}
              </p>
            </div>

            <!-- Character Ability 2 -->
            <div
              class="group/ability flex flex-col gap-3 w-full p-4 rounded-xl bg-primary-50/50 dark:bg-primary-900/20 border border-primary-200/50 dark:border-primary-800/50 transition-all duration-200 hover:bg-primary-100/70 dark:hover:bg-primary-900/40 hover:border-primary-300 dark:hover:border-primary-700 hover:shadow-md"
            >
              <div class="flex items-center gap-2">
                <div
                  class="w-1.5 h-1.5 rounded-full bg-primary-500 group-hover/ability:animate-pulse"
                />
                <UBadge
                  size="xl"
                  variant="soft"
                  color="primary"
                  class="w-fit font-semibold"
                  :label="props.character?.ability2"
                />
              </div>
              <!-- Description -->
              <p
                class="text-pretty font-poppins text-sm text-gray-600 dark:text-gray-400 leading-relaxed pl-3.5"
              >
                {{ props.character?.ability2_description }}
              </p>
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
</script>

<style scoped></style>
