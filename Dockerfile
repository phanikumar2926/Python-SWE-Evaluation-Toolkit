# Use an official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the automated tests by default
CMD ["python", "-m", "pytest", "tests/test_user_validation.py", "tests/test_task_manager.py", "tests/test_duplicate_detection.py", "tests/test_golden_discount_calculator.py", "-v"]