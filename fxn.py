boy_list = ["he" , "him" , "his", "Onee-chan"]
girl_list = ["she" , "her" , "her", "Onii-chan"]

prompt = "\n---> "

def ask_gender():
    sex = input(prompt).lower().split(' ')
    #for completion him\her
    new_list = []
    for i in sex:
        new = i.strip(' "" .!? ')
        new_list.append(new)
    #test value
    return new_list


print("are you a boy or a girl?")

gender = ask_gender()

print(gender)



#pronoun1 , pronoun2 , pronoun3 , jp_porn = ask_gender()
