export interface Character {
  id: string;
  name: string;
  description: string;
  ability1: string;
  ability2: string;
  ability1_description: string;
  ability2_description: string;
  alignment: string;
  faction: string;
  attack: number;
  defense: number;
  speed: number;
  luck: number;
  image: {
    id: string;
    name: string;
    hash: string;
  };
  // Optional extended fields
  rarity?: number; // 1-5 scale
  role?: string; // e.g. Tank, Mage, Assassin
  stats?: {
    attack: number;
    defense: number;
    speed: number;
  };
  tags?: string[];
}
