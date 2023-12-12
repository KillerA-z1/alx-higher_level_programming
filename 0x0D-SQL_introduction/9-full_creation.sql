-- a script that creates a second_table in the database hbtn_0c_0 and add multiples rows.
CREATE TABLE IF NOT EXISTS `second_table` (
	`id` int,
	`name` varchar(256),
	`score` int
	);

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES
('1', 'Bob', '14'),
('2', 'John', '10'),
('3', 'George', '8'),
('4', 'Alex', '3');