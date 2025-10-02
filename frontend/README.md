# Custom Nuxt Starter

A starter template for building applications with Nuxt 4, Vue 3, Pinia and postgres. This repository includes a basic project structure, config for fonts and CSS, tooling (ESLint, Prettier, Stylelint), and Docker development helpers.

- Framework: Nuxt 4
- UI Kit: @nuxt/ui
- State: Pinia
- Database: Postgres
- ORM: Drizzle

## Quick Start

Prerequisites:

- Node.js (22 recommended)
- pnpm (recommended) or npm/yarn
- Docker & docker compose

Install dependencies:

```bash
pnpm install
# or
npm install
```

Start container:

```bash
docker compose up --build -d
```

Open <https://localhost:3000> in your browser.

Once finished, stop the container with:

```bash
docker compose down
```

## Directory Structure

- `app/` — Nuxt application source (pages, components, `app.vue`, `assets/`).
- `app/assets/` — styles, images and other static assets used by the app.
- `public/` — static files served at the site root (favicon, `robots.txt`, etc.).
- `nuxt.config.ts` — Nuxt configuration and modules.
- `package.json` — project scripts and dependencies.
- `docker-compose.yml` & `Dockerfile.dev` — development Docker setup.
- `README.md`, `.gitignore`, `tsconfig.json` — repository metadata and tooling config.
