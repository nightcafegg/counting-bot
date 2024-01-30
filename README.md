# Counting

Counting Bot is your go-to solution for counting on Discord servers! Users take turns adding numbers in a dedicated channel, with Counting Bot ensuring accuracy and resetting if mistakes occur.

## Tech Stack

- [`Python`](https://www.python.org/)
- [`disnake`](https://disnake.dev/)
- [`PostgreSQL`](https://www.postgresql.org/)
- [`Redis`](https://redis.io/)
- [`Docker`](https://www.docker.com/)

## Setup

### Prerequisites

- [`Docker`](https://www.docker.com/)
- [`Docker Compose`](https://docs.docker.com/compose/)

### Installation

1. Clone the repository
    ```sh
    gh repo clone nightcafegg/counting-bot
    # or
    git clone nightcafegg/counting-bot
    ```

2. Copy the example environment file and fill in the values
    ```sh
    cp .env.example .env
    ```

3. Build and run the Docker containers
    ```sh
    docker-compose up -d
    ```

## Contributing

Contributions are welcome! There is currently no contributing guidelines, but feel free to open an issue or pull request if you have any suggestions or improvements.
