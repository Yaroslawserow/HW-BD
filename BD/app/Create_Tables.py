#!/usr/bin/python

import psycopg2
import psycopg2.extras
import string
from random import randint
#from app.Select_book import select_book
from app.insert_data import insert_Data

path = "/home/andrey/Project_BD-master/BD/app/"


def create_Tables():
    # Connect to an existing database
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    try:
        input_file = open(path+"drop_table.sql", 'r')
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
            #print(command)
            command = ""
    try:
        input_file = open(path+"create_table_4.sql", 'r')
    except IOError as e:
        print("I/O Error in string: ", e.strerror)
    command = ""
    for line in input_file:
        command += line
        if line.find(';') != -1:
            #command = format_t(command)+';'
            command = command.replace("\n","")
            #print(command)
            #cur.execute(command)
            try:
                cur.execute(command)
                conn.commit()
            except psycopg2.Error as e:
                print(e)
                conn.rollback()
            command = ""
    cur.close()
    conn.close()
    print("Tables create")
    insert_Data()
    print("Data insert")


"""
def select_book_by_name(book_name):#, book_genre, book_quantity_in_stock, author_first_name, author_middle_name, author_full_name, author_short_name, raiting, count_voted):
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE true AND name = %s;" , (book_name,))
    return cur.fetchall()
"""

#create_Tables()
#for line in select_book(['','Джоан Роулинг', '']):# здесь нужны аргументы из всех полей, даже пустых, но мне лень
#    print(line[0])
