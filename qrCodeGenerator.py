# Implementing an script that generates QR code based on a given URL.
# -----------------   TO DO: Use GUI library for the User interface of the app -----------------------
import subprocess
import sys

def install(package, note):
    """
    Installs the package passed with pip install via a subprocess or terminates the execution
    Returns true if it was installed
    """
    inst = "m"

    # We keep asking for a valid input until it is given.
    while inst != "1" and inst != "2":
        print("Please answer with '1' (Yes) or '2' (No, and 0 to exit program)")
        inst = input("It seems you don't have "+package + " (" + note + ") "+" installed yet, do you want to install it?: ")

        # Exits the program
        if inst == "0":
            print("Program terminated.")
            sys.exit(0)

    # If they want to install
    if inst == "1":
        # We inform that we are installing the lib
        print("Installing " + package + "...")

        # Subsystem call
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package])

    elif inst == "2":
        # We inform that we are not installing the lib and as warning that without it, it won't work
        print("Skipping " + package +
              " install... (Remember that if you didn't install it yet, it will give an error).")


def checkInstalls():
    """
    We try to include de library, managing the exception in which the user failed to install them then
    We define the URL linked to QR code, ask for where they want to save the file and generate it and save the QR code resulted
    """
    # Lib import
    installed = False
    matInstalled = False
    try:
        import pyqrcode
        installed = True
    except Exception:
        exception(
            "You didn't install the required libraries! (Try again or exit)")

    return installed, pyqrcode


def createQR(pyqrcode):
    """
    We create thee QR based on the link the user will give
    and place it in the path they choose.
    If matplot was installed, it also shows the image
    """

    # QR code creation
    url = input("Input the URL you want to be directed to with the QR code: ")
    path = input(
        "Type folder with the relative or absolute path where you want to save it: ")
    qr = pyqrcode.create(url)

    # We create and open the image so the user can check it works fine if they choose to
    try:
        qr.png(path+"myQR.png", scale=6)
    except Exception:
        exception("You didn't write a correct path!")
        createQR(pyqrcode)

    # We check if matplot was installed so we can show the image, if not we dont show
    try:
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        img = mpimg.imread(path+"myQR.png")
        imgplot = plt.imshow(img)
        plt.show()
    except Exception:
        install("matplotlib", "OPTIONAL, to check the resulted QR")
        try:
            import matplotlib.pyplot as plt
            import matplotlib.image as mpimg
            img = mpimg.imread(path+"myQR.png")
            imgplot = plt.imshow(img)
            plt.show()
        except:
            pass

def exception(message):
    """
    Catchs the exception and prints a message of warning, giving the option of trying again
    """
    # We inform them about the error
    print(" -- ERROR -- " + message)

    # We give the option of retrying or leave
    retry = input("Write 0 to exit, anything else to retry: ")
    if retry == "0":
        sys.exit(0)


def main():
    # We try to install pyqrcode if it is not installed and import them
    sent = True
    while sent:
        # First we check if they are already installed
        sent, pyqrcode = checkInstalls()

        # If they are not, then we try to install them again
        if not sent:
            install("pyqrcode", "REQUIRED, creates QR")
        else:
            sent = False

    # We create a loop in case they want to create more than 1 QR code
    sent = "1"
    while sent == "1":
        # We create the QR code based on a URL and path input by user
        createQR(pyqrcode)

        # We inform that the QR was successfully created and terminate the program
        print("The QR code was successfully created!")
        sent = input(
            "Do you want to create another QR Code? (Type '1' to do it, anything else to exit the program): ")

    sys.exit(0)


if __name__ == '__main__':
    main()
