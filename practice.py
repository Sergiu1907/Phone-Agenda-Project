agenda = {
    "Sergiu": "93847474",
    "Ion": "0752022454",
    "Riven": "8384737",
    "Sorin": "234324",
    "Sorina" : "123213"}

def find_contact ():
    check_name = input ("Enter first letters of a contact:")
    sorted_agenda = sorted(agenda.keys())
    n = 0
    dict1 = {}
    
    for k in sorted_agenda :
        if check_name == k[:len(check_name)] :
            n +=1
            a = str(n) + "."+ " " + k
            print (a)
            dict1[n] = k
    dict1[0] = "Return to Meniu"
    print (dict1)


    
    contact_details = int (input("-->"))

    d = dict1.get(contact_details)
    print ("+", "-"*20, "+")
    print ("Name:",d)
    print ("Phone number:", agenda.get(d))
    print ("+", "-"*20, "+")

find_contact()    


