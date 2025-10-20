import type { Character } from '~/types/character';

export const useCharactersStore = defineStore('charactersStore', {
  state: () => ({
    characters: null as Character[] | null,
    isLoading: false
  }),
  getters: {},
  actions: {
    async get() {
      const toast = useToast();
      const data = await $fetch.raw(`/api/characters`);
      console.log(data);

      if (data.status !== 200) {
        toast.add({
          title: 'Failed to fetch character',
          color: 'error',
          icon: 'i-lucide-circle-x'
        });
        return;
      }

      // Add characters to store state
      this.characters = data._data.characters;
      console.log(data);
    }
  }
});
