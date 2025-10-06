import type { Character } from '~/types/character';

export const useCharacterStore = defineStore('characterStore', {
  state: () => ({ character: null as Character | null, isLoading: false }),
  getters: {},
  actions: {
    async create(image: File) {
      const formData = new FormData();
      formData.append('file', image);

      try {
        this.isLoading = true;
        const data = await $fetch.raw('/api/character', {
          method: 'POST',
          body: formData
        });

        // Add character to store
        this.character = data._data.character;
        console.log(data);
      } finally {
        this.isLoading = false;
      }
    },

    async get(characterId: string) {
      const toast = useToast();
      const data = await $fetch.raw(
        `/api/character?character_id=${characterId}`
      );
      console.log(data);

      if (data.status !== 200) {
        toast.add({
          title: 'Failed to fetch character',
          color: 'error',
          icon: 'i-lucide-circle-x'
        });
        return;
      }

      // Add character to store
      this.character = data._data.character;
      console.log(data);
    },

    async delete(characterId: string) {
      const toast = useToast();
      const data = await $fetch.raw(
        `/api/character?character_id=${characterId}`,
        { method: 'DELETE' }
      );
      console.log(data);

      if (data.status !== 200) {
        toast.add({
          title: 'Failed to delete character',
          color: 'error',
          icon: 'i-lucide-circle-x'
        });
        return;
      }

      toast.add({
        title: 'Succesfully deleted character',
        color: 'success',
        icon: 'i-lucide-circle-check-big'
      });
      // Remove character from store
      this.character = null;
      console.log(data);
    }
  }
});
