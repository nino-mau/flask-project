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

        // Add data to store
        this.character = data._data.character;
        console.log(data);
      } finally {
        this.isLoading = false;
      }
    }
  }
});
