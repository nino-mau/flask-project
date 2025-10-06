<template>
  <div class="p-15">
    <UPageColumns>
      <CardCharacterSmall
        v-if="character.character"
        :character="character.character"
      />
      <CardCharacterSmall
        v-if="character.character"
        :character="character.character"
      />
      <CardCharacterSmall
        v-if="character.character"
        :character="character.character"
      />
      <CardCharacterSmall
        v-if="character.character"
        :character="character.character"
      />
      <CardCharacterSmall
        v-if="character.character"
        :character="character.character"
      />
    </UPageColumns>
  </div>
</template>

<script setup lang="ts">
const character = useCharacterStore();
</script>
