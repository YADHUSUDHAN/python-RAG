# 🐳 Docker Deployment Guide (Optional)

## Overview

Docker provides containerized deployment - your app runs the same everywhere! Great for:
- ✅ Consistent environments (dev = prod)
- ✅ Easy scaling
- ✅ Self-hosting on AWS, Azure, GCP
- ✅ Team collaboration

---

## Quick Docker Setup

### 1. Create `Dockerfile`

```dockerfile
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. Create `.dockerignore`

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log

# Environment
.env

# Git
.git/
.gitignore

# Documentation
*.md
docs/
screenshots/

# Tests
tests/
pytest.ini
.pytest_cache/
```

### 3. Create `docker-compose.yml`

```yaml
version: '3.8'

services:
  rag-app:
    build: .
    container_name: rag-qa-system
    ports:
      - "8501:8501"
    environment:
      - LLM_PROVIDER=${LLM_PROVIDER}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - HUGGINGFACE_API_KEY=${HUGGINGFACE_API_KEY}
      - LLM_MODEL=${LLM_MODEL}
      - EMBEDDING_MODEL=${EMBEDDING_MODEL}
      - TEMPERATURE=${TEMPERATURE}
      - MAX_NEW_TOKENS=${MAX_NEW_TOKENS}
      - CHUNK_SIZE=${CHUNK_SIZE}
      - CHUNK_OVERLAP=${CHUNK_OVERLAP}
      - TOP_K_RESULTS=${TOP_K_RESULTS}
      - DEVICE=${DEVICE}
      - LOG_LEVEL=${LOG_LEVEL}
    volumes:
      - ./logs:/app/logs
      - model-cache:/root/.cache/huggingface
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

volumes:
  model-cache:
```

---

## Usage

### Build and Run

```bash
# Build the image
docker build -t rag-qa-system .

# Run the container
docker run -p 8501:8501 \
  -e LLM_PROVIDER=openai \
  -e OPENAI_API_KEY=your-key \
  rag-qa-system

# Or use docker-compose (recommended)
docker-compose up -d
```

### Access

Open browser: `http://localhost:8501`

### Stop

```bash
# Using docker-compose
docker-compose down

# Or direct docker
docker stop rag-qa-system
```

---

## Docker Deployment Platforms

### 1. AWS ECS (Elastic Container Service)

**Cost**: ~$10-30/month  
**Steps**:
1. Push image to ECR
2. Create ECS cluster
3. Define task definition
4. Create service
5. Configure load balancer

**Best for**: Production, scalability needed

### 2. Google Cloud Run

**Cost**: Pay per use (~$5-20/month)  
**Steps**:
1. Build image: `gcloud builds submit`
2. Deploy: `gcloud run deploy`
3. Auto-scales to zero (pay only when used!)

**Best for**: Variable traffic, cost-conscious

### 3. Azure Container Instances

**Cost**: ~$10-30/month  
**Steps**:
1. Push to Azure Container Registry
2. Create container instance
3. Configure networking

**Best for**: Azure ecosystem users

### 4. DigitalOcean App Platform

**Cost**: $5-12/month  
**Steps**:
1. Connect GitHub
2. Select Dockerfile
3. Add environment variables
4. Deploy

**Best for**: Simple, affordable

### 5. Self-Hosted (VPS)

**Cost**: $5-10/month (Linode, Vultr, Hetzner)  
**Steps**:
1. Rent VPS
2. Install Docker
3. Upload code
4. Run `docker-compose up -d`

**Best for**: Full control, learning

---

## Production Dockerfile (Optimized)

```dockerfile
# Multi-stage build for smaller image
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy application
COPY . .

# Add local bin to PATH
ENV PATH=/root/.local/bin:$PATH

# Non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", \
    "--server.port=8501", \
    "--server.address=0.0.0.0", \
    "--server.headless=true", \
    "--browser.serverAddress=0.0.0.0"]
```

---

## Docker with GPU Support (Advanced)

For faster embeddings/models:

```dockerfile
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Install Python
RUN apt-get update && apt-get install -y python3.11 python3-pip

# Install PyTorch with CUDA
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cu118

# Continue as normal...
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

**Run with GPU**:
```bash
docker run --gpus all -p 8501:8501 rag-qa-system
```

---

## Environment Variables in Docker

### Option 1: .env file with docker-compose

Create `.env.docker`:
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key
LLM_MODEL=gpt-3.5-turbo
```

```bash
docker-compose --env-file .env.docker up
```

### Option 2: Pass at runtime

```bash
docker run -p 8501:8501 \
  -e LLM_PROVIDER=openai \
  -e OPENAI_API_KEY=sk-your-key \
  -e LLM_MODEL=gpt-3.5-turbo \
  rag-qa-system
```

### Option 3: Docker secrets (production)

```bash
echo "sk-your-key" | docker secret create openai_key -
```

---

## CI/CD with Docker

### GitHub Actions Example

```yaml
name: Build and Deploy Docker

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Login to DockerHub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          push: true
          tags: username/rag-qa-system:latest
      
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            docker pull username/rag-qa-system:latest
            docker-compose up -d
```

---

## Docker vs Streamlit Cloud

| Feature | Docker | Streamlit Cloud |
|---------|--------|-----------------|
| **Setup Complexity** | Medium | Easy |
| **Cost** | $5-30/month | FREE |
| **Control** | Full | Limited |
| **Scaling** | Manual | Automatic |
| **GPU Support** | Yes | No |
| **Custom Domain** | Easy | Pro only |
| **Best For** | Production | Demos/Portfolio |

---

## Performance Optimization

### 1. Multi-stage builds (smaller images)
```dockerfile
FROM python:3.11 as builder
# Build here

FROM python:3.11-slim
COPY --from=builder ...
# Runtime only
```

### 2. Layer caching
```dockerfile
# Copy requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt

# Then copy code (changes more often)
COPY . .
```

### 3. Use .dockerignore
- Reduces build context size
- Faster builds
- Smaller images

---

## Monitoring Docker Containers

### Logs
```bash
# View logs
docker logs rag-qa-system

# Follow logs
docker logs -f rag-qa-system

# Last 100 lines
docker logs --tail 100 rag-qa-system
```

### Resource Usage
```bash
# Stats
docker stats rag-qa-system

# Inspect
docker inspect rag-qa-system
```

### Health Checks
```bash
# Check health
docker ps
# Look for "healthy" status
```

---

## Security Best Practices

1. **Don't store secrets in image**
   ```dockerfile
   # ❌ BAD
   ENV OPENAI_API_KEY=sk-123
   
   # ✅ GOOD
   # Pass at runtime via -e or docker-compose
   ```

2. **Use non-root user**
   ```dockerfile
   RUN useradd -m appuser
   USER appuser
   ```

3. **Scan for vulnerabilities**
   ```bash
   docker scan rag-qa-system
   ```

4. **Keep base images updated**
   ```dockerfile
   FROM python:3.11-slim  # Use specific versions
   ```

---

## When to Use Docker

### ✅ Use Docker When:
- Deploying to cloud (AWS, GCP, Azure)
- Need consistent environments
- Self-hosting
- Multiple services (frontend + backend)
- Need GPU support
- Want full control

### ❌ Don't Use Docker When:
- Just need quick demo (use Streamlit Cloud)
- Learning/prototyping
- Don't want maintenance overhead
- Free hosting is enough

---

## Quick Commands Reference

```bash
# Build
docker build -t rag-qa-system .

# Run
docker run -d -p 8501:8501 rag-qa-system

# Stop
docker stop rag-qa-system

# Remove
docker rm rag-qa-system

# View logs
docker logs rag-qa-system

# Execute command inside
docker exec -it rag-qa-system bash

# With docker-compose
docker-compose up -d          # Start
docker-compose down           # Stop
docker-compose logs -f        # Logs
docker-compose restart        # Restart
```

---

## Cost Comparison

| Platform | Docker Cost | Traffic Limit | Best For |
|----------|-------------|---------------|----------|
| **Streamlit Cloud** | FREE | Good | Demos |
| **Google Cloud Run** | $5-20/month | Pay per use | Variable traffic |
| **DigitalOcean** | $12/month | Unlimited | Steady traffic |
| **AWS ECS** | $20-50/month | Unlimited | Enterprise |
| **Self-hosted VPS** | $5-10/month | Unlimited | Learning |

---

## Conclusion

**For Your Resume Project:**
- ✅ **Start with Streamlit Cloud** (free, easy)
- ✅ **Mention Docker capability** in README
- ✅ **Add Dockerfile** to repo (shows skills)
- ⚠️ **Don't deploy with Docker** unless needed

**Employers love seeing**:
- Dockerfile in repo ✅ (shows DevOps knowledge)
- Multiple deployment options ✅
- Production-ready practices ✅

**But for demo purposes**:
- Streamlit Cloud is perfect! 🎯
- FREE, fast, no maintenance
- Just add Dockerfile to show you *could* use Docker

---

## Next Steps

1. ✅ Add Dockerfile to your repo (show skills)
2. ✅ Add Docker section to README
3. ✅ Deploy on Streamlit Cloud (free, easy)
4. ✅ Mention both options in resume
5. ⏭️ Learn Docker deployment if job requires it

**You don't need to deploy with Docker now - just showing you know about it is valuable!** 🚀
