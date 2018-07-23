#1 python3
'''randomQuizGenerator.py - creates different quizzes using 50 multiple
    choice questions for each quiz, in random order. Provides one correct
    answer as well as 3 incorrect answers for each question. Writes quiz
    to 35 different text files and answer keys to 35 text files.'''

import random

# Dictionary of quiz data to draw from. States are keys, Capitals are values
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Create 35 quiz test files
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_Answers%s.txt' % (quizNum + 1), 'w')

    # Write the header file for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz ( Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states and make a question for each
    for questionNum in range(50):
        # Generate correct and incorrect answers
        correctAnswer = capitals[states[questionNum]]
        # Generate list of all capitals 
        wrongAnswers = list(capitals.values())
        # Delete the correct answer from that list
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # Pull 3 incorrect answers
        wrongAnswers = random.sample(wrongAnswers, 3)
        # Bundle the correct answer with the incorrect answers
        answerOptions = wrongAnswers + [correctAnswer]
        # Shuffle the answers
        random.shuffle(answerOptions)

        # Write quiz question and possible answer choices
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

    # Write the answer key out to file
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
