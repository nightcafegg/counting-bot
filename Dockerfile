FROM python:3.12-slim

# Set pip to have cleaner logs and no cache
ENV PIP_NO_CACHE_DIR=false

# Create the working directory
WORKDIR /bot

# Copy the requirements file
COPY requirements.txt .

# Install project dependencies
RUN apt-get update -y \
 pip install -U pip wheel setuptools \
 pip install -Ur requirements.txt

# Copy the source code
COPY . .

# Install the package using pep 517
RUN pip install . --no-deps

ENTRYPOINT ["python", "-m", "counting"]
