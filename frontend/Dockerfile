ARG NODE_VERSION=22.17.0
FROM node:${NODE_VERSION}-slim

# Enable pnpm
RUN npm install -g corepack@latest && corepack enable

WORKDIR /app

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy source code
COPY . .

# Build the application
RUN pnpm build

# Set production environment
ENV NODE_ENV=production

# Expose port
EXPOSE 3000

# Start the application
CMD ["node", ".output/server/index.mjs"]

