CREATE TABLE book(
  book_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(60) NOT NULL DEFAULT '',
  genre VARCHAR(60) NOT NULL DEFAULT '',
  quantity_in_stock INT NOT NULL DEFAULT 0,
  PRIMARY KEY (book_id)
) ENGINE = MyISAM ;

CREATE TABLE book_autor(
	book_id INT NOT NULL AUTO_INCREMENT,
	autor_id INT NOT NULL,
        PRIMARY KEY (autor_id),
        FOREIGN KEY (book_id) REFERENCES book(book_id)
) ENGINE = MyISAM ;

CREATE TABLE AUTOR(
	autor_id INT NOT NULL,
        first_name VARCHAR(60) NOT NULL DEFAULT '',
        middle_name VARCHAR(60) NOT NULL DEFAULT '',
        full_name VARCHAR(60) NOT NULL DEFAULT '',
        short_name VARCHAR(60) NOT NULL DEFAULT '',
        FOREIGN KEY (autor_id) REFERENCES book_autor(autor_id)
) ENGINE = MyISAM ;

CREATE TABLE rating(
	book_id INT NOT NULL AUTO_INCREMENT,
        rating NUMERIC NOT NULL DEFAULT 0.00,
        count_voted INT NOT NULL DEFAULT 0,
        FOREIGN KEY (book_id) REFERENCES book(book_id)
) ENGINE = MyISAM;

CREATE TABLE ORDER_ITEMS(
	order_id INT NOT NULL,
	client_id INT NOT NULL,
	book_id INT NOT NULL,
	FOREIGN KEY (order_id) REFERENCES order(order_id),
	FOREIGN KEY (client_id) REFERENCES client(client_id),
	FOREIGN KEY (book_id) REFERENCES book(book_id)
) ENGINE = MyISAM ;

CREATE TABLE time_of_orders(
	order_id INT NOT NULL,
	open_date datetime NOT NULL,
	close_date datetime,
	PRIMARY KEY (order_id)
) ENGINE = MyISAM ;

CREATE TABLE CLIENT(
	client_id INT NOT NULL,
        login VARCHAR(60) NOT NULL DEFAULT '',
        name VARCHAR(60) NOT NULL DEFAULT '',
	password VARCHAR(60) NOT NULL,
	PRIMARY KEY (client_id)
) ENGINE = MyISAM ;
