# Dockerfile for FreshCart Online Grocery Application
# Case 37: Online Grocery
# Student: Likhith Gowda M S (ENG24CS0105 / Roll 37)

FROM python:3.14-slim

LABEL maintainer="Likhith Gowda M S <eng24cs0105@dsu.edu.in>"
LABEL case="37"
LABEL project="Online Grocery"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV FLASK_APP=grocery_app.app:app

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and test files
COPY grocery_app/ grocery_app/
COPY tests/ tests/

# Expose web application and health check port
EXPOSE 5000

# Docker healthcheck targeting the monitoring endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the Flask production application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
