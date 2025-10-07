<template>
  <div class="size-full flex items-center justify-center">
    <div class="flex flex-col gap-0 items-center justify-center">
      <UPageCTA
        v-if="!characterStore.isLoading"
        description="Generate a character rpg card from any image, powered by AI"
        variant="naked"
      >
        <template #title>
          <p class="text-5xl">
            Character Card <span class="grad-text-text1"> Generator </span>
          </p>
        </template>

        <UForm
          :schema="schema"
          :state="state"
          class="space-y-1 flex flex-col items-center"
          @submit="onSubmit"
        >
          <UFormField name="image">
            <UFileUpload
              v-model="state.image"
              size="xl"
              position="inside"
              layout="list"
              label="Drop your images here"
              description="SVG, PNG, JPG or GIF (max. 2MB)"
              accept="image/*"
              class="min-h-48"
            />
          </UFormField>

          <div class="flex flex-row gap-5 mt-15">
            <!-- Button: Submit -->
            <UButton
              type="submit"
              size="xl"
              variant="solid"
              icon="i-lucide-save"
              label="Submit"
            />
            <!-- Button: To Gallery -->
            <UButton
              size="xl"
              variant="outline"
              label="See Gallery"
              icon="i-lucide-image"
              to="/characters"
            />
          </div>
        </UForm>
      </UPageCTA>

      <LoadingMain v-else />
    </div>
  </div>
</template>

<script setup lang="ts">
import type { FormSubmitEvent } from '@nuxt/ui';
import * as z from 'zod';

// const isLoading = useState('isLoading', () => true);
const characterStore = useCharacterStore();

const MAX_FILE_SIZE = 2 * 1024 * 1024; // 2MB
const MIN_DIMENSIONS = { width: 50, height: 50 };
const MAX_DIMENSIONS = { width: 4096, height: 4096 };
const ACCEPTED_IMAGE_TYPES = [
  'image/jpeg',
  'image/jpg',
  'image/png',
  'image/webp'
];

const formatBytes = (bytes: number, decimals = 2) => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return (
    Number.parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i]
  );
};

const schema = z.object({
  image: z
    .instanceof(File, {
      message: 'Please select an image file.'
    })
    .refine((file) => file.size <= MAX_FILE_SIZE, {
      message: `The image is too large. Please choose an image smaller than ${formatBytes(MAX_FILE_SIZE)}.`
    })
    .refine((file) => ACCEPTED_IMAGE_TYPES.includes(file.type), {
      message: 'Please upload a valid image file (JPEG, PNG, or WebP).'
    })
    .refine(
      (file) =>
        new Promise((resolve) => {
          const reader = new FileReader();
          reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
              const meetsDimensions =
                img.width >= MIN_DIMENSIONS.width &&
                img.height >= MIN_DIMENSIONS.height &&
                img.width <= MAX_DIMENSIONS.width &&
                img.height <= MAX_DIMENSIONS.height;
              resolve(meetsDimensions);
            };
            img.src = e.target?.result as string;
          };
          reader.readAsDataURL(file);
        }),
      {
        message: `The image dimensions are invalid. Please upload an image between ${MIN_DIMENSIONS.width}x${MIN_DIMENSIONS.height} and ${MAX_DIMENSIONS.width}x${MAX_DIMENSIONS.height} pixels.`
      }
    )
});

type schema = z.output<typeof schema>;

const state = reactive<Partial<schema>>({
  image: undefined
});

async function onSubmit(event: FormSubmitEvent<schema>) {
  /**
   * Upload image
   */
  await characterStore.create(event.data.image);
  navigateTo(`/character/${characterStore.character?.id}`);
}
</script>

<style scoped></style>
