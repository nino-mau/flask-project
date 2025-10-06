<template>
  <div class="size-full flex items-center justify-center">
    <!-- <CardCharacter -->
    <!--   v-if="character.character" -->
    <!--   :character="character.character" -->
    <!-- /> -->

    <CardCharacter2 :character="testData" />
  </div>
</template>

<script setup lang="ts">
const testData = {
  ability1: 'Expert Instruction',
  ability1_description:
    'Professor Blackwood possesses an unparalleled ability to explain complex concepts clearly and effectively, guiding students to understanding through engaging demonstrations and detailed explanations.',
  ability2: 'Historical Knowledge',
  ability2_description:
    'With a lifetime dedicated to studying history, Professor Blackwood has an encyclopedic knowledge of the past, allowing him to provide insightful context and analysis to any situation.',
  description:
    'A wise and experienced educator, known for his knowledge and patience.',
  id: '509de93e-257d-4071-9331-36510e561f00',
  image_hash:
    'https://res.cloudinary.com/ddvhq6txv/image/upload/v1759736309/flask_app_uploads/5eb55149a9981-elderly-teacher-with-moustache-cartoon-character2.jpg.jpg',
  image_id: '2c5116d4-3ae0-4e61-b860-41bea1d1d15d',
  name: 'Professor Silas Blackwood'
};

const character = useCharacterStore();
</script>

<style scoped></style>
