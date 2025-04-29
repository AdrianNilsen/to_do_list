-- Database: todo_app

Create Database if not exists todo_app;
create user todo_user identified by 'todo_password';
grant all privileges on todo_app.* to todo_user;
USE todo_app;

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status boolean DEFAULT true,
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);