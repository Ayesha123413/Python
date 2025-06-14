# Project Title
# Tea House API

A simple FastAPI application for managing a tea collection.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. After completing the setup, run the application using:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your browser and navigate to:
   - http://localhost:8000 - For the welcome message
   - http://localhost:8000/docs - For the interactive API documentation

## Available Endpoints
- GET / - Welcome message
- GET /teas - Get all teas
- POST /teas - Add a new tea
- PUT /teas/{tea_id} - Update a tea
- DELETE /teas/{tea_id} - Delete a tea
