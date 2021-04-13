import sys

#Main line:
def main():
    nameList = ["Steve", "Craig", "Sarah", "Filipe", "xXNoScopezXx"]
    #Main while loop:
    while(True):
        print("Here are the existing users in the database:")
        for name in nameList:
            print("User: " + name)
        #Read user input:
        whaleName = input("Type a new name to add, or 'no' to quit: ")
        if whaleName.lower() == "no":
            break
        #Update list:
        nameList.append(whaleName)

main()