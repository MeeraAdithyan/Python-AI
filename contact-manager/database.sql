-- PostgreSQL setup for Contact Manager
CREATE DATABASE contact_manager;

\c contact_manager;

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(120) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- Sample data
INSERT INTO contacts (name, phone, email) VALUES
('John Doe', '+916241235622', 'john@email.com'),
('Jane Smith', '+912356256320', 'jane@gmail.com'),
('Bob Johnson', '+915623412356', 'bob@yahoo.com');