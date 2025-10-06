export interface Character {
  id: string;
  name: string;
  description: string;
  ability1: string;
  ability2: string;
  ability1_description: string;
  ability2_description: string;
  image: {
    id: string;
    name: string;
    hash: string;
  };
}
