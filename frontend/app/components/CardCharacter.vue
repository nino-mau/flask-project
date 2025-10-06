<template>
  <UPageCard
    variant="subtle"
    :highlight="true"
    highlight-color="primary"
    class="w-auto min-w-[350px] overflow-hidden max-w-[450px] h-fit rounded-2xl"
    :ui="{
      container: '!p-0'
    }"
  >
    <template #body>
      <div class="flex flex-col justify-start">
        <!-- Image -->
        <div class="h-[250px] w-full">
          <NuxtImg
            v-if="props.character?.image_hash"
            class="size-full contain-content"
            :src="props.character?.image_hash"
          />
          <!-- Placeholder -->
          <NuxtImg
            v-else
            class="size-full contain-content"
            src="https://placehold.co/600x400/png"
          />
        </div>
        <div class="flex flex-col gap-5 items-start p-4">
          <!-- Name -->
          <h1
            class="text-3xl font-poppins font-bold text-highlighted uppercase"
          >
            {{ props.character?.name }}
          </h1>
          <!-- Description -->
          <p class="text-pretty font-poppins italic">
            {{ props.character?.description }}
          </p>
          <div class="flex flex-col gap-5 items-start">
            <!-- Ability 1 -->
            <div class="flex flex-col gap-3">
              <UBadge
                size="xl"
                variant="soft"
                color="secondary"
                class="w-fit"
                :label="props.character?.ability1"
              />
              <p class="text-pretty font-poppins text-sm text-muted">
                {{ props.character?.ability1_description }}
              </p>
            </div>
            <!-- Ability 1 -->
            <div class="flex flex-col gap-3">
              <UBadge
                size="xl"
                variant="soft"
                color="primary"
                class="w-fit"
                :label="props.character?.ability2"
              />
              <p class="text-pretty font-poppins text-sm text-muted">
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
