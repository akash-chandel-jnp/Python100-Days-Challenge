def name_format() :
    f_Name = input("Enter Your First Name : ").lower()
    l_Name = input("Enter Your Last Name : ").lower()


    f_Name_First_letter = f_Name[0].capitalize()
    f_Name_remaining_letters=''
    l_Name_First_letter = l_Name[0].capitalize()
    l_Name_remaining_letters=''

    for i in range(1,len(f_Name)):
        f_Name_remaining_letters +=f_Name[i]

    for i in range(1,len(l_Name)):
        l_Name_remaining_letters +=l_Name[i]

    full_name_formatted = f_Name_First_letter + f_Name_remaining_letters + " " +l_Name_First_letter+l_Name_remaining_letters

    return full_name_formatted

print(name_format())