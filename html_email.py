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
                  font_family = 'Helvetica',
                  font_size = '42px',
                  color = '#1A1A1A',
                  background_color = '#FEFEFE'):
        
        # Import html tags
        tags = CleanBeautifulSoup("templates/title.html")
        
        # Modify the title
        tags.h1.string = title
        
        # Modify the aligmnent
        tags.h1['style'] = re.sub(
                pattern = 'text-align:center',
                string = tags.h1['style'],
                repl = 'text-align:' + alignment)
        
        # Modify the family font
        tags.h1['style'] = re.sub(
                pattern = 'font-family:Helvetica',
                string = tags.h1['style'],
                repl = 'font-family:' + font_family)
        
        # Modify the font size
        tags.h1['style'] = re.sub(
                pattern = 'font-size:[0-9]+px',
                string = tags.h1['style'],
                repl = 'font-size:' + font_size)
        
        # Modify the color
        tags.h1['style'] = re.sub(
                pattern = 'color:#1A1A1A',
                string = tags.h1['style'],
                repl = 'color:' + color)
        
        # Modify the background-color
        tags.table['style'] = re.sub(
                pattern = 'background:#fefefe',
                string = tags.table['style'],
                repl = 'background:' + background_color)
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)
        
    
    def add_one_stats(self,
                      stat_metric1,
                      stat_value1,
                      background_color = '#fefefe',
                      stat_metric_color = '',
                      stat_metric_font = '',
                      stat_metric_font_size = '',
                      stat_value_color = '',
                      stat_value_font = '',
                      stat_value_fontsize = ''):
        
        # Import html tags
        tags = CleanBeautifulSoup("templates/one_stats.html")
        
        # Modify the stat_metrics and stat_values
        tags.find("h6", { "class" : "stat-metric1" }).string = stat_metric1
        tags.find("h4", { "class" : "stat-value1" }).string = stat_value1
        
        # Modify the background-color
        tags.table['style'] = re.sub(
                pattern = 'background:#fefefe',
                string = tags.table['style'],
                repl = 'background:' + background_color)
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)
    
    
    def add_two_stats(self,
                      stat_metric1,
                      stat_value1,
                      stat_metric2,
                      stat_value2,
                      background_color = '#fefefe',
                      stat_metric_color = '',
                      stat_metric_font = '',
                      stat_metric_font_size = '',
                      stat_value_color = '',
                      stat_value_font = '',
                      stat_value_fontsize = ''):
        
        # Import html tags
        tags = CleanBeautifulSoup("templates/two_stats.html")
        
        # Modify the stat_metrics and stat_values
        tags.find("h6", { "class" : "stat-metric1" }).string = stat_metric1
        tags.find("h4", { "class" : "stat-value1" }).string = stat_value1
        tags.find("h6", { "class" : "stat-metric2" }).string = stat_metric2
        tags.find("h4", { "class" : "stat-value2" }).string = stat_value2
        
        # Modify the background-color
        tags.table['style'] = re.sub(
                pattern = 'background:#fefefe',
                string = tags.table['style'],
                repl = 'background:' + background_color)
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)
        
    def add_three_stats(self,
                      stat_metric1,
                      stat_value1,
                      stat_metric2,
                      stat_value2,
                      stat_metric3,
                      stat_value3,
                      background_color = '#fefefe',
                      stat_metric_color = '',
                      stat_metric_font = '',
                      stat_metric_font_size = '',
                      stat_value_color = '',
                      stat_value_font = '',
                      stat_value_fontsize = ''):
        
        # Import html tags
        tags = CleanBeautifulSoup("templates/three_stats.html")
        
        # Modify the stat_metrics and stat_values
        tags.find("h6", { "class" : "stat-metric1" }).string = stat_metric1
        tags.find("h4", { "class" : "stat-value1" }).string = stat_value1
        tags.find("h6", { "class" : "stat-metric2" }).string = stat_metric2
        tags.find("h4", { "class" : "stat-value2" }).string = stat_value2
        tags.find("h6", { "class" : "stat-metric2" }).string = stat_metric2
        tags.find("h4", { "class" : "stat-value2" }).string = stat_value2
        
        # Modify the background-color
        tags.table['style'] = re.sub(
                pattern = 'background:#fefefe',
                string = tags.table['style'],
                repl = 'background:' + background_color)
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)
    
    def add_spacer(self,
                   height = '16px',
                   background_color = '#F5F5F5'):
        
         # Import html tags
        tags = CleanBeautifulSoup("templates/spacer.html")
        
        # Modify the spacer height 
        tags.table.table.td['height'] = height
        tags.table.table.td['style'] = re.sub(
                pattern = 'line-height:16px',
                string = tags.table.table.td['style'],
                repl = 'line-height:' + height)
        
        # Modify the background-color
        tags.table['style'] = re.sub(
                pattern = 'background:#fefefe',
                string = tags.table['style'],
                repl = 'background:' + background_color)
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)
        
    def add_text(self,
                   text,
                   background_color = '#FEFEFE'):
        
         # Import html tags
        tags = CleanBeautifulSoup("templates/text.html")
        
        # Modify the text
        tags.p.string = text
        
        # Modify the background-color
        tags.table['style'] = re.sub(
                pattern = 'background:#fefefe',
                string = tags.table['style'],
                repl = 'background:' + background_color)
        
        # Append new tags
        self.soup.find("center", { "class" : "main_body" }).append(tags)
        
        # Update html
        self.html = repr(self.soup)
    
    def add_three_features(self,
                           background_color = '#FEFEFE'):
        
        # Import html tags
        tags = CleanBeautifulSoup("templates/three_features.html")
        
        # Modify the background-color
        tags.table['style'] = re.sub(
                pattern = 'background:#fefefe',
                string = tags.table['style'],
                repl = 'background:' + background_color)
        
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
        

text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad earum ducimus, non, eveniet neque dolores voluptas architecto sed, voluptatibus aut dolorem odio. Cupiditate a recusandae, illum cum voluptatum modi nostrum.'


email = HTMLEmail()
email.add_full_width_image("http://via.placeholder.com/350x150")
email.add_spacer(height = '40px')
email.add_title(title = "Test")
email.add_one_stats("Metric","32,647")
email.add_three_features()
email.add_text(text = text)
email.open_in_browser()
        
        
        
        
        
        