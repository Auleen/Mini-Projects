import sys,webbrowser,pyperclip
sys.argv
if len(sys.argv)>1:
    my_address='+'.join(sys.argv[1:])
else:
    my_address= pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/"+my_address)
