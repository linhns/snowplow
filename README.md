# snowplow

A poor man's web application for generating unique Snowflake IDs using a custom
backend.

Both frontend and backend are public-facing, frontend can be reached at **/**,
while backend can be reached at **/api**

Visit the live demo at: [Demo](https://snowplow.up.railway.app/)

## 🚀 Tech Stack

### Frontend

- **React** + **Vite** with plain **CSS**
- Communicates with the backend API to fetch generated Snowflake IDs

### Backend

- **Python** with **FastAPI**
- Implements the Snowflake ID generation algorithm

### Hosting

- **Railway** is used for hosting both frontend and backend services based on
  Docker images

## 📂 Project Structure

```text
    project-root/
    ├── backend/     # FastAPI app for Snowflake ID generation
    ├── frontend/    # Static HTML, CSS, JS files
    └── README.md
```

## ⚙️ How It Works

1. The frontend provides a user interface with a button to generate a
   Snowflake ID.
1. When clicked, the frontend sends a request to the backend API.
1. The backend generates a unique Snowflake ID and sends it back.
1. The frontend displays the generated ID to the user.

## 📦 Deployment

- Caddy is used as both a reverse proxy and a load balancer
- Backend consists of multiple servers, each with different machine id.
- Frontend is hosted as a single service.

## 🛠️ Local Development

### Docker Compose

```bash
docker compose watch
```

### Backend

```bash
cd backend
uv sync --locked
uv run hypercorn app:main.app --bind :: --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```
