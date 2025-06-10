# Messages API Documentation

## Base URL
`http://localhost:5000`

## Endpoints

### Get All Messages
- **URL:** `/api/messages`
- **Method:** GET
- **Success Response:**
  - **Code:** 200
  - **Content:** Array of messages
    ```json
    [
      {
        "id": 1,
        "content": "Hello world",
        "created_at": "2025-06-10T12:00:00Z"
      }
    ]
    ```

### Create Message
- **URL:** `/api/messages`
- **Method:** POST
- **Data Parameters:**
  ```json
  {
    "content": "Your message here"
  }
  ```
- **Success Response:**
  - **Code:** 201
  - **Content:** Created message object
    ```json
    {
      "id": 1,
      "content": "Your message here",
      "created_at": "2025-06-10T12:00:00Z"
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{"error": "Missing content"}`

### Delete Message
- **URL:** `/api/messages/:id`
- **Method:** DELETE
- **URL Parameters:** `id=[integer]`
- **Success Response:**
  - **Code:** 204
  - **Content:** None
- **Error Response:**
  - **Code:** 404
  - **Content:** Not Found

## Database Schema

### Message Table
- `id`: Integer (Primary Key)
- `content`: String (max 500 characters)
- `created_at`: DateTime (auto-set to UTC time of creation)

## Running the Application

### Backend (Flask)
1. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python app.py
   ```
Server will start at `http://localhost:5000`

### Frontend (Next.js)
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Run the development server:
   ```bash
   npm run dev
   ```
Frontend will be available at `http://localhost:3000`
