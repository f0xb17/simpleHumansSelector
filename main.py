from os import walk, path

def findFiles(folderPath):
    collectedFiles = []

    for root, dirs, files in walk(folderPath):
        for file in files:
            if file.lower().endswith('.hum'):
                collectedFiles.append(path.join(root, file))

    return collectedFiles


def selectFiles(list):
    print ("Select your .hum files:")
    for i, file in enumerate(list):
        print(f"{ i + 1 }. { file }")

    index = input("Enter the numbers yout want to choose (e.g. 1,2,3): ")
    
    try:
        if index:
            index = [int(id.strip()) - 1 for id in index.split(',')]
            selectedFiles = [list[id] for id in index]
            return selectedFiles
        else:
            raise ValueError
    except ValueError:
        print("Something went wrong")
        return selectFiles(list)

def main():
    folderPath = 'Humans/'
    humans = findFiles(folderPath)

    if humans:
        selection = selectFiles(humans)
        print(f"You selected: { selection }")
    else:
        print("No .hum files found in current context!")


if __name__ == "__main__":
    main()