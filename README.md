# TMS Backend

Task Management System backend built with **Flask**, **MySQL**, and **Docker**.

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Installation and Setup

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd tms-python-backend
   ```

2. Create environment file
   ```bash
   cp .env.example .env
   ```

3. Start the services
   ```bash
   docker-compose up -d
   ```

4. Access the application at http://tms.uit.local:8084

   > Note: Don't forget to add the domain to your hosts file.
   >
   > ```
   > 127.0.0.1    tms.uit.local
   > ```
   
## 🧱 Database Migration
  > Note: Don't forget run the migration after you create a new database.
   >
   > ```
   > touch cmd/__init__.py
   > 
   > docker compose run --rm flask_app python -m cmd.migrate
   > ```
   >

## 📦 Services

- **Flask Backend**: Available at http://localhost:5001

## 🛠️ Development

### Project Structure
```
tms-python-backend/
├── run.py                # Main application file
├── config.py             # Configuration management
├── app/                  # Application package
├── docker/               # Docker configurations
│   ├── Dockerfile        
│   └── nginx/            # Nginx configurations
├── docs/                 # Documentation
│   └── database-v1.md    # Database schema
└── logs/                 # Log files
```

### Database

The database schema is defined in [docs/database-v1.md](docs/database-v1.md).

## 📄 License

This project is licensed under the MIT License.
