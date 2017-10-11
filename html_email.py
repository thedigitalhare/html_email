#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:18:00 2017

@author: The Digital Hare
"""
from bs4 import BeautifulSoup
import re
import webbrowser
import os

def CleanBeautifulSoup(file_path):
    """
    Clean html file
    Return a BeautifulSoup object
    """
    # Open the html file
    file = open(file_path)
    
    # Store its content as a string
    html = file.read()
    
    # Remove html comments
    html = re.sub('<!--.*-->','',html)
    
    # Remove spaces between html tags
    html = re.sub('>\\n*\s*<', '><', html)
    
    # Remove spaces between css properties
    html = re.sub(';\\n*\s*',';',html)
    
    # Create beautiful soup object
    soup = BeautifulSoup(html,"html.parser")
    
    return soup


class HTMLEmail(object):

    # Initializer 
    def __init__(self,
                 background_color = "#F5F5F5",
                 body_background_color = "#FEFEFE"):
        
        self.soup = CleanBeautifulSoup("templates/base.html")
        self.html = repr(self.soup)
    
    def add_full_width_image(self,
                             image_url):
        # Import html tags
        tags = CleanBeautifulSoup("templates/full_width_image.html")
        
        # Modify src link
        tags.img['src'] = image_url
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)
    
    def add_title(self,
                  title,
                  alignment = 'center',
                  family_font = '',
                  font_size = '',
                  color = '',
                  background_color = ''):
        
        # Import html tags
        tags = CleanBeautifulSoup("templates/title.html")
        
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)

    def open_in_browser(self):        
        path = os.path.abspath('temp.html')
        url = 'file://' + path
        with open(path, 'w') as f:
            f.write(self.html)
        webbrowser.open_new_tab(url)
        
        
        