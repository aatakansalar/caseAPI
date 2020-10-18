FROM python:3.6

# Copy the files
COPY . .

# Install requirements for the program
RUN pip3 install -r "requirements/requirements.txt"

# Run the program
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]