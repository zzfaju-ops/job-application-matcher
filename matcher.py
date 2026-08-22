#resume = "We are looking for a backend engineer with Python experience"
# this function will tale the resume, as well as suggested requirement, split it, and compare tp see if they match in any way. 

def match(requirements,resume):

    #the following put both the resume words and requirements into lower case so that matching isn't case sensitive

    l_requirements = requirements.lower() 
    l_resume = resume.lower() 

    # this line will split the words in lower case resume and requirements  and put each world into the list resume_words

    resume_words = l_resume.split()
    requirements_words = l_requirements.split()

 #this is an empty list that will be filled with words  found in lower case requirements

   # cleaned_found = []
 # A loop, looping through the list checking if the word is in l_requirements

    #for word in resume_words:
     # if word in requirements_words:
       #  cleaned_found.append(word)

  # once we  have a found list in order to return a match percentage , we need to compare the found list size againgst the initial requiremnet size 
    requirement_set = set(requirements_words)
    resume_set = set(resume_words)
    matched = requirement_set & resume_set   # words that appear in both

    matched_count = len(matched)
    total_required = len(requirement_set)
    match_percentage = (matched_count / total_required) * 100

    return match_percentage