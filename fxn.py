prompt = "\n---> "

#this should allow the user to type in any sentence. so long as "boy" or "girl" is in the sentence, it should proceed.

def ask_gender():
    sex = input(prompt).lower().split(" ")
    gender_list = []
    for i in sex:
        new = i.strip(' "" .!? ')
        gender_list.append(new)

    if "boy" in gender_list:
        return ("he" , "him" , "his", "Onee-chan" , "boy")
    elif "girl" in gender_list:
        return ("she" , "her" , "her", "Onii-chan" , "girl")
    
    #if neither "boy" or "girl" is in the sentence, the user should be asked again
    else:
        print("\nJust choose either boy or girl for now. \n")
        ask_gender()

print("is Alex a boy or a girl?")

pronoun1 , pronoun2 , pronoun3 , pet_name , gender = ask_gender()

print(f"""
Alex is a {gender}.
{pronoun1} has 3 siblings who all calls {pronoun2} {pet_name}.
Even {pronoun3} mom calls {pronoun2} {pet_name}.
""")
