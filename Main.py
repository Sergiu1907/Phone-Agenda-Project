agenda = {
    "Sergiu": "93847474",
    "Sorin" : "7374734",
    "Sonia" : "21939123",
    "Ion": "0752022454",
    "Riven": "8384737"}

def meniu () :
    print ("Meniu:" "\n" 
        "1.Add new contact" "\n" 
        "2.Find contact" "\n" 
        "3.Delete contact" "\n"
        "4.Show Agenda")
    a = int(input ("-->"))
    return a

   
def add_contact():
    cmd =verify_contact()
    if cmd == 1:
        add_contact()


def find_contact():
    print("find")


def delete():
    print("delete")


def show_agenda ():
    sorted_agenda = sorted(agenda.keys())
    print ("Agenda:")
    for k in sorted_agenda :
        print (k, "--->", agenda[k])
    comanda = int(input("0.Return to Menu" "\n" "1.Create New Contact" "\n" "-->"))
    if comanda == 1:
        add_contact()


def verify_contact ():
    exist = True
    key_list = list(agenda.keys())
    while exist == True :
        add_contact = input("Enter name:")
        if add_contact in key_list :
            print ("Name already existing, enter another name: ")
            exist = True 
        else :
            exist = False
            add_number = input("Enter number:")
            agenda[add_contact] = add_number
            # info("Contact added")
    comanda = int(input("0.Return to Menu" "\n" "1.Create New Contact" "\n" "-->"))
    return comanda 


def command(nr):
    if nr == 1:
        add_contact()
    if nr == 2:
        find_contact()
    if nr == 3:
        delete()
    if nr == 4:
        show_agenda()

            
while True:
    nr_meniu = meniu()
    command(nr_meniu)




