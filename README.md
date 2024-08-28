# FastAPI MongoDB Integration

This project demonstrates how to integrate FastAPI with MongoDB using the Motor library, an asynchronous Python driver for MongoDB. It provides basic CRUD operations for managing items in a MongoDB collection.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Connect to MongoDB using the Motor library.
- Perform CRUD (Create, Read, Update, Delete) operations on items.
- Simple and efficient structure to build upon.

## Requirements

- Python 3.8+
- MongoDB (running locally or accessible via URI)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate the Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

#### On macOS and Linux:

```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:

```bash
python -m venv env
.\env\Scripts\activate
```

### 3. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This command will start the server on `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`. 

## API Endpoints

- **GET /items**: Retrieve all items.
- **POST /items**: Create a new item.
- **GET /items/{item_id}**: Retrieve an item by ID.
- **PUT /items/{item_id}**: Update an item by ID.
- **DELETE /items/{item_id}**: Delete an item by ID.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
