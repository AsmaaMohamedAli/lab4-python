import webbrowser
import random

websites = ["www.google.com", "www.youtube.com", "www.yahoo.com", "www.linkedin.com"]
webbrowser.open_new_tab(random.choice(websites))