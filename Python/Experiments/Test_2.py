# Develop a program that picks up current path of execution and creates a file= .\Concepts\<InputFromUser>\<InputFromUser>.py

import os
import sys

FOLDERNAME = "Concepts"

def main() -> None:
    Args = sys.argv[1:]
    Concept: str= ""
    Cwd: str = os.path.dirname(__file__) 

    '''
    os.path.abspath() = Gets the absolute path of the file being executed -->  Since __file__ already returns the abspath this is redundant
    os.path.dirname() = Gets the absolute path of the directory that contains the file being executed
    '''

    BasePath: str = Cwd

    if len(Args):  
        if len(Args) > 1:
            print(f"INFO: Taking the first input. Lets take one step at a time!")
            Concept = str(Args[0])
            print(f"INFO: The concept for the day -> '{Concept}'")
        else:
            Concept = str(Args[0])
            print(f"INFO: The concept for the day -> '{Concept}'")
            
    else:
        raise RuntimeError(f"Enter A Concept name that you plan on learning today!")

    CreatePlaceholderFileFromUserInput(BasePath, Concept)

def CreatePlaceholderFileFromUserInput(Path: str, FileName: str) -> None:
    try:
        FolderPath: str = os.path.join(Path,FOLDERNAME,FileName)
        os.makedirs(FolderPath)
    except FileExistsError as err:
        print(f"INFO: '{FolderPath}' already exists!")
    except PermissionError as err:
        raise PermissionError(f"Permission Denied! Cannot create folder '{FolderPath}'!")
    except Exception as err:
        raise Exception(err)

    File: str = os.path.join(FolderPath,FileName + ".py")

    if os.path.exists(File):
        print(f"INFO: The placeholder concept file already exists. Let us begin!")

    else:
        try:
            with open(file= File, mode= 'w') as f:
                f.write(f"# placeholder.py created!")
            
            print(f"INFO: Directory created. Let us begin!")

        except Exception as err:
            raise Exception(f"Encountered an error while creating the placeholder file: {err}")

if __name__ == "__main__":
    main()


