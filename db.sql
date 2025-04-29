-- Database: todo_app

Create Database if not exists todo_app;
create user todo_user identified by 'todo_password';
grant all privileges on todo_app.* to todo_user;
USE todo_app;
CREATE TABLE lists (
    id INT PRIMARY KEY auto_increment not null,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE tasks (
    id INT PRIMARY KEY auto_increment not null,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status boolean DEFAULT true NOT NULL,
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium' NOT NULL,
    list_id INT not null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foreign key (list_id) references lists(id)
);

insert into lists (name) values ('Work'), ('Personal'), ('Shopping'), ('Fitness'), ('Hobbies');
insert into tasks (title, description, status, priority, list_id) values 
('Finish project report', 'Complete the final report for the project.', true, 'high', 1),
('Buy groceries', 'Milk, eggs, bread, and fruits.', true, 'medium', 3),
('Gym workout', 'Leg day workout routine.', true, 'high', 4),
('Read a book', 'Finish reading the current book.', true, 'low', 5),
('Plan vacation', 'Research destinations and plan itinerary.', true, 'medium', 2);