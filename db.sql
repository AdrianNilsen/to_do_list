-- Database: todo_app

Create Database if not exists todo_app;
create user todo_user identified by 'todo_password';
create user 'todo_user'@'%' identified by 'todo_password';
grant all privileges on todo_app.* to 'todo_user'@'%';
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

insert into lists (name) values ('Arbeid'), ('Personlig'), ('Handleliste'), ('Trening'), ('Hobbyer');
insert into tasks (title, description, status, priority, list_id) values 
('Fullfør prosjekt rapport', 'Fullfør den endelige rapporten for prosjektet.', true, 'high', 1),
('Kjøp dagligvarer', 'Melk, egg, brød og frukt.', true, 'medium', 3),
('Treningsøkt', 'Beindag treningsrutine.', true, 'high', 4),
('Les en bok', 'Fullfør å lese den nåværende boken.', true, 'low', 5),
('Planlegg ferie', 'Undersøk destinasjoner og planlegg reiserute.', true, 'medium', 2);