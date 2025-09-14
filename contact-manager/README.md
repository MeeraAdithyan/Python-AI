# Contact Manager API

Simple Flask REST API for managing contacts with PostgreSQL.

## Setup

1. Install dependencies:

```pip install -r requirements.txt```

2. Setup PostgreSQL database: Log in to PostgreSQL and run the SQL file to create the database and tables:
```psql -U postgres -f database.sql```

3. Update database connection in `config.py`

4. Run the app:
```python app.py```

## API Endpoints

- `GET /api/contacts` - Get all contacts
- `GET /api/contacts/<id>` - Get contact by ID
- `POST /api/contacts` - Create contact
- `PUT /api/contacts/<id>` - Update contact  
- `DELETE /api/contacts/<id>` - Delete contact
