def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    personalbest = 0
    for result in scores:
        if result > personalbest:
            personalbest = result
    return personalbest        


def personal_top_three(scores):
    PersonalTopThree = []
    for result in scores:
        PersonalTopThree.append(result)
        PersonalTopThree.sort(reverse=True)
        PersonalTopThree = [PersonalTopThree[i] for i in range(min(len(PersonalTopThree),3))]
    return PersonalTopThree                
