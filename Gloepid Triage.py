print("Hello I'm Gloepid Bot \n"

"Here to help you assess your COVID-19 risk factor and know if you need to contact the NCDC. \n"

"Please note that I am an assessment tool and should not be used for diagnostic purposes \n"

"Let’s begin when you are ready: Type 1 to begin")

start = input('')
assert start == str(1), "You cancelled the test"

print()
input("Q1: What is your name? \n")
print()

print("Q2: What is your age? \n"
"Enter the key to choose an age range \n"
      "key          Age range \n"
      "1            Below 10 \n"
      "2            10 - 19 \n"
      "3            20 - 29 \n"
      "4            30 - 39 \n"
      "5            40 - 49 \n"
      "6            60+ \n")
age = input('')
if age in str([1,2,3,4,5,6]):
    pass
else:
    print("You entered an invalid key")

print()
print("Where are you right now? \n"
      "Enter 1 to use my current location or 2 to input (state)")
state_list = ["Abia", "Abuja", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River",
              "Delta", "Ebonyi", "Enugu", "Edo", "Ekiti", "Gombe","Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi",
              "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto",
              "Taraba", "Yobe", "Zamfara"]
location = str(input('')).title()
assert location in state_list, "Invalid State"

def question_set_1():
    print()
    print("Q4. Have you travelled outside the country within the last 14 days? \n"
     "To select Yes press 1 to select No press 2")
    global travel
    travel = str(input(''))
    print()
    if travel == '2':
        print("Q5. Have you been in contact with a confirmed case of coronavirus (COVID-19)? \n"
              "Enter 1 for Yes \n"
              "Enter 2 for No \n"
              "Enter 3 for Not to my knowledge \n")
        global contact_with_conf_case
        contact_with_conf_case = str(input(''))
        print()
        if contact_with_conf_case == '2' or contact_with_conf_case == '3':
            print("Q6. Have you been in contact with someone who just arrived in Nigeria in the last one month? \n"
                  "Enter 1 for Yes \n"
                  "Enter 2 for No \n"
                  "Enter 3 for Not to my knowledge \n")
            global contact_with_nig_arrival
            contact_with_nig_arrival = str(input(''))
            print()
            if contact_with_nig_arrival == '1':
                print("is the individual sick or indicating any COVID-19 symptoms \n"
                      "Enter 1 for Yes \n"
                      "Enter 2 for No \n")
                global individual_sick
                individual_sick = input(str(''))
            elif contact_with_nig_arrival == '2' or contact_with_nig_arrival == '3':
                return
            else:
                raise Exception('Invalid Input')
        elif contact_with_conf_case == '1':
            return
        else:
            raise Exception('Invalid Input')
    elif travel == '1':
        return
    else:
        raise Exception('Invalid Input')
question_set_1()

print()
print("Q7.Have you been experiencing any of the following (select all that apply by entering 1 for yes and 2 for no)")
print("Dry Cough")
dry_cough = str(input(''))
if dry_cough not in ['1','2']:
    raise Exception('Invalid Input')
print()
print("Body Temperature > 37.8 Celsius")
fever = str(input(''))
if fever not in ['1', '2']:
    raise Exception('Invalid Input')
print()
print("Difficulty in breathing")
diff_in_brth = str(input(''))
if diff_in_brth not in ['1', '2']:
    raise Exception('Invalid Input')
print()
print("fatigue/tiredness")
fatigue = str(input(''))
if fatigue not in ['1', '2']:
    raise Exception('Invalid Input')
print()
print("Sore throat")
sore_throat = str(input(''))
if sore_throat not in ['1', '2']:
    raise Exception('Invalid Input')
print()

print("Q8. When did the symptoms start? (Enter number of days)")
symptoms_start = int(input(''))

def question_set_2():
    print()
    print("Have you been self-isolating? \n"
          "Enter 1 for Yes or 2 for No")
    global self_isolating
    self_isolating = str(input(''))
    if self_isolating == '2':
        print("Have you visited any public space since you first started to notice symptoms? \n"
              "Enter 1 for Yes or 2 for No")
        global public_space
        public_space = str(input(''))
    elif self_isolating == '1':
        return
    else:
        raise Exception('Invalid Input')
question_set_2()

print()
print("Kindly provide your phone number and contact address")
print("Phone number")
phone_number = str(input(''))
print("Contact Address")
contact_address = str(input(''))

print("-"*100)

low_risk_message = ("You seem to be doing fine at the moment. But stay alert and practice social distancing.\n"
"You can call a doctor if you have any unrelated health issues or questions.\n"
"Add Link to Gloepid mobile app download,  self-isolation guide, subscribe to NCDC WhatsApp bot,\n"
"invite others to take the test")

medium_risk_message = ("You may have been exposed. Please self isolate and monitor your health status,\n"
"if there are any changes to your symptoms, please call a doctor or take the assessment test again\n"
"Add Link to Gloepid mobile app download,  self-isolation guide, subscribe to NCDC WhatsApp bot,\n" 
"invite others to take the test")

high_risk_message = ("Please be patient and wait for an NCDC rep to contact you.\n"
"In the meantime, kindly do the following\n"
"- Remain calm\n"
"- Self-isolate insert self-isolation guide\n"
"- Wait for healthcare services to contact you for further information and next steps")

if (travel == '1' and dry_cough == '1') or (travel =='1' and diff_in_brth == '1') or (travel =='1' and fever == '1'):
    print(high_risk_message)
elif (contact_with_conf_case == '1' and dry_cough == '1') or (contact_with_conf_case =='1' and diff_in_brth == '1') or (contact_with_conf_case =='1'and fever == '1'):
    print(high_risk_message)
elif (location in ['Lagos', 'Abuja', 'Oyo'] and dry_cough == '1') or (location in ['Lagos', 'Abuja', 'Oyo'] and diff_in_brth == '1') or (location in ['Lagos', 'Abuja', 'Oyo'] and fever == '1'):
    print(high_risk_message)

if ((travel == '1' and dry_cough == '2' and diff_in_brth == '2' and fever == '2', fatigue == '2', sore_throat == '2') or
        (contact_with_conf_case == '1' and dry_cough == '2' and diff_in_brth == '2' and fever == '2' and fatigue == '2' and sore_throat == '2') or
        (individual_sick == '1' and dry_cough == '2' and diff_in_brth == '2' and fever == '2' and fatigue == '2' and sore_throat == '2')
    or (contact_with_conf_case == '3' and dry_cough == '1') or (contact_with_conf_case == '3' and diff_in_brth == '1') or (contact_with_conf_case == '3'
and fever == '1') or (contact_with_nig_arrival  == '3' and dry_cough == '1') or (contact_with_nig_arrival  == '3' and diff_in_brth == '1') or
    (contact_with_nig_arrival  == '3' and fever == '1')):
    print(medium_risk_message)

else:
    print(low_risk_message)