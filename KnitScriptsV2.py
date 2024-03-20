#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 07:54:10 2024

@author: zackreardon
"""

# importing necessary packages
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import sqlite3
from sqlite3 import Error
import datetime
import os
import pandas as pd

# initializing database
def setup_database():

    # function to create connection to sqlite database
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn
    
    # function to create a new table in database
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
        return
    
    # creating database
    current_folder = os.path.dirname(os.path.abspath(__file__))
    db_name = os.path.basename(__file__).split(".")[0] + ".db"
    conn = create_connection(current_folder + "/" + db_name)
    
    # creating tables in database
    if conn is not None:
        
        create_table(conn,
                         '''CREATE TABLE IF NOT EXISTS KnitGauge (
                         timestamp text NOT NULL,
                         first_Gauge_Stitch_Count integer,
                         first_Gauge_Row_Count integer,
                         second_Gauge_Stitch_Count integer,
                         second_Gauge_Row_Count integer,
                         Row_or_Stitch_Value integer NOT NULL,
                         Rows_or_Stitches text NOT NULL,
                         Output text NOT NULL
                         );'''
                     )
    
        create_table(conn,
                         '''CREATE TABLE IF NOT EXISTS YarnConverter (
                         timestamp text NOT NULL,
                         Yarn_1_Weight integer NOT NULL,
                         Yarn_1__Weight_Unit text NOT NULL,
                         Yarn_1_Length integer NOT NULL,
                         Yarn_1_Length_Unit text NOT NULL,
                         Yarn_2_Weight integer NOT NULL,
                         Yarn_2__Weight_Unit text NOT NULL,
                         Yarn_2_Length integer NOT NULL,
                         Yarn_2_Length_Unit text NOT NULL,
                         Output text NOT NULL
                         );'''
                     )
        
    return conn

def main():
    
    # function to add KnitGauge data to table
    def add_knit_gauge_data(conn, knit_gauge_data):
        sql = '''INSERT INTO KnitGauge (timestamp, first_Gauge_Stitch_Count, first_Gauge_Row_Count, second_Gauge_Stitch_Count, second_Gauge_Row_Count, Row_or_Stitch_Value, Rows_or_Stitches, Output)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, knit_gauge_data)
        conn.commit()
        return cur.lastrowid
    
    # function to add YarnConverter data to table
    def add_yarn_converter_data(conn, yarn_converter_data):
        sql = '''INSERT INTO YarnConverter (timestamp, Yarn_1_Weight, Yarn_1__Weight_Unit, Yarn_1_Length, Yarn_1_Length_Unit, Yarn_2_Weight, Yarn_2__Weight_Unit, Yarn_2_Length, Yarn_2_Length_Unit, Output)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, yarn_converter_data)
        conn.commit()
        return cur.lastrowid
    
    # constructing GUI
    root = tk.Tk()
    root.title("KnitScripts")
    l1 = ttk.Label(text = "KnitScripts", foreground = "red", font = ("Noteworthy", 50))
    l1.grid(row = 0, column = 1, sticky = "nsew", padx = 50)
    
    f1 = ttk.Frame(root)
    l2 = ttk.Label(f1, text = "KnitGauge", foreground = "blue", font = ("Noteworthy", 18))
    l3 = ttk.Label(f1, text = "YarnConverter", foreground = "green", font = ("Noteworthy", 18))
    f1.grid(row = 1, column = 1, sticky = "nsew", padx = 20)
    l2.pack(side = "left")
    l3.pack(side = "right")
    
    f2 = ttk.Frame(root)
    l4 = ttk.Label(f2, text = "1st Gauge Stitch Count")
    l5 = ttk.Label(f2, text = "Yarn 1 Weight")
    f2.grid(row = 2, column = 1, sticky = "nsew", padx = 20)
    l4.pack(side = "left")
    l5.pack(side = "right")
    
    f3 = ttk.Frame(root)
    e1 = ttk.Entry(f3, width = 10)
    e2 = ttk.Entry(f3, width = 10)
    f3.grid(row = 3, column = 1, sticky = "nsew", padx = 20)
    e1.pack(side = "left")
    e2.pack(side = "right")
    
    f4 = ttk.Frame(root)
    l6 = ttk.Label(f4, text = "1st Gauge Row Count")
    om1_selection = tk.StringVar()
    om1 = ttk.OptionMenu(f4, om1_selection, "Select", "Grams", "Ounces")
    f4.grid(row = 4, column = 1, sticky = "nsew", padx = 20)
    l6.pack(side = "left")
    om1.pack(side = "right")
    
    f5 = ttk.Frame(root)
    e3 = ttk.Entry(f5, width = 10)
    l7 = ttk.Label(f5, text = "Yarn 1 Length")
    f5.grid(row = 5, column = 1, sticky = "nsew", padx = 20)
    e3.pack(side = "left")
    l7.pack(side = "right")
    
    f6 = ttk.Frame(root)
    l8 = ttk.Label(f6, text = "2nd Gauge Stitch Count")
    e4 = ttk.Entry(f6, width = 10)
    f6.grid(row = 6, column = 1, sticky = "nsew", padx = 20)
    l8.pack(side = "left")
    e4.pack(side = "right")
    
    f7 = ttk.Frame(root)
    e5 = ttk.Entry(f7, width = 10)
    om2_selection = tk.StringVar()
    om2 = ttk.OptionMenu(f7, om2_selection, "Select", "Meters", "Yards")
    f7.grid(row = 7, column = 1, sticky = "nsew", padx = 20)
    e5.pack(side = "left")
    om2.pack(side = "right")
    
    f8 = ttk.Frame(root)
    l9 = ttk.Label(f8, text = "2nd Gauge Row Count")
    l10 = ttk.Label(f8, text = "Yarn 2 Weight")
    f8.grid(row = 8, column = 1, sticky = "nsew", padx = 20)
    l9.pack(side = "left")
    l10.pack(side = "right")
    
    f9 = ttk.Frame(root)
    e6 = ttk.Entry(f9, width = 10)
    e7 = ttk.Entry(f9, width = 10)
    f9.grid(row = 9, column = 1, sticky = "nsew", padx = 20)
    e6.pack(side = "left")
    e7.pack(side = "right")
    
    f10 = ttk.Frame(root)
    l11 = ttk.Label(f10, text = "Row or Stitch Value")
    om3_selection = tk.StringVar()
    om3 = ttk.OptionMenu(f10, om3_selection, "Select", "Grams", "Ounces")
    f10.grid(row = 10, column = 1, sticky = "nsew", padx = 20)
    l11.pack(side = "left")
    om3.pack(side = "right")
    
    f11 = ttk.Frame(root)
    e8 = ttk.Entry(f11, width = 10)
    l12 = ttk.Label(f11, text = "Yarn 2 Length")
    f11.grid(row = 11, column = 1, sticky = "nsew", padx = 20)
    e8.pack(side = "left")
    l12.pack(side = "right")
    
    f12 = ttk.Frame(root)
    om4_selection = tk.StringVar()
    om4 = ttk.OptionMenu(f12, om4_selection, "Select", "Stitches", "Rows")
    e9 = ttk.Entry(f12, width = 10)
    f12.grid(row = 12, column = 1, sticky = "nsew", padx = 20)
    om4.pack(side = "left")
    e9.pack(side = "right")
    
    f13 = ttk.Frame(root)
    om5_selection = tk.StringVar()
    om5 = ttk.OptionMenu(f13, om5_selection, "Select", "Meters", "Yards")
    f13.grid(row = 13, column = 1, sticky = "nsew", padx = 20)
    om5.pack(side = "right")
    
    f14 = ttk.Frame(root)
    f15 = ttk.Frame(root)
    
    def run_knit_gauge():
        
        timestamp = str(datetime.datetime.now().astimezone()).replace(" ", "T")
            
        if om4_selection.get() == "Stitches":
            inches = float(e8.get()) / float(e1.get())
            return_info = str(round(inches * float(e5.get()), 1)) + " stitches"
            
        elif om4_selection.get() == "Rows":
            inches = float(e8.get()) / float(e3.get())
            return_info = str(round(inches * float(e6.get()), 1)) + " rows"
            
        l13["text"] = "\n" + return_info + "\n"
        
        # passing info to database
        knit_gauge_data = (timestamp, e1.get(), e3.get(), e5.get(), e6.get(), e8.get(), om4_selection.get(), return_info)
        add_knit_gauge_data(conn, knit_gauge_data)
        
        return
            
    b1 = ttk.Button(f13, text = "Run", command = run_knit_gauge, width = 7)
    b1.pack(side = "left")
            
    def run_multi_yarn_converter():
        
        timestamp = str(datetime.datetime.now().astimezone()).replace(" ", "T")
            
        if om1_selection.get() == "Ounces":
            yarn_1_weight = float(e2.get()) * 28.3495
        elif om1_selection.get() == "Grams":
            yarn_1_weight = float(e2.get())
        if om3_selection.get() == "Ounces":
            yarn_2_weight = float(e7.get()) * 28.3495
        elif om3_selection.get() == "Grams":
            yarn_2_weight = float(e7.get())
            
        if om2_selection.get() == "Yards":
            yarn_1_length = float(e4.get()) * 0.9144
        elif om2_selection.get() == "Meters":
            yarn_1_length = float(e4.get())
        if om5_selection.get() == "Yards":
            yarn_2_length = float(e9.get()) * 0.9144
        elif om5_selection.get() == "Meters":
            yarn_2_length = float(e9.get())
                
        ratio_1 = yarn_1_length / yarn_1_weight
        ratio_2 = yarn_2_length / yarn_2_weight
            
        weight_length = (100 * max(ratio_1, ratio_2)/(1 + max(ratio_1, ratio_2)/min(ratio_1, ratio_2)))
            
        if weight_length > 500:
            category = "lace\n(US 000-1)"
        elif 400 <= weight_length < 500:
            category = "super fine\n(US 1-3)"
        elif 300 <= weight_length < 400:
            category = "fine\n(US 3-5)"
        elif 240 <= weight_length < 300:
            category = "light\n(US 5-7)"
        elif 120 <= weight_length < 240:
            category = "medium\n(US 7-9)"
        elif 100 <= weight_length < 120:
            category = "bulky\n(US 9-11)"
        elif weight_length < 100:
            category = "super bulky\n(US 11-17)"
        
        l13["text"] = str(int(weight_length)) + "m/100g\n" + category
        
        # passing info to database
        yarn_converter_data = (timestamp, e2.get(), om1_selection.get(), e4.get(), om2_selection.get(), e7.get(), om3_selection.get(), e9.get(), om5_selection.get(), l13["text"].replace("\n", " "))
        add_yarn_converter_data(conn, yarn_converter_data)
        
        return
        
    b2 = ttk.Button(f14, text = "Run", command = run_multi_yarn_converter, width = 7)
    f14.grid(row = 14, column = 1, sticky = "nsew", padx = 20)
    b2.pack(side = "right")
    
    l12 = ttk.Label(f15, text = "Output", font = ("Noteworthy", 18))
    f15.grid(row = 15, column = 1, sticky = "nsew", padx = 20)
    l12.pack()
    
    
    f16 = ttk.Frame(root)
    f17 = ttk.Frame(root)
    
    l13 = ttk.Label(f16, text = "\n\n", borderwidth = 2, relief = "solid", width = 10, anchor = "n", justify = tk.CENTER)
    f16.grid(row = 16, column = 1, sticky = "nsew", padx = 20)
    l13.pack()
    
    b3 = ttk.Button(f17, text = "Quit", command = root.destroy, width = 7)
    l14 = ttk.Label(f17, text = "")
    f17.grid(row = 20, column = 1, sticky = "nsew", padx = 20)
    l14.pack(side = "top")
    b3.pack(side = "bottom")
    
    def query_database():
        
        # obtaining path to user's downloads folder
        if os.name == "nt":
            download_folder = f"{os.getenv('USERPROFILE')}\\Downloads"
        else:  # PORT: For *Nix systems
            download_folder = f"{os.getenv('HOME')}/Downloads"
        
        query_name = str(datetime.datetime.now().astimezone()).replace(" ", "T") + os.path.basename(__file__).split(".")[0] + "query.xlsx"
        
        writer = pd.ExcelWriter(download_folder + "/" + query_name)
        
        # obtaining available tables to query
        cur = conn.cursor()
        query = cur.execute("SELECT * FROM sqlite_master WHERE type='table'")
        rows = cur.fetchall()
        tables = [table[1] for table in rows]
        
        # obtaining data from available tables
        for table in tables:
            query = cur.execute("SELECT * FROM {}".format(table))
            rows = cur.fetchall()
            column_names = [e[0] for e in query.description]
            df = pd.DataFrame(rows, columns = column_names)
            df.to_excel(writer, sheet_name = table, index = False)
        
        writer.close()
        
        return
    
    f18 = ttk.Frame(root)
    
    b4 = ttk.Button(f18, text = "Query", command = query_database, width = 10)
    f18.grid(row = 19, column = 1, sticky = "nsew", padx = 20)
    b4.pack(side = "bottom")
    
    root.mainloop()
    
    return

if __name__ == "__main__":
    
    conn = setup_database()
    
    main()
