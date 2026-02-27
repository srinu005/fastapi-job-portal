# 1. Use a lightweight Python image
FROM python:3.12-slim

# 2. Set the directory where our code will live inside the container
WORKDIR /app

# 3. Copy the requirements file first (this makes building faster)
COPY requirements.txt .

# 4. Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy everything else from your local folder to the container
COPY . .

# 6. Tell Docker which port the app runs on
EXPOSE 8000

# 7. The command to start the API
# We use "0.0.0.0" so it can be accessed from outside the container
CMD ["fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]