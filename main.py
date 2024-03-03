from os import walk, path

def collectHumFiles(folderPath):
    humans = []

    for root, dirs, files in walk(folderPath):
        for file in files:
            if file.lower().endswith('.hum'):
                humans.append(path.join(root, file))

    return humans


def selectHumans(humanList):
    print ("Select your .hum files:")
    for i, file in enumerate(humanList):
        print(f"{ i + 1 }. { file }")

    try:
        choice = int(input("Enter the number you want to add: ")) - 1
        if 0 <= choice < len(humanList):
            return humanList[choice]
        else:
            raise ValueError
    except ValueError:
            print("Invalid number!")
            return selectHumans(humanList)

def main():
    folderPath = 'Humans/'
    humans = collectHumFiles(folderPath)

    if humans:
        selection = selectHumans(humans)
        print(f"You selected: { selection }")
    else:
        print("No .hum files found in current context!")


if __name__ == "__main__":
    main()