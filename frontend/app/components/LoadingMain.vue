<template>
  <div :class="'relative ' + props.class">
    <Lottie width="400px" height="400px" name="loading-animation" />
    <div class="absolute top-80">
      <h1 class="text-2xl text-center font-bold text-highlighted">
        LOADING...
      </h1>
      <p class="text-center text-muted mt-4">
        Please be patient, your image is currently being processed.
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  class?: string;
}

const props = withDefaults(defineProps<Props>(), {
  class: 'mb-50'
});
</script>
