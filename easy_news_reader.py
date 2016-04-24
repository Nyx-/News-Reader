



#-----Task Description-----------------------------------------------#
#
#  EASY NEWS READER
#
#  There are many Web sites that give you lists of news stories or
#  similar regularly-updated information.  Here you will create an
#  application that makes it easy to read the stories on such a page
#  by presenting them to the user one at a time, via an intuitive
#  Graphical User Interface.  See the instruction sheet accompanying
#  this file for full details.
#
#--------------------------------------------------------------------#



#----------
#
# Import the various functions needed to complete this program.
# NB: You may NOT import or use code from any other module
# in your solution.  Also, you do NOT need to use all these
# functions in your solution.

# Import the function for fetching web documents and images
from urllib import urlopen 

# Import all the Tkinter GUI functions
from Tkinter import *

# Import the regular expression search function
from re import findall

# Import the scrolled text widget (Optional - you
# do not need to use this, a standard Text
# widget is adequate)
from ScrolledText import ScrolledText
#
#----------

# Retrieve, open and read the url
url = 'http://www.polygon.com/news'

page = urlopen(url)

html_page = page.read()

page.close()

# Replacing unwanted text within the html page
html_spaced = html_page.replace("\r\n", " ")
html_spaced = html_spaced.replace("\xc2\xa0", " ")
html_spaced = html_spaced.replace("\xe2\x80\x94", "-")
html_spaced = html_spaced.replace("\xe2\x80\x93", "-")
html_spaced = html_spaced.replace("\xe2\x80\x99", "'")
html_spaced = html_spaced.replace("&nbsp;", " ")

# Finding the date, writer, title and description to insert into the text box
date = findall('<span class="long_date">\n +(.+)\n +</span>', html_page) 
writer = findall('<p class="byline">\n +By <a href=".+">(.+)</a>', html_page) 
title = findall('<h2><a href=".+">(.+)</a>', html_spaced) 
description = findall('<div class="copy">\n +(.+) *\n ?[\n]?[</div>]?', html_spaced)

# Setting the values of the two global variables used
page = 0
value = -1


##-------------------------------------##


# Defining the next button function to insert into the scroll text box
# and change page number
def next_button():
    global page
    if page == len(date):
        page = 1
    else:
        page += 1
    page_number['text'] = str(page)
    global value
    if value == len(date) - 1:
        value = 0
    else:
        value = value + 1
    news_box.delete(0.0, END)
    news_box.insert(END, 'Published ' + date[value] + '\n')
    news_box.insert(END, 'By ' + writer[value] + '\n' + '\n' + '\n')
    news_box.insert(END, title[value] + '\n' + '\n')
    news_box.insert(END, description[value] + '\n' + '\n')
    window.title('In Recent Gaming News... ' + title[value])

# Defining the previous button function to insert into the scroll text box
# and change page number
def prev_button():
    global page
    if page == 0 or page == 1:
        page = len(date)
    else:
        page -= 1
    page_number['text'] = str(page)
    global value
    if value == 0 or value == -1:
        value = len(date) - 1
    else:
        value = value - 1
    news_box.delete(0.0, END)
    news_box.insert(END, 'Published ' + date[value] + '\n')
    news_box.insert(END, 'By ' + writer[value] + '\n' + '\n' + '\n')
    news_box.insert(END, title[value] + '\n' + '\n')
    news_box.insert(END, description[value] + '\n' + '\n')
    window.title('In Recent Gaming News... ' + title[value])


##-------------------------------------##


# Create the window
window = Tk()
window.title('In Recent Gaming News...')
window.geometry("1300x520")
window.configure(background = 'white')

# Create and Insert the scrolling text box
news_box = ScrolledText(window, width = 60, height = 15, borderwidth = 2,
                        bg = 'slateblue', wrap = "word", foreground = 'white',
                        font = ('calibri', 16))
news_box.grid(row = 3, column = 2, rowspan = 2)

# Create and Insert the 'next button'
next_but = Button(window, text = 'Next >', width = 10, command = next_button)
next_but.grid(row = 4, column = 8)

# Create and Insert the 'previous button'
prev_but = Button(window, text = '< Previous', width = 10, command = prev_button)
prev_but.grid(row = 4, column = 6)

# Create and Insert page numbers (inbetween the buttons)
page_number = Label(window, text = ' ', width = 10, bg = 'white',
                    font = ("Arial", 18, "bold"))
page_number.grid(row = 4, column = 7)

# Import and display the image
img = urlopen("http://24.media.tumblr.com/567cc58bece83e7687df11a5f7e8df17/tumblr_mx14as6o5i1sl6vmto1_500.gif")\
        .read().encode('base64', 'strict')
photo = PhotoImage(data = img)
Picture = Label(window, image = photo, bg = 'white')
Picture.grid(row = 2, column = 6, rowspan = 2, columnspan = 3)

# Create and Insert the title on the page
Title = Label(window, text = 'RECENT GAMING NEWS', font = ("Arial", 48, "bold"),
              bg = 'white')
Title.grid(row = 1, column = 2, pady = 10, padx = 5)

# Create and Insert text about the website, under the buttons
Site = Label(window, text = 'Find out more at www.polygon.com/news',
             font = ("Arial", 10, "bold"), bg = 'white')
Site.grid(row = 5, column = 6, columnspan = 3)

#Insert the initial text into the scrolled text box    
news_box.insert(END, '\n\n\n\n\n\n\n' + '  Click through the ' + str(len(date)) +
                ' latest gaming news stories from Polygon.com ...')


window.mainloop()


#
#--------------------------------------------------------------------#
