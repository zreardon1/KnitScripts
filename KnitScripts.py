#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 07:54:10 2024

@author: zackreardon
"""

# importing necessray packages
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *

def main():
    
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
            
        if om4_selection.get() == "Stitches":
            inches = float(e8.get()) / float(e1.get())
            return_info = str(round(inches * float(e5.get()), 1)) + " stitches"
            
        elif om4_selection.get() == "Rows":
            inches = float(e8.get()) / float(e3.get())
            return_info = str(round(inches * float(e6.get()), 1)) + " rows"
            
        l13["text"] = "\n" + return_info + "\n"
            
    b1 = ttk.Button(f13, text = "Run", command = run_knit_gauge, width = 7)
    b1.pack(side = "left")
            
    def run_multi_yarn_converter():
            
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
    f17.grid(row = 19, column = 1, sticky = "nsew", padx = 20)
    l14.pack(side = "top")
    b3.pack(side = "bottom")
    
    root.mainloop()
    
    return

if __name__ == "__main__":
    main()