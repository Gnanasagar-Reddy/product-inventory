
# Telusko Trac - Product Inventory Management

A comprehensive product inventory management system built with FastAPI backend and React frontend, providing seamless tracking and management of product inventory.

## Features

- **GET /**: Welcome endpoint
- **GET /products/**: Get all products
- **GET /products/{product_id}**: Get a specific product by ID
- **POST /products/**: Create a new product

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate.ps1  # Windows PowerShell
   ```

2. **Install dependencies:**
   ```bash
   python -m pip install -r backend/requirements.txt
   ```

3. **Configure the database:** Copy `.env.example` to `.env` in the project root and set `DB_PASSWORD` to your local PostgreSQL password. Keep `.env` private. PostgreSQL must be running with a database named `fastapi_tut`.

4. **Run the application:**
   ```bash
   cd backend
   python -m uvicorn main:app --reload
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Structure

```
stocksphere/
├── main.py          # FastAPI application with endpoints
├── models.py        # Pydantic models
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## API Usage Examples

### Get all products
```bash
curl http://localhost:8000/products/
```

### Get product by ID
```bash
curl http://localhost:8000/products/1
```

### Create a new product
```bash
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 5,
       "name": "Monitor",
       "description": "4K monitor",
       "price": 299.99,
       "quantity": 15
     }'
```

## Models

### Product
- `id`: integer
- `name`: string
- `description`: string
- `price`: float
- `quantity`: integer

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation
