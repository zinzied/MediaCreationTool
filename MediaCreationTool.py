import subprocess
from colorama import init, Fore, Style

init(autoreset=True)
def banner():
    print(Fore.GREEN + '''
 #     #                         #####                                             #######                      
 ##   ## ###### #####  #   ##   #       #####  ######   ##   ##### #  ####  #    #    #     ####   ####  #      
 # # # # #      #    # #  #  #  #       #    # #       #  #    #   # #    # ##   #    #    #    # #    # #      
 #  #  # #####  #    # # #    # #       #    # #####  #    #   #   # #    # # #  #    #    #    # #    # #      
 #     # #      #    # # ###### #       #####  #      ######   #   # #    # #  # #    #    #    # #    # #      
 #     # #      #    # # #    # #       #   #  #      #    #   #   # #    # #   ##    #    #    # #    # #      
 #     # ###### #####  # #    #  #####  #    # ###### #    #   #   #  ####  #    #    #     ####   ####  ###### 
                                                                                                                
    ''' + Style.RESET_ALL)

def run_media_creation_tool():
    try:
        # Call the MediaCreationTool.bat script
        subprocess.run(["cmd.exe", "/c", "MediaCreationTool.bat"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    banner()
    choice = input("Do you want to open the Media Creation Tool as a .bat? " + Fore.GREEN + "yes/" + Fore.RED + "no: " + Style.RESET_ALL).strip().lower()
    if choice == 'yes':
        run_media_creation_tool()