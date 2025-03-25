# TMS Backend

Task Management System backend built with Flask and MySQL.

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

## 📦 Services

- **Flask Backend**: Available at http://localhost:5001

## 🛠️ Development

### Project Structure
```
tms-python-backend/
├── app.py                # Main application file
├── config.py             # Configuration management
├── models/               # Database models
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
