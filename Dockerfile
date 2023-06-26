FROM python:3.11-slim

# Set pip to have cleaner logs and no cache
ENV PIP_NO_CACHE_DIR=false

# Create the working directory
WORKDIR /bot

# Install project dependencies
RUN apt update -y
RUN pip install -U pip wheel setuptools
RUN pip install poetry==1.3

# Export requirements after copying req files
COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes > requirements.txt
RUN pip uninstall poetry -y
RUN pip install -Ur requirements.txt

# Copy the source code
COPY . .

# Install the package using pep 517
RUN pip install . --no-deps

ENTRYPOINT ["python", "-m", "kazoeru"]