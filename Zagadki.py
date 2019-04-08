wrong_count = 0
right_count = 0

quest_base = {"Name ticher " : "nikita",
"You learning " : "python",
"Last version python ":"3.6",
"Site developer ":"github",
"sfssasssa ": "sfasfascas",
"sdfsdsdsd ":"vsdfvsd"
}

for cikle, znachenie in quest_base.items(): # items -  это предметы
	otvet = str(input(cikle)).lower()		# .lower - приведение к нижнему регистру
	if otvet == znachenie:
		print("Nice! ")
		right_count +=1
	elif otvet != znachenie:
		print("fUCK!Noooo....")
		wrong_count +=1

print("Good otvet: {}" .format (right_count) + "," + "Bad otvet: {}" .format (wrong_count))
