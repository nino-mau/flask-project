<template>
  <UHeader>
    <template #title>
      <UIcon name="i-lucide-trello" class="size-6 text-primary" />
      <p class="text-xl text-highlighted font-bold">MySite</p>
    </template>
    <template #right>
      <div class="flex flex-row gap-9">
        <ULink as="button">Home</ULink>
        <ULink as="button">Characters</ULink>
        <ULink as="button">About</ULink>
      </div>
    </template>
  </UHeader>
</template>

<script setup lang="ts"></script>
