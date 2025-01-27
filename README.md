# AI Haiku Poet

A Flask-based web service that generates beautiful haikus about any theme using OpenAI's GPT-3.5 model.

## Features

- Generate unique haikus based on user-provided themes
- RESTful API endpoints
- Powered by OpenAI's GPT-3.5 model
- Health check endpoint
- Production-ready Gunicorn configuration

## Prerequisites

- Python 3.8+
- OpenAI API key

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd AI-Haiku-Poet-Flask
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env_example` to `.env`
   - Add your OpenAI API key and environment setting to the `.env` file:
```bash
OPENAI_API_KEY=your_api_key_here
ENVIRONMENT=development  # or production
```

## Running the Application

### Development Mode
Run the Flask development server:
```bash
python main.py
```
This will start the server on http://localhost:5000 with debug mode enabled.

### Production Mode
Run with Gunicorn using the provided configuration:
```bash
gunicorn -c gunicorn.conf.py main:app
```
This will start the server on http://0.0.0.0:8000 with optimized settings.

## API Endpoints

### Generate a Haiku
```
GET /haiku?theme={theme}
```
- `theme`: The theme for the haiku

Example request:
```bash
curl "http://localhost:8000/haiku?theme=spring"
```

Example response:
```json
{
    "Haiku": "Inkling of the mind,\nNature's whispers on the wind,\nInspiration finds."
}
```

### Health Check
```
GET /health
```
Example request:
```bash
curl "http://localhost:8000/health"
```

Example response:
```json
{
    "Health": "Ok"
}
```

## Configuration

### Gunicorn Settings
The `gunicorn.conf.py` file includes production-ready settings:
- Dynamic worker count based on CPU cores
- Proper logging configuration
- Development mode auto-reload
- Connection handling optimization

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key
- `ENVIRONMENT`: Set to 'development' or 'production'

## Production Deployment Tips

- Ensure your `.env` file is properly configured with production settings
- Consider using a reverse proxy (like Nginx) in front of Gunicorn
- Set up proper monitoring and logging
- Implement rate limiting and security measures as needed

## License

MIT License 