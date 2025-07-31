# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY ./ /app/

ARG VITE_API_URL=${VITE_API_URL}

RUN npm run build


# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM caddy:alpine

WORKDIR /app

COPY Caddyfile ./

COPY --from=builder /app/dist/ ./dist

CMD ["caddy", "run", "--config", "Caddyfile", "--adapter", "caddyfile"]
