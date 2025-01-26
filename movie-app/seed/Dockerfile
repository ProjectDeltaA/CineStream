FROM python:3.12-slim

# Set the working directory
WORKDIR /seed

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir pandas pymongo

# Run the seed script
CMD ["python", "seed_db.py"]
