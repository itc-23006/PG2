import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))

    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    keyword = sys.argv[2]
    if keyword in mcb_shelf:
        del mcb_shelf[keyword]
        print(f"'{keyword}' has been deleted.")
    else:
        print(f"'{keyword}' not found.")
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    mcb_shelf.clear()
    print("All keywords have been deleted.")

mcb_shelf.close()
