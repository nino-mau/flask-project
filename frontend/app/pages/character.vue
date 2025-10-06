<template>
  <div class="size-full flex items-center justify-center">
    <CardCharacter3
      v-if="character.character"
      :character="character.character"
    />
  </div>
</template>

<script setup lang="ts">
const character = useCharacterStore();
</script>
