<template>
  <UPageCard
    variant="naked"
    class="group max-w-120 rounded-2xl overflow-hidden bg-gradient-to-br dark:from-gray-900 dark:to-gray-800 border dark:border-gray-700/50"
    :ui="{ container: '!p-0' }"
  >
    <template #body>
      <div class="flex flex-col gap-4">
        <div class="flex flex-col items-start gap-4 p-4 pb-0">
          <div class="flex flex-col items-center w-full gap-2 min-w-0">
            <!-- Name -->
            <h2
              class="font-poppins font-semibold text-2xl tracking-tight text-highlighted truncate"
            >
              {{ character?.name }}
            </h2>
            <div class="flex flex-wrap gap-2">
              <!-- Alignment -->
              <UBadge
                v-if="character?.alignment"
                leading-icon="i-lucide-scale"
                variant="soft"
                color="neutral"
                :label="character?.alignment"
              />
              <!-- Faction -->
              <UBadge
                v-if="character?.faction"
                leading-icon="i-lucide-shield-half"
                variant="soft"
                color="tertiary"
                :label="character?.faction"
              />
            </div>
          </div>
          <!-- Character Image -->
          <div
            class="w-full h-60 shrink-0 rounded-lg overflow-hidden dark:bg-gray-800 border dark:border-gray-700 shadow-md"
          >
            <NuxtImg
              v-if="character?.image.hash"
              :src="character.image.hash"
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
        </div>

        <!-- Description -->
        <div class="mx-4">
          <div
            class="py-4 bg-elevated/50 rounded-lg w-full flex flex-col items-center"
          >
            <p
              class="text-center max-w-100 italic text-sm text-slate-300 leading-relaxed"
            >
              "{{ character?.description }}"
            </p>
          </div>
        </div>

        <!-- Stats -->
        <div class="grid grid-cols-4 gap-5 px-4">
          <!-- Attack -->
          <UPageCard
            variant="subtle"
            :spotlight="true"
            spotlight-color="primary"
            :ui="{
              container: '!py-3 !px-5 '
            }"
            class="col-span-1 h-fit w-full"
          >
            <div class="flex flex-col items-center size-full gap-1">
              <span
                class="text-sm font-medium uppercase tracking-wide text-gray-400"
                >ATK</span
              >
              <span class="font-bold text-lg !text-pink-400">{{
                character?.attack
              }}</span>
            </div>
          </UPageCard>
          <!-- Defense -->
          <UPageCard
            variant="soft"
            :spotlight="true"
            spotlight-color="primary"
            :ui="{
              container: '!py-3 !px-5 '
            }"
            class="col-span-1 h-fit w-full"
          >
            <div class="flex flex-col items-center size-full gap-1">
              <span
                class="text-sm font-medium uppercase tracking-wide text-gray-400"
                >DEF</span
              >
              <span class="font-bold text-lg !text-sky-400">{{
                character?.defense
              }}</span>
            </div>
          </UPageCard>
          <!-- Speed -->
          <UPageCard
            variant="soft"
            :spotlight="true"
            spotlight-color="primary"
            :ui="{
              container: '!py-3 !px-5 '
            }"
            class="col-span-1 h-fit w-full"
          >
            <div class="flex flex-col items-center size-full gap-1">
              <span
                class="text-sm font-medium uppercase tracking-wide text-gray-400"
                >SPD</span
              >
              <span class="text-lg font-bold !text-indigo-400">{{
                character?.speed
              }}</span>
            </div>
          </UPageCard>
          <!-- Luck -->
          <UPageCard
            variant="soft"
            :spotlight="true"
            spotlight-color="primary"
            :ui="{
              container: '!py-3 !px-5 '
            }"
            class="col-span-1 h-fit w-full"
          >
            <div class="flex flex-col items-center size-full gap-1">
              <span class="text-sm font-medium text-gray-400">LCK</span>
              <span class="text-lg font-bold !text-red-400">{{
                character?.luck
              }}</span>
            </div>
          </UPageCard>
        </div>

        <!-- Abilities (Expanded Descriptions) -->
        <div v-if="character" class="flex flex-col gap-4 p-4 pt-0">
          <div v-if="character.ability1_description" class="text-sm">
            <div class="flex flex-row gap-1 text-secondary items-center mb-2">
              <UIcon name="i-lucide-scroll" class="size-[16px]" />
              <span class="font-medium">{{ character.ability1 }}</span>
            </div>
            {{ character.ability1_description }}
          </div>
          <div v-if="character.ability2_description" class="text-sm">
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
