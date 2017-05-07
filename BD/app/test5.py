import psycopg2
import psycopg2.extras
import string

def format_t(input_f):
    """if input_f is not None:
        try:
            input_file = open(input_f, 'r')
        except IOError as e:
            print("I/O Error in string: ", e.strerror)
    else:
        input_file = sys.stdin"""
    input_file = input_f
    #output_file = input_f
    line_length = 10000000
    paragraph_spaces = 0
    out = []
    s0 = "',.?!-:'"
    fl = 0
    for line in input_file:
        i = 0
        while i < len(line):
            current = line[i]
            if fl == 0:
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "'" or current == "=" or current == "_":
                    out.append(' ' * paragraph_spaces + current)
                    fl = 1
                elif s0.find(current) != -1:
                    fl = 2
                elif current == ' ':
                    fl = 0
                elif ord(current) == 10:
                    fl = 0
            elif fl == 1:
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "'" or current == "=" or current == "_":
                    out[-1] += current
                    fl = 1
                elif s0.find(current) != -1:
                    out[-1] += current
                    fl = 2
                elif current == ' ':
                    fl = 2
                elif ord(current) == 10:
                    fl = 3
            elif fl == 2:
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "'" or current == "=" or current == "_":
                    out.append(current)
                    fl = 1
                elif s0.find(current) != -1:
                    out[-1] += current
                    fl = 2
                elif current == ' ':
                    fl = 2
                elif ord(current) == 10:
                    fl = 3
            elif fl == 3:
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "'" or current == "=" or current == "_":
                    out.append(current)
                    fl = 1
                elif s0.find(current) != -1:
                    fl = 2
                elif current == ' ':
                    fl = 3
                elif ord(current) == 10:
                    out[-1] += current
                    fl = 0
            i += 1
    l = 0
    fl_a = 0
    se0 = ''
    for world in out:
        if len(world) < line_length:
            if l + len(world) < line_length:
                if l == 0:
                    se0 += world
                    l += len(world)
                else:
                    se0 += (' ' + world)
                    l += (len(world) + 1)
                if ord(world[-1]) != 10:
                    fl_a = 1
                else:
                    l = 0
                    fl_a = 0
            else:
                if fl_a == 0:
                    raise ValueError('The word is too long')
                else:
                    l = len(world) + 1
                    se0 = se0 + chr(10) + world
                    fl_a = 1
        else:
            raise ValueError('The word is too long')
    """if output_f is not None:
        output_file = open(output_f, 'w')
    else:
        output_file = sys.stdout"""
    """input_file.close()
    output_file.close()"""
    return se0


def create_Tables():
    # Connect to an existing database
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    try:
        input_file = open("drop_table.sql", 'r')
    except IOError as e:
        print("I/O Error in string: ", e.strerror)
    command = ""
    for line in input_file:
        command += line
        if line.find(';') != -1:
            #command = format_t(command)+';'
            command = command.replace("\n","")
            #cur.execute(command)
            try:
                cur.execute(command)
                conn.commit()
            except psycopg2.Error as e:
                conn.rollback()
            print(command)
            command = ""
    try:
        input_file = open("create_table_4.sql", 'r')
    except IOError as e:
        print("I/O Error in string: ", e.strerror)
    command = ""
    for line in input_file:
        command += line
        if line.find(';') != -1:
            #command = format_t(command)+';'
            command = command.replace("\n","")
            print(command)
            #cur.execute(command)
            try:
                cur.execute(command)
                conn.commit()
            except psycopg2.Error as e:
                conn.rollback()
            command = ""
    cur.close()
    conn.close()

def insert_Date():
    # Connect to an existing database
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    try:
        input_file = open("import_date.sql", 'r')
    except IOError as e:
        print("I/O Error in string: ", e.strerror)
    """command = ""
    for line in input_file:
        command += line
        if line.find(';') != -1:
            #command = format_t(command)+';'
            command = command.replace("\n","")
            #cur.execute(command)
            try:
                cur.execute(command)
                conn.commit()
            except psycopg2.Error as e:
                conn.rollback()
            print(command)
            command = ""
            """
    c =()
    for line in input_file:

        c = tuple(line[:-1].split('|'))
        try:
            cur.execute("INSERT INTO book (name, genre, quantity_in_stock) VALUES (%s, %s, %s);", c)#[(1, 2, 3), (4, 5, 6), (7, 8, 9)])
            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
    #cur.copy_from("import_date.sql", 'book', columns=('name', 'genre', 'quantity_in_stock'))
    #execute_values(cur, "INSERT INTO test (id, v1, v2) VALUES %s", [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    #cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 ) ");
    #cur.execute("""INSERT INTO some_table (an_int, a_date, a_string) VALUES (%s, %s, %s);""", (10, datetime.date(2005, 11, 18), "O'Reilly"))


def select_book_by_name(book_name):#, book_genre, book_quantity_in_stock, author_first_name, author_middle_name, author_full_name, author_short_name, raiting, count_voted):
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE name = %s ;" , (book_name,))
    return cur.fetchall()


create_Tables()
insert_Date()
#print(select_book_by_name("Собачье сердце"))