import webbrowser
with open('my-favorite-links.txt') as file:
    links = file.readlines()
    for link in links:
        webbrowser.open(link)