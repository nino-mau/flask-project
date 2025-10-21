ARG NODE_VERSION=22.17.0
FROM node:${NODE_VERSION}-slim

# Enable pnpm
ENV PNPM_HOME="/pnpm"
ENV PATH="${PNPM_HOME}:$PATH"
RUN corepack enable

# Use existing node user
USER node
WORKDIR /home/node/app

# Copy package files with proper ownership
COPY --chown=node:node package.json pnpm-lock.yaml ./

# Install dependencies as node
RUN pnpm install --frozen-lockfile

# Copy rest of app files as node
COPY --chown=node:node . .

ENV NODE_ENV=development
EXPOSE 3000

CMD ["pnpm", "run", "dev"]

