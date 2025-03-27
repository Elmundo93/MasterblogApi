# Masterschool Flask Blogging Platform

## Overview
This project is a full-stack blogging platform developed as part of the Masterschool curriculum. It demonstrates how to build a RESTful API using Flask (backend) and a simple Flask-based frontend that communicates with the API via JavaScript. The platform allows users to list, add, update, delete, search, and sort blog posts.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Requirements](#requirements)
- [License](#license)

## Features
- **List Posts:** Retrieve all blog posts with optional sorting by title or content.
- **Add Post:** Create a new blog post with a title and content.
- **Delete Post:** Remove an existing blog post by its unique identifier.
- **Update Post:** Modify the title and/or content of an existing post.
- **Search Posts:** Find posts by matching search terms in the title or content.
- **Sorting:** Supports sorting in both ascending and descending order based on title or content.

## Project Structure
project-root/
│
├── backend/
│   └── backend_app.py       # Flask backend application
│
├── frontend/
│   ├── static/
│   │   ├── main.js          # JavaScript file handling API calls
│   │   └── styles.css       # CSS for styling the frontend
│   └── templates/
│       └── index.html       # HTML template for the frontend
│
├── frontend_app.py          # Flask frontend application
├── README.md                # This file
└── requirements.txt         # Python dependencies

## Prerequisites
- **Python 3.7+** installed on your machine.
- **pip** package manager.
- (Optional) A virtual environment tool such as `venv` or `virtualenv`.

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   
2. **Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install the dependencies:**
pip install -r requirements.txt

## Running the Application
This project consists of two Flask applications: one for the backend API and one for the frontend.

### Running the Backend
1. Navigate to the `backend` directory:
    cd backend
2. 	Start the backend server:
python backend_app.py
The backend will run at `http://0.0.0.0:5002`.

### Running the Frontend
1. Open a new terminal and navigate to the project root.
2. Start the frontend server:
    python frontend_app.py
The frontend will run at `http://0.0.0.0:5001`.
3. Open your web browser and go to `http://127.0.0.1:5001` to view the application.

## API Documentation
### List Posts
- **Endpoint:** `GET /api/posts`
- **Description:** Retrieves all blog posts.
- **Optional Query Parameters:**
- `sort`: Field to sort by (`title` or `content`).
- `direction`: Sorting order (`asc` or `desc`).

### Add Post
- **Endpoint:** `POST /api/posts`
- **Description:** Creates a new blog post.
- **Request Body:**
{
“title”: “Your post title”,
“content”: “Your post content”
}
- **Response:** Returns the created post with a new unique ID.
- **Error:** Returns `400 Bad Request` if the title or content is missing.

### Delete Post
- **Endpoint:** `DELETE /api/posts/<id>`
- **Description:** Deletes a blog post identified by its ID.
- **Response:** Returns a success message.
- **Error:** Returns `404 Not Found` if the post does not exist.

### Update Post
- **Endpoint:** `PUT /api/posts/<id>`
- **Description:** Updates a blog post.
- **Request Body:**
{
“title”: “Updated title (optional)”,
“content”: “Updated content (optional)”
}
- **Response:** Returns the updated post.
- **Error:** Returns `404 Not Found` if the post does not exist.

### Search Posts
- **Endpoint:** `GET /api/posts/search`
- **Description:** Searches for posts by title and/or content.
- **Query Parameters:**
- `title`: Search term for the post title.
- `content`: Search term for the post content.
- **Response:** Returns a list of posts matching the search criteria (empty list if no match).

## Testing
- **Using Postman:**  
Send requests to the API endpoints (e.g., `http://127.0.0.1:5002/api/posts`) to verify functionality.

- **Using the Frontend:**  
Open the frontend at `http://127.0.0.1:5001` and use the interface to interact with the API.

## Requirements
For a complete list of dependencies, please see the [requirements.txt](requirements.txt) file.

## License
This project is licensed under the MIT License.