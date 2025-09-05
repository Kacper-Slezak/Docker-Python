# Notes Service

A simple note-taking web application built with Flask, PostgreSQL, and Docker for demonstrating DevOps practices.

## 🚀 Features

- Create and delete notes
- PostgreSQL database for persistent storage
- Containerized with Docker and Docker Compose
- Production-ready with Gunicorn WSGI server

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Web Server:** Gunicorn
- **Frontend:** HTML, CSS, Jinja2 templates

## 📋 Prerequisites

- Docker
- Docker Compose
- Git

## 🏃‍♂️ Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd notes-service
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   Open your browser and go to `http://localhost:5000`

## 📁 Project Structure

```
notes-service/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   ├── static/
│   │   └── style.css        # CSS styles
│   └── templates/
│       └── index.html       # HTML template
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # Docker image definition
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:password@db:5432/mydatabase` |
| `FLASK_APP` | Flask application entry point | `app` |
| `FLASK_ENV` | Flask environment | `development` |

### Database Configuration

The application uses PostgreSQL with the following default settings:
- **Host:** db (Docker service name)
- **Port:** 5432
- **Database:** mydatabase
- **Username:** user
- **Password:** password

## 🐳 Docker Commands

```bash
# Build and start services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Remove volumes (data will be lost)
docker-compose down -v
```

## 🧪 Development

### Running Locally (without Docker)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up PostgreSQL and update `DATABASE_URL`

3. Run the application:
   ```bash
   flask run
   ```

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display all notes and add note form |
| POST | `/` | Create a new note |
| GET | `/delete_note/<int:note_id>` | Delete a specific note |

## 🔒 Security Considerations

- Database credentials are currently hardcoded in docker-compose.yml
- No authentication/authorization implemented
- Input validation is minimal

## 🚧 Known Issues

- No error handling for database connection failures
- No input sanitization
- No tests implemented

## 📝 Future Improvements

- [ ] Add user authentication
- [ ] Implement REST API
- [ ] Add unit and integration tests
- [ ] Implement proper logging
- [ ] Add database migrations
- [ ] Improve error handling
- [ ] Add input validation and sanitization
- [ ] Implement CI/CD pipeline

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- GitHub: [@Kacper-Slezak](https://github.com/Kacper-Slezak)

## 🙏 Acknowledgments

- Flask documentation
- Docker documentation
- PostgreSQL community
