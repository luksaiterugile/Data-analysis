import pandas as pd
import pyparsing as pp
import re
import sys
import os
import csv

def calculate_percent_symbol(email):
    return email.count('%')

def calculate_discount(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('discount') > 0):
        return 1
    elif(lower_case_email.count('nuolaida') > 0):
        return 1
    elif(lower_case_email.count('nuolaidos') > 0):
        return 1
    else:
        return 0

def calculate_links(email):
    lower_case_email = email.lower()
    if(email.count('https://') > 0):
        return 1
    else:
        return 0

def calculate_size(email_fp):
    for count, line in enumerate(email_fp):
        pass
    return count + 1

def calculate_black_friday(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('black friday') > 0):
        return 1
    elif(lower_case_email.count('juodasis penktadienis') > 0):
        return 1
    else:
        return 0
    
def calculate_euro_symbol(email):
    if(email.count('€') > 0):
        return 1
    else:
        return 0

def calculate_respect(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('pagarbiai') > 0):
        return 1
    else:
        return 0
    
def calculate_question_marks(email):
    return email.count('?')

def calculate_order(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('užsakymas') > 0):
        return 1
    elif(lower_case_email.count('order') > 0):
        return 1
    else:
        return 0
    
def calculate_name(email):
    lower_case_email = email.lower()
    match_from = re.findall("from: .*", lower_case_email)
    match_to = re.findall("to: .*", lower_case_email)
    lower_case_email = lower_case_email.replace(match_from[0], '')
    lower_case_email = lower_case_email.replace(match_to[0], '')
    if(lower_case_email.count('rugilė') > 0):
        return 1
    elif(lower_case_email.count('rugile') > 0):
        return 1
    elif(lower_case_email.count('lukšaitė') > 0):
        return 1
    elif(lower_case_email.count('luksaite') > 0):
        return 1
    else:
        return 0
    
def calculate_sale(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('sale') > 0):
        return 1
    elif(lower_case_email.count('išpardavimas') > 0):
        return 1
    else:
        return 0
    
def calculate_capital_letters(email):
    return sum(1 for letter in email if letter.isupper())

def calculate_lowercase_letters(email):
    return sum(1 for letter in email if letter.islower())

def calculate_num_of_files(email):
    match = re.findall("ATTACHMENTS \(.*\): (\".*\")+", email)
    founded_files = ''
    if(len(match) != 0):
        for i in match:
            founded_files = i
    result = pp.commaSeparatedList.parseString(founded_files).asList()
    return len(result)

def calculate_recipients(email):
    match = re.findall("TO: .*@.*\..*", email)
    result = 0
    if(match):
        for i in match:
            test = i
        extract_email = re.findall(" .*@.*\..*", test)
        result = (len(extract_email[0].split(',')))
        if(result > 1):
            return 1
        elif(result == 1):
            return 0

def calculate_exclamation(email):
    return email.count('!')

def calculate_file(email):
    match = re.findall("ATTACHMENTS \(.*\): (\".*\")+", email)
    if(len(match) != 0):
        return 1
    else:
        return 0

def calculate_unsubscribe(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('unsubscribe') > 0):
        return 1
    elif(lower_case_email.count('atsisakyti') > 0):
        return 1
    else:
        return 0

def calculate_receipt(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('receipt') > 0):
        return 1
    elif(lower_case_email.count('sąskaita') > 0):
        return 1
    elif(lower_case_email.count('čekis') > 0):
        return 1
    else: 
        return 0

def calculate_forward(email):
    match = re.findall("-* Forwarded message -*", email)
    if(len(match) != 0):
        return 1
    else:
        return 0
    
def calculate_photo(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('.jpg') > 0):
        return 1
    elif(lower_case_email.count('.png') > 0):
        return 1
    else:
        return 0
    
def calculate_letters(email):
    return len(email)

def calculate_thanks(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('ačiū') > 0):
        return 1
    elif(lower_case_email.count('dėkojame') > 0):
        return 1
    elif(lower_case_email.count('thanks') > 0):
        return 1
    elif(lower_case_email.count('thank you') > 0):
        return 1
    else:
        return 0
   
def calculate_space(email):
    return email.count(' ')

def calculate_period(email):
    return email.count('.')

def calculate_subject(email):
    match = re.findall("SUBJECT: .*", email)
    result = 0
    if(match):
        for i in match:
            test = i
        extract_subject = re.findall(" .*", test)
        result = len(str(extract_subject[0]))
    return result
    

def calculate_comma(email):
    return email.count(',')
 
def calculate_privacy_policy(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('privatumo politika') > 0):
        return 1
    elif(lower_case_email.count('privacy policy') > 0):
        return 1
    else:
        return 0

def calculate_offer(email):
    lower_case_email = email.lower()
    if(lower_case_email.count('offer') > 0):
        return 1
    elif(lower_case_email.count('pasiūlymai') > 0):
        return 1
    elif(lower_case_email.count('pasiūlymas') > 0):
        return 1
    elif(lower_case_email.count('offers') > 0):
        return 1
    else:
        return 0
    
class_argument_non_advertisement = 'non-advertisement'
class_argument_advertisement = 'advertisement'

files_non_advertisement = os.listdir('../Laiškai/Ne_reklama/')
files_advertisement = os.listdir('../Laiškai/Reklama/')

# Creating csv file
header = ['percent', 'discount', 'links', 'size', 'black_friday',
           'euro', 'respect', 'question', 'order', 'name', 'sale', 
           'capital_letters', 'lowercase_letters', 'num_of_files',
           'recipients', 'exclamation', 'file', 'unsubscribe',
           'receipt', 'forward', 'photo', 'letters', 'thanks',
           'space', 'period', 'subject', 'comma', 'privacy_policy',
           'offer', 'class']

csv_file = open('non-advertisement.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(header)

for file in files_non_advertisement:
    file_atributes = []
    f = open('../Laiškai/Ne_reklama/' + file, 'r')
    email = f.read()
    percent = calculate_percent_symbol(email)
    discount = calculate_discount(email)
    links = calculate_links(email
    size = calculate_size(email)
    black_friday = calculate_black_friday(email)
    euro = calculate_euro_symbol(email)
    respect = calculate_respect(email)
    question = calculate_question_marks(email)
    order = calculate_order(email)
    name = calculate_name(email)
    sale = calculate_sale(email)
    capital_letters = calculate_capital_letters(email)
    lowercase_letters = calculate_lowercase_letters(email)
    num_of_files = calculate_num_of_files(email)
    recipients = calculate_recipients(email)
    exclamation = calculate_exclamation(email)
    file = calculate_file(email)
    unsubscribe = calculate_unsubscribe(email)
    receipt = calculate_receipt(email)
    forward = calculate_forward(email)
    photo = calculate_photo(email)
    letters = calculate_letters(email)
    thanks = calculate_thanks(email)
    space = calculate_space(email)
    period = calculate_period(email)
    subject = calculate_subject(email)
    comma = calculate_comma(email)
    privacy_policy = calculate_privacy_policy(email)
    offer = calculate_offer(email)

    # Creating list with all email attribute values
    file_atributes.extend([percent, discount, links,
                         size, black_friday, euro, respect,
                         question, order, name, sale, capital_letters,
                         lowercase_letters, num_of_files, recipients,
                         exclamation, file, unsubscribe, receipt,
                         forward, photo, letters, thanks, space,
                         period, subject, comma, privacy_policy, offer, 
                         class_argument_non_advertisement])

    writer.writerow(file_atributes)