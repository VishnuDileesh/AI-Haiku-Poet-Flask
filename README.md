# AI Haiku Poet

A Flask-based web application that generates beautiful haikus about any theme using OpenAI's GPT-3.5 model. Features a simple web interface with HTMX for seamless interactions.

## Features

- Clean, minimal web interface
- HTMX-powered form submissions
- OpenAI GPT-3.5 for haiku generation
- Line-break preserved haiku display
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

## Using the Application

### Web Interface
Visit the root URL (e.g., http://localhost:5000) to access the web interface:
1. Enter a theme in the input field
2. Click "Submit"
3. The haiku will appear below with proper formatting and line breaks

### API Endpoints

#### Generate Haiku
```
POST /get-haiku
```
Parameters (form data):
- `theme`: The theme for the haiku

Example request:
```bash
curl -X POST -F "theme=inkling" http://localhost:8000/get-haiku
```

Example response:
```html
<h3 style='white-space: pre-wrap;'>Inkling’s gentle sway<br>Whispers secrets in the breeze<br>Nature’s silent muse</h3>
```

Note: The endpoint returns formatted HTML with preserved line breaks for direct display.

#### Health Check
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

## Project Structure

- `main.py`: Flask application and route handlers
- `templates/index.html`: Simple web interface with HTMX
- `gunicorn.conf.py`: Production server configuration
- `.env`: Configuration for API keys and environment
- `requirements.txt`: Project dependencies

## Technology Stack

- Flask: Lightweight web framework
- OpenAI GPT-3.5: AI model for haiku generation
- HTMX: Simple frontend interactivity
- Pico CSS: Minimal styling framework
- Gunicorn: Production WSGI server

## Configuration

### Gunicorn Settings
The `gunicorn.conf.py` file includes production-ready settings:
- Dynamic worker count based on CPU cores
- Logging configuration
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

![CleanShot 2025-01-27 at 11 22 44@2x](https://github.com/user-attachments/assets/d1f649ef-50ac-437f-b746-1ecbc3b94c76)


## License

MIT License 
