CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT,
    username text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text DEFAULT NULL,
    psw text NOT NULL,
    registration_date text NOT NULL,
    avatar BLOB DEFAULT NULL,
    UNIQUE(username, email)
);