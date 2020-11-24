while True:
    try:
        copa = input()
        if copa == "": break
        copa = int(copa)
        if copa > 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except EOFError:
        break