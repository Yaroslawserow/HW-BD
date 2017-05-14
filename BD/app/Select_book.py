#!/usr/bin/python

import psycopg2
import psycopg2.extras
import string
from random import randint
path = "/home/andrey/Project_BD-master/BD/app/"

def select_book(args):
    list_args = ['book0name', 'autor0full_name', 'book0genre', 'book0quantity_in_stock', 'autor0first_name',
                 'autor0middle_name', 'autor0short_name', 'rating0rating', 'rating0count_voted']
    conn = psycopg2.connect("dbname='testpython' user='matt' host='localhost' password='password'")
    cur = conn.cursor()
    command = """SELECT (book.book_id, autor.full_name, book.name, book.quantity_in_stock, rating.rating, rating.count_voted) FROM (((book
    LEFT JOIN book_autor ON book.book_id = book_autor.book_id)
    LEFT JOIN AUTOR ON book_autor.autor_id = autor.autor_id)
    LEFT JOIN rating ON rating.book_id = book.book_id) WHERE true"""
    #args = [book0name, book0genre, book0quantity_in_stock, author0first_name, author0middle_name, author0full_name, author0short_name, raiting0raiting, raiting0count_voted]
    dict_as_list = zip(list_args,args)
    #print(dict_as_list)
    args_to_execute = []
    for pair in dict_as_list:
        #print(pair)
        if(pair[1] != ''):
            #print(pair)
            s = pair[0]
            command += ' AND '+ s.replace('0','.') + ' = ' + '%s'
            args_to_execute.append(pair[1])
        else:
            pass
            #dict_as_list.remove(pair)

    command += ' ORDER BY rating DESC;'
    #print(command)
    #print(tuple(args))
    if(command.find(';')==len(command)-1):
        try:
            #print(command)
            cur.execute(command, tuple(args_to_execute))
            result= cur.fetchall()
            r = ""
            for line in result:
                r += ((line[0])[1:-1]+"\n")
            return r
        except psycopg2.Error as e:
            conn.rollback()
        return []
    else:
        return ['Не корректный запрос']

#for line in select_book(['','','']):
    #print(line)
