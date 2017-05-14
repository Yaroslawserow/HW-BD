#!/usr/bin/python

import psycopg2
import psycopg2.extras
import string
from random import randint
path = "/home/andrey/Project_BD-master/BD/app/"


def format_t(input_f):
    """if input_f is not None:
        try:
            input_file = open(input_f, 'r')
        except IOError as e:
            print("I/O Error in string: ", e.strerror)
    else:
        input_file = sys.stdin"""
    input_file = input_f
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
    return se0


def insert_Data():
    # Connect to an existing database
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    try:
        input_file = open(path+"Books1.txt", 'r')
    except IOError as e:
        print("I/O Error in string: ", e.strerror)
    for line in input_file:
        i = 0
        middle_name = ' '
        second_name = ''
        first_name = ''
        genre = ''
        book_name = ''
        line_length = 10000000
        paragraph_spaces = 0
        out = []
        s0 = "',.?!-:'"
        fl = 0
        while i < len(line):
            current = line[i]
            if fl == 0:
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "-" or current == "<" or current == ">":
                    out.append(' ' * paragraph_spaces + current)
                    fl = 1
                elif s0.find(current) != -1:
                    fl = 2
                elif current == ' ':
                    fl = 0
                elif ord(current) == 10:
                    fl = 0
            elif fl == 1:
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "-" or current == "<" or current == ">":
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
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "-" or current == "<" or current == ">":
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
                if current.isalnum() or current.isalpha() or current == '(' or current == ')' or current == "-" or current == "<" or current == ">":
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
        i = 0
        for word in out:
            if i==0:
                i +=1
                if(word[-1] != ")"):
                    second_name = word
                    continue
                else:
                    i += 3
            elif i==1:
                i+=1
                if(word[-1] != ")"):
                    first_name = word
                    continue
                else:
                    i += 2
            elif i==2:
                if (word[-1] != ")"):
                    middle_name +=(word + ' ')
                    continue
                else:
                    i += 1
            elif i == 3:
                if(word[0] != "<"):
                    genre +=(' ' + word)
                else:
                    book_name = word[1:]
                    i += 1
            elif i == 4:
                book_name += ' ' + word
        book_name = book_name[:-1]
        c = (book_name, genre[1::], randint(0,1000),)
        cur.execute("SELECT book_id FROM book WHERE name = %s;", (book_name,))
        book_id = cur.fetchall()
        if book_id == []:
            try:
                cur.execute("INSERT INTO book (name, genre, quantity_in_stock) VALUES (%s, %s, %s);", c)
                conn.commit()
            except psycopg2.Error as e:
                print(e)
                conn.rollback()
                continue
            c = (book_name, genre[1::], randint(0,1000),)
            cur.execute("SELECT book_id FROM book WHERE name = %s;", (book_name,))
            book_id = cur.fetchall()
            cur.execute("INSERT INTO rating (book_id, rating, count_voted) VALUES (%s, %s, %s);", (book_id[0][0], randint(0,1000)/100, randint(0, 1000)))
            conn.commit()
        book_id = book_id[0][0]
        full_name = first_name + ' ' + middle_name + ' ' + second_name
        full_name = format_t(full_name)
        c = (first_name, second_name, middle_name[1:-1], full_name,)
        cur.execute("SELECT autor_id FROM autor WHERE full_name = %s;", (full_name,))
        autor_id = cur.fetchall()
        if autor_id == []:
            try:
                cur.execute("INSERT INTO autor (first_name, second_name, middle_name, full_name) VALUES (%s, %s, %s, %s);", c)
                conn.commit()
            except psycopg2.Error as e:
                print(e)
                conn.rollback()
                continue
            cur.execute("SELECT autor_id FROM autor WHERE full_name = %s;", (full_name,))
            autor_id = cur.fetchall()
        autor_id = autor_id[0][0]
        c=(book_id, autor_id,)
        try:
            cur.execute("INSERT INTO book_autor (book_id, autor_id) VALUES (%s, %s);", c)
            conn.commit()
        except psycopg2.Error as e:
            print(e)
            conn.rollback()
            continue
        #cur.copy_from("import_date.sql", 'book', columns=('name', 'genre', 'quantity_in_stock'))
    #execute_values(cur, "INSERT INTO test (id, v1, v2) VALUES %s", [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    #cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 ) ");
    #cur.execute("""INSERT INTO some_table (an_int, a_date, a_string) VALUES (%s, %s, %s);""", (10, datetime.date(2005, 11, 18), "O'Reilly")
