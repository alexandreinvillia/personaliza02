# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request validation, and CRUD-style operations.
By the end of this assignment, students should be able to design endpoints and test them using browser docs or API clients.

## 📝 Tasks

### 🛠️ Create the API Structure

#### Description
Set up a FastAPI project and implement the core endpoints for a resource called items.

#### Requirements
Completed program should:

- Create a FastAPI app in starter-code.py and run it with uvicorn.
- Implement a GET endpoint at / that returns a welcome JSON message.
- Implement a GET endpoint at /items that returns a list of items.
- Implement a GET endpoint at /items/{item_id} that returns one item by ID.

### 🛠️ Add Validation and Write Operations

#### Description
Extend the API with request body validation and endpoints to create and update items.

#### Requirements
Completed program should:

- Define a Pydantic model for item data (for example: name, price, in_stock).
- Implement a POST endpoint at /items to create a new item.
- Implement a PUT endpoint at /items/{item_id} to update an existing item.
- Return appropriate status codes and clear JSON responses for success and error cases.
