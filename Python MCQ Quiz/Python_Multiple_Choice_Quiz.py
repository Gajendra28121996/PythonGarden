from Python_Question_Class import Question_Class

question_prompts=[
	"\n1. Study of the Universe is known as ? \n(a) Sociology \n(b) Cosmology\n(c) Universology\n\n",
	"\n2. Approximately how many Galaxies are there ? \n(a) 100 Billion Galaxies \n(b) 10 Billion Galaxies \n(c) 1000 Billion Galaxies \n\n",
	"\n3. Big Bang theory explains ? \n(a) Origin of Universe. \n(b) Origin of Sun.\n(c) Laws of physics.\n\n",
	"\n4. Which is correct order of solar system starting from Sun ? \n(a) Mercury, Venus, Earth, Jupiter, Mars, Saturn, Uranus, Neptune\n(b)Mercury, Venus, Earth, Mars, Jupiter, Saturn, Neptune, Uranus\n(c) Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune\n\n", 
	"\n5. Big Bang was an explosion that occurred ?  \n(a) 20 Billion years ago \n(b) 10 Billion years ago.\n(c) 15 Billion years ago\n\n",
	"\n6. Which Planet is dwarf planet ? \n(a) Mercury \n(b) Pluto\n(c) Mars\n\n",
]

questions = [
	Question_Class(question_prompts[0],"b"),
	Question_Class(question_prompts[1],"b"),
	Question_Class(question_prompts[2],"a"),
	Question_Class(question_prompts[3],"c"),
	Question_Class(question_prompts[4],"c"),
	Question_Class(question_prompts[5],"b"),


]

def run_test(questions):
	score=0 
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score +=1
	print("You Got "+str(score)+ "/" +str(len(questions))+ " correct")
 
run_test(questions)