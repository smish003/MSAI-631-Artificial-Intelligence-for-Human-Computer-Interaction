import tkinter.messagebox
import webbrowser
import pygame
import time
from functools import partial
from tkinter import ttk
import imdb_recommendation_system as ims
from tkHyperlinkManager import *
import re # to enable the use of regular expressions (regex)

# Adaptive User Profile

user_preferences  ={
    "selected_movies": {},
    "interaction_count": 0
}

# Using Netflix style and setting UI changes
BG_MAIN = "#141414"
BG_PANEL = "#1f1f1f"
RED = "#e50914"
WHITE = "#ffffff"
YELLOW = "#e4b612"
BORDER = "#2a2a2a"
FONT_STYLE= "Georgia"



def play_menu_sound(option):
    """
    :type option: str
    :return: None
    Plays a sound based on the 'option' argument
    """
    if option == 'menu_bar':
        pygame.mixer.music.load('music/button-11.wav')
        pygame.mixer.music.play()
    elif option == 'quit':
        pygame.mixer.music.load('music/quit.wav')
        pygame.mixer.music.play()
        time.sleep(0.3)
        root.destroy()


def open_popup():
    tkinter.messagebox.showinfo('How it Works?', 'Using Cosine Similarity on IMDb dataset!')


# Capturing the User Interaction

def open_link(my_url, movie_title=None):
    """
    Opens the provided URL in the default browser and
    records user interaction for adaptation.
    """
    pygame.mixer.music.load('music/open_browser.wav')
    pygame.mixer.music.play()

    if movie_title:
        # Increment total interaction count
        user_preferences["interaction_count"] += 1

        # Track clicked movie count
        user_preferences["selected_movies"][movie_title] = (
            user_preferences["selected_movies"].get(movie_title, 0) + 1
        )

    webbrowser.open_new(url=my_url)


def get_text(event=None):
    """
    :param event: None
    :return: None
    Gets the recommendations and shows it in a text widget.
    """
    pygame.mixer.music.load('music/button-3.wav')
    pygame.mixer.music.play()
    text_widget = Text(frame, font='Courier 13 italic', cursor='arrow', bg='yellow', height=11, width=60)
    hyperlink = HyperlinkManager(text_widget)
    text_widget.tag_configure('tag-center', justify='center')
    text_widget.tag_configure('tag-left', justify='left')
    query = combo1.get()  # get input from combo widget
    query = ' '.join([word for word in re.split(r'\s+', query) if word != ''])  # handling white space
    text = ims.get_recommendations(query)
    if text is None:  # if the movie/tv show not found print some tips
        text = "Item not found!\n"
        text_widget.insert(1.0, text, 'tag-center')
        text_widget.insert(END, '\nYou can try the following:\n\n 1. Enter keywords and choose from dropdown menu.\n '
                                '2. Check for typos.', 'tag-left')
    else:  # if found iterate over the DataFrame to create hyperlinks in the text widget
        text_widget.delete(1.0, END)  # clear previous entries
        for idx, title, imdb_url in text.itertuples():  # iterating over the DataFrame as tuples
            text_widget.insert(END, title, hyperlink.add(partial(open_link, imdb_url)))  # insert hyperlinks in the
            # widget
            if idx != 9:  # if not the last index, insert a new line after the previous entry
                text_widget.insert(END, '\n')
                text_widget.insert(END, '\n')
    text_widget.config(highlightcolor='black', highlightbackground="black", highlightthickness=2)
    text_widget.place(x=185, y=310)
    # adding scrollbar to the text widget
    scroll_y = Scrollbar(text_widget, orient='vertical', command=text_widget.yview)
    scroll_y.place(x=185*3 + 30, relheight=1)
    text_widget.configure(state='disabled', yscrollcommand=scroll_y.set)  # making the text widget un-editable


# initialize master window
root = Tk()  # creates a window in which we work our gui
root.title("Recommendation System")
root.geometry('960x720')  # width x height
root.resizable(width=False, height=False)  # restricts window size
root.configure(bg=BG_MAIN)
bg_image=PhotoImage(file="images/backgroundimage.png")
bg_label=Label(root,image=bg_image)
bg_label.place(x=0,y=0, relwidth=1, relheight=1)

#  Variable Declaration
selected_movie=StringVar()

selected_button= None
# Creating a netflix style panel
frame= Frame(
    root,
    bg=BG_PANEL,
    width= 760,
    height = 520,
    highlightbackground=BORDER,
    highlightthickness=1
)
frame.place(x=100, y=90)

## Setting the labels
Label(

    frame,
    text= 'Movie Recommendation Sytem',
    font= (FONT_STYLE, 24, "bold"),
    fg=WHITE,
    bg=BG_PANEL
).place(x=160, y=25)

Label(

    frame,
    text= 'Powered by IMDb',
    font= (FONT_STYLE, 16),
    fg=YELLOW,
    bg=BG_PANEL
).place(x=305, y=95)



# Selected Movie


def select_movie(movie,btn):
    global selected_button, select_movie

    selected_movie.set(movie)

    if selected_button:
        selected_button.configure(bg="#2b2b2b")
    btn.configure(bg=YELLOW)
    selected_button = btn

movies= [    
    "Inception", "The Dark Knight", "Titanic",
    "Avatar", "The Matrix", "Gladiator",
    "The Godfather", "Forrest Gump", "Interstellar"

]

x_start = 140
y_start = 140
for i,movie in  enumerate(movies):
    btn= Button(
        frame,
        text=movie,
        width=20,
        height = 3,
        bg= "#615d5d",
        fg=WHITE,
        activebackground=YELLOW,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        
    )
    btn.configure(command=lambda m=movie, b=btn: select_movie(m,b))
    
    btn.place(

    x= x_start + (i%3) *220,
    y=y_start+ (i// 3)*60
)
Button(
    frame,
    text="Recommend",
    font=(FONT_STYLE, 14, "bold"),
    bg=YELLOW,
    fg=WHITE,
    activebackground="#ebeae4",
    relief="flat",
    width=14,
    height=1,
    cursor="hand2",
    command=lambda: show_recommendations()
).place(x=320, y=330)

def show_recommendations():
    movie = selected_movie.get()
    if not movie:
        return

    recommendations = ims.get_recommendations(movie)
    recommendations=ims.adapt_recommendation(recommendations,user_preferences)
    if recommendations is None:
        return

    result_box = Text(
        frame,
        font=("Georgia", 12),
        bg="#111111",
        fg=WHITE,
        height=14,
        width=80,
        highlightbackground=BORDER,
        highlightthickness=1
    )
    result_box.place(x=80, y=380)

    hyperlink = HyperlinkManager(result_box)

    for row in recommendations.itertuples():
        title = row.title
        rating = row.rating
        url = row.urls

        display_text = f"{title}"

        result_box.insert(
            END,
            display_text,
            hyperlink.add(partial(open_link, url, title))
        )
        # Show Rating Out of URL
        result_box.insert(
            END,
            f" Rating ({rating})"
        )
        result_box.insert(END, "\n\n")

    result_box.configure(state="disabled")



# main loop
if __name__ == '__main__':
    pygame.mixer.init()
    root.mainloop()

