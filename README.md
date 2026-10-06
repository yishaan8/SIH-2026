

AI-Powered Real-Time Detection and Prevention of Voice Cloning Impersonation Attacks.

## Project Structure

- `frontend/` — Voice Integrity web application
- `backend/` — API and orchestration layer
- `ai/` — Voice AI/ML modules

## Run the demo

### Local frontend

```bash
cd frontend
npm ci
npm run dev
```

The frontend runs in clearly labelled Demo mode when `VITE_ANALYSIS_API_URL` is
not configured. To connect the Spring Boot service, copy
`frontend/.env.example` to `frontend/.env.local` and set the API URL.

### Docker

From the repository root:

```bash
docker compose up --build
```

Open <http://localhost:4173>. The container serves the production bundle and
supports client-side routes through Nginx. A health check is available at
<http://localhost:4173/healthz>.

### Evidence hash demo

The prototype fingerprints the final analysis JSON, never raw audio:

```bash
cd frontend
npm run hash:evidence
```

The SHA-256 output is deterministic for the frozen integration contract and can
be shown during the submission demo.
