<template>
  <UHeader>
    <template #title>
      <div class="flex flex-row items-center gap-1">
        <IconSite :width="35" :height="35" color="var(--color-primary)" />
        <p class="text-xl text-highlighted font-bold">Card Generator</p>
      </div>
    </template>
    <template #right>
      <div class="flex flex-row gap-9">
        <ULink as="button" to="/">Home</ULink>
        <ULink as="button" to="/characters">Characters</ULink>
        <ULink as="button">About</ULink>
      </div>
    </template>
  </UHeader>
</template>

<script setup lang="ts"></script>
