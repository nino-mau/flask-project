<template>
  <NuxtLink
    :to="`/character/${character?.id}`"
    class="group relative block rounded-2xl overflow-hidden bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 border border-gray-200/50 dark:border-gray-700/50 hover:border-primary-400/50 dark:hover:border-primary-500/50 transition-all duration-300 hover:shadow-xl hover:-translate-y-1"
  >
    <div
      class="absolute inset-0 bg-gradient-to-tr from-primary-500/0 via-primary-400/0 to-primary-300/0 group-hover:from-primary-500/10 group-hover:via-primary-400/5 group-hover:to-transparent transition-all duration-500"
    />

    <div class="flex flex-col gap-4">
      <div class="relative flex flex-row items-center gap-3 pb-0 p-3">
        <div
          class="relative w-16 h-16 shrink-0 rounded-xl overflow-hidden ring-2 ring-gray-200 dark:ring-gray-700 group-hover:ring-primary-400 dark:group-hover:ring-primary-500 transition-all duration-300"
        >
          <NuxtImg
            v-if="character?.image?.hash"
            :src="character.image.hash"
            :alt="character?.name || 'Character image'"
            class="size-full object-cover transition-transform duration-500"
          />
          <NuxtImg
            v-else
            src="https://placehold.co/300x300/png"
            alt="Placeholder"
            class="size-full object-cover group-hover:scale-110 transition-transform duration-500"
          />
          <div
            class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
          />
        </div>

        <div class="flex-1 min-w-0 space-y-2">
          <h3
            class="font-poppins font-bold text-base text-gray-900 dark:text-white truncate group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors duration-200"
          >
            {{ character?.name }}
          </h3>

          <div class="flex items-center gap-1.5 flex-row">
            <UBadge
              v-if="character?.alignment"
              leading-icon="i-lucide-scale"
              variant="subtle"
              color="neutral"
              :label="character?.alignment"
            />
            <!-- <UBadge -->
            <!--   v-if="character?.faction" -->
            <!--   leading-icon="i-lucide-castle" -->
            <!--   variant="soft" -->
            <!--   color="tertiary" -->
            <!--   :label="character?.faction" -->
            <!-- /> -->
          </div>
        </div>
      </div>

      <!-- <UIcon -->
      <!--   name="i-lucide-chevron-right" -->
      <!--   class="size-5 text-gray-400 group-hover:text-primary-500 group-hover:translate-x-1 transition-all duration-300" -->
      <!-- /> -->

      <div class="grid grid-cols-4 gap-0">
        <div
          class="p-4 flex flex-col items-center ring ring-default size-full gap-1"
        >
          <span class="text-xs uppercase tracking-wide text-gray-400">ATK</span>
          <span class="font-semibold text-sm">{{ character?.attack }}</span>
        </div>
        <div
          class="p-4 flex flex-col items-center ring ring-default size-full gap-1"
        >
          <span class="text-xs uppercase tracking-wide text-gray-400">DEF</span>
          <span class="font-semibold text-sm">{{ character?.defense }}</span>
        </div>
        <div
          class="p-4 flex flex-col items-center ring ring-default size-full gap-1"
        >
          <span class="text-xs uppercase tracking-wide text-gray-400">SPD</span>
          <span class="font-semibold text-sm">{{ character?.speed }}</span>
        </div>
        <div
          class="p-4 flex flex-col items-center ring ring-default size-full gap-1"
        >
          <span class="text-xs uppercase tracking-wide text-gray-400">LCK</span>
          <span class="font-semibold text-sm">{{ character?.luck }}</span>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup lang="ts">
import type { Character } from '~/types/character';

interface Props {
  character?: Character;
}

const props = defineProps<Props>();
const { character } = toRefs(props);
</script>
