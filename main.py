import pywhatkit as pwk # You need to install this using pip install pywhatkit
def main():
    videoName = input("Search: ")
    pwk.playonyt(videoName) 
    
# calling of main function in exception handling block
try:
    main()
except:
    print("An unexpected error occurred")
finally:
    print("Script closed")
