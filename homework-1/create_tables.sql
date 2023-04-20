-- SQL-команды для создания таблиц
create table employees
(
	first_name varchar(100) PRIMARY KEY,
	last_name varchar(100) not null,
	title varchar(100) not null,
	birth_date date not null,
	notes varchar(100)
);

create table customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(100) not null,
	contact_name varchar(100) not null
);

create table orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id) not null,
	employee_id int not null,
	order_date date not null,
	ship_city varchar(100)
);
