def problems():
    try:
        choice = int(input("""Please select an option
            1.Broken Tool
            2.Lost Tool
            3.Stolen Tool: """))    # Input choice
        if choice == 1:
            print("Okay we will inform insurance company as well as owner")
        elif choice == 2:
            print("Okay we will inform insurance company as well as owner")
        elif choice == 3:
            print("Okay we will inform insurance company as well as owner but did you already informed police ?")
    except ValueError:
        return
