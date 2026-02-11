# User Behavior Analytics

A comprehensive real-time user behavior monitoring and risk assessment platform with ML-powered anomaly detection.

## Features

- 🔐 **JWT Authentication** - Secure role-based access control (Admin, Analyst, Viewer)
- 🤖 **ML Risk Engine** - Isolation Forest-based anomaly detection
- ⚡ **Real-time Monitoring** - WebSocket-powered live activity updates
- 📊 **Advanced Analytics** - Multiple chart types including 24-hour heatmap
- 🔍 **Comprehensive Tracking** - IP addresses and device fingerprinting
- 👥 **User Management** - Full CRUD operations with audit logging
- 🎨 **Modern UI** - Glassmorphism design with dark theme

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker (optional)

### Local Development

**Backend:**
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
python app.py
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

### Docker Deployment

```bash
docker-compose up -d
```

Access the application at `http://localhost`

## Project Structure

```
├── backend/
│   ├── app.py              # Main Flask application
│   ├── auth.py             # JWT authentication
│   ├── user_manager.py     # User CRUD operations
│   ├── ml_risk_engine.py   # ML anomaly detection
│   ├── behavior_profiler.py # User profiling
│   ├── velocity_checker.py  # Velocity checks
│   ├── audit_logger.py     # Audit logging
│   ├── config.py           # Configuration
│   ├── validation.py       # Input validation
│   ├── error_handlers.py   # Error handling
│   └── tests/              # Unit tests
├── frontend/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── Login.js        # Login component
│   │   └── UserManagement.js # User management UI
│   └── public/
└── docker-compose.yml      # Docker orchestration
```

## API Documentation

Access Swagger documentation at: `http://localhost:5000/api/docs`

## Environment Variables

See `.env.example` for all configuration options.

Critical variables:
- `JWT_SECRET_KEY` - Must be changed in production
- `FLASK_ENV` - Set to `production` for deployment
- `DATABASE_PATH` - Database file location

## Testing

**Backend:**
```bash
cd backend
pytest --cov
```

**Frontend:**
```bash
cd frontend
npm test
```

## Security Features

- ✅ JWT-based authentication
- ✅ Password hashing with bcrypt
- ✅ Input validation and sanitization
- ✅ SQL injection prevention
- ✅ CORS configuration
- ✅ Rate limiting ready
- ✅ Audit logging

## Production Deployment

1. Update environment variables
2. Change `JWT_SECRET_KEY`
3. Set `FLASK_ENV=production`
4. Use `gunicorn` for backend
5. Build frontend with `npm run build`
6. Deploy with Docker or cloud platform

## License

MIT License

## Support

For issues and questions, please open an issue on GitHub.
