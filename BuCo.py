
#from BuCo_AI import *
from BuCo_Players import *

import time
import itertools

from colorama import *
init()

# Declare class Data
D=Data()
# Declare class Generator
G=Generator()
# Declare class Analyze
A=Analyze()

PlayerOne = Player()
#OneB = Bot('Bot One')
#TwoB = Bot('Bot Two')

def clearScreen(mode=2):
	"""Очистка экрана"""
	#wt=winterm.WinTerm()
	#wt.erase_screen(2,0)
	print(ansi.clear_screen(mode))	

def playerTry(PythonList):
	"""Player try function"""
	MY = list(input('\nPlayer Try\nPlease enter:>'))
	BC = A.findBullsCows(PythonList, MY)
	print (Fore.GREEN + Cursor.UP(1) + Cursor.FORWARD(7) + '> Bulls={Bulls}, Cows={Cows}'.format(Bulls=BC[0],Cows=BC[1]), Fore.WHITE)
	return BC[0]

def PythonTry(inStepNum,inMyList,inExceptList,inWorkList,inPastLists):
	"""Python try function"""

	inStepNum+=1
	D.StepNum=inStepNum
	print('\n---STEP:',inStepNum,'------------------------------------')
	print('Find the list:',D.MyList)

	if inStepNum==1:
		GenList=G.GL(('0','1','2','3','4','5','6','7','8','9'),4)# GenerateList()
		BullsCows=A.findBullsCows(GenList,inMyList)

		AnalyzeRusult=A.analyzer(inStepNum,GenList,BullsCows,D.DigitsList)
		D.Mode=AnalyzeRusult[0]

		if AnalyzeRusult[0]==('FULL'):
			D.AcceptList=GenList
                
		if AnalyzeRusult[0]==('EMPTY'):
			D.ExceptList=D.ExceptList+GenList

		if AnalyzeRusult[0]==('MIDDLE'):
			D.WorkList=GenList
                
	if inStepNum==2:
		if D.Mode=='FULL':
			GenList=G.genListFromList(D.AcceptList,inPastLists)
                
		#if (Mode=='EMPTY') | (Mode=='MIDDLE'):
		if D.Mode=='EMPTY':
			GenList=G.generateListWithExcept(inExceptList,inPastLists,D.DigitsList,[])

		if D.Mode=='MIDDLE':
			GenList=G.generateListWithExcept(inExceptList,inPastLists,D.DigitsList,[])

		BullsCows=A.findBullsCows(GenList,inMyList)
		AnalyzeRusult=A.analyzer(inStepNum,GenList,BullsCows,D.DigitsList)
		D.Mode=AnalyzeRusult[0]

		if AnalyzeRusult[0]==('FULL'):
			D.AcceptList=GenList
                
		#if AnalyzeRusult[0]==('EMPTY'):
			#ExceptList=ExceptList+GenList

		if AnalyzeRusult[0]==('MIDDLE'):
			D.WorkList=GenList

		D.analyzeResultSave=AnalyzeRusult

	if inStepNum>=3:
		genWay = random.randint(0,1)

		if D.Mode=='FULL':
			#if genWay == 1:
			GenList=G.genListFromList(D.AcceptList,inPastLists)
			#else:
				#GenList=getFromAnalyzeResult(analizeResultSave,inPastLists)

		if D.Mode=='EMPTY':
			#if genWay == 1:
			#	GenList = GenerateListWithExcept(inExceptList, inPastLists, DigitsList, analizeResultSave)
			#else:
			GenList = G.genListFromAnalyzeResult(D.analyzeResultSave, inPastLists)

		if D.Mode=='MIDDLE':
			#if genWay == 1:
			#	GenList = GenerateListWithExcept(inExceptList, inPastLists, DigitsList, analizeResultSave)
			#else:
			GenList = G.genListFromAnalyzeResult(D.analyzeResultSave, inPastLists)

		BullsCows = A.findBullsCows(GenList, inMyList)
		AnalyzeRusult = A.analyzer(inStepNum,GenList,BullsCows,D.DigitsList)

		D.Mode=AnalyzeRusult[0]
		BullsList_Pos1=AnalyzeRusult[3]
		BullsList_Pos2=AnalyzeRusult[4]
		BullsList_Pos3=AnalyzeRusult[5]
		BullsList_Pos4=AnalyzeRusult[6]
		
		if AnalyzeRusult[0]==('FULL'):
			D.AcceptList=GenList

		if AnalyzeRusult[0]==('MIDDLE'):
			D.WorkList=GenList

		D.analyzeResultSave = AnalyzeRusult

	##print (AnalyzeRusult)
	print (D.Mode)
	print ('GenList:',GenList)
	print ('AcceptList:',D.AcceptList)
	print ('ExceptList:', D.ExceptList)
	print ('WorkList:',D.WorkList)

	return inStepNum,tuple(GenList),tuple(BullsCows)

def resultGame(Player1,Player2):
	print(Player1.name,'steps collect:')
	for line in range(len(Player1.Data.StepCollect)):
		print(Player1.Data.StepCollect[line])

	print('\n',Player2.name,'steps collect:')
	for line in range(len(Player2.Data.StepCollect)):
		print(Player2.Data.StepCollect[line])

	Player1.Data.PythonList = Player1.Data.StepData[-1]
	print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
	print(Player1.name,'stats:')
	print(Player1.name,'list:{a}{b}{c}{d}'.format(a=Player1.playerSetList[0], b=Player1.playerSetList[1],
										 c=Player1.playerSetList[2], d=Player1.playerSetList[3]))
	print('Step:', Player1.Data.StepNumber[-1],
		  '-> Opponent list: {a}{b}{c}{d}'.format(a=Player1.Data.PythonList[0], b=Player1.Data.PythonList[1],
												  c=Player1.Data.PythonList[2], d=Player1.Data.PythonList[3]))

	Player2.Data.PythonList = Player2.Data.StepData[-1]
	print('')
	print(Player2.name,'stats:')
	print(Player2.name,'list:{a}{b}{c}{d}'.format(a=Player2.playerSetList[0], b=Player2.playerSetList[1],
										c=Player2.playerSetList[2], d=Player2.playerSetList[3]))
	print('Step:', Player2.Data.StepNumber[-1],
		  '-> Opponent list: {a}{b}{c}{d}'.format(a=Player2.Data.PythonList[0], b=Player2.Data.PythonList[1],
												  c=Player2.Data.PythonList[2], d=Player2.Data.PythonList[3]))

	print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

	if Player1.Data.StepNumber[-1] < Player2.Data.StepNumber[-1]:
		print('\n---------------')
		print(Player1.name,'WIN!!!')
		print('---------------')
		return Player1.name
	elif Player1.Data.StepNumber[-1] > Player2.Data.StepNumber[-1]:
		print('\n---------------')
		print(Player2.name,'WIN!!!')
		print('---------------')
		return Player2.name
	else:
		print('\n---------------')
		print('DRAW')
		print('---------------')
		return 'DRAW'

def procBuCo():
	"""Procedure realization of game bot against bot"""
	while True:
		clearScreen()

		timeStart = time.time()

		D.__init__()

		D.PythonList = G.GL(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 4)
		print(D.PythonList)

		##MyList=list(input('My List > '))
		# D.MyList = G.GL(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 4)
		D.MyList = PlayerOne.autoGenerateList()
		print(D.MyList)
		D.MyTry = 4

		while True:
			PythonFinding = PythonTry(D.StepNum, D.MyList, D.ExceptList, D.WorkList, D.StepData)
			print(PythonFinding)
			D.StepCollect.append(PythonFinding)
			D.StepNumber.append(PythonFinding[0])
			D.StepData.append(PythonFinding[1])
			D.StepResult.append(PythonFinding[2])

			# Show Matrix
			for stringNum in range(len(D.DigitsList)):
				print(stringNum, D.DigitsList[stringNum])

			if PythonFinding[2] == (4, 0):
				print('\nFIND SUCCESS!!!!\n')
				break
			if D.MyTry != 4:
				D.MyTry = playerTry(D.PythonList)
				if D.MyTry == 4:
					print('\nYES! This is 4 bulls!\nYou won at', D.StepNumber[-1], 'attempts!')

			# qc=input('\nEnter comand or press any key to generate next step:')
			qc = 'pass'
			if qc == 'q':
				print('Exit')
				break
			if qc == 'l':
				print('Accept list:')
				print(D.AcceptList)
				print('Except list:')
				print(D.ExceptList)
				input('\nEnter any key to generate next step...')
			if qc == 's':
				print('Collect data:')
				print('-----------------------------------------------')
				for i in range(len(D.StepCollect)):
					print(D.StepCollect[i])
				input('\nEnter any key to generate next step...')

		D.PythonList = D.StepData[-1]
		print('Step:', D.StepNumber[-1],
			  '-> Value: {a}{b}{c}{d}'.format(a=D.PythonList[0], b=D.PythonList[1], c=D.PythonList[2],
											  d=D.PythonList[3]))
		# input('\nEnter any key to exit')

		timeFinish = time.time()
		print('Time for result:', timeFinish - timeStart)
		time.sleep(0.5)

def objBotBot():
	"""Game AI Bot against AI Bot"""
	while True:
		clearScreen()

		timeStart = time.time()

		OneB = Bot('Bot One')
		TwoB = Bot('Bot Two')

		OneB.autoGenerateList()
		TwoB.autoGenerateList()

		OneB.opponentList = TwoB.playerSetList
		TwoB.opponentList  = OneB.playerSetList

		while True:
			OneB.game()
			TwoB.game()
			if OneB.Data.Mode == 'COMPLETE' and TwoB.Data.Mode == 'COMPLETE':
				print('\nGAME COMPLETE!!!!\n')
				break

		timeFinish = time.time()

		resultGame(OneB, TwoB)

		timeGame = str(timeFinish - timeStart)
		print('\nGame time:', timeGame[0:5],'sec')

		#print(Bot.botsCount)
		#print(Player.playersCount)
		#print('\nStep collect in object:', OneB.Data.StepCollect[4])
		time.sleep(2)

		#input('\nEnter any key to continue')

def objBotPlayer():
	"""Game human player against AI Bot"""
	while True:
		clearScreen()

		PlayerMy = Player('Player Me')
		PlayerBot = Bot('Player Bot')

		PlayerBot.autoGenerateList()
		PlayerMy.setList()

		PlayerBot.opponentList  = PlayerMy.playerSetList
		PlayerMy.opponentList  = PlayerBot.playerSetList

		while True:
			if PlayerMy.Data.Mode != 'COMPLETE':
				print('\nPlayer steps collect:')
				for line in range(len(PlayerMy.Data.StepCollect)):
					print(PlayerMy.Data.StepCollect[line])
				MyTry = PlayerMy.inputTry(PlayerBot.playerSetList)
				if MyTry[0] == 4:
					print('FIND SUCCESS!')
					time.sleep(3)
				#input('Press enter key to continue....')
				if MyTry[0] == 4:
					PlayerMy.Data.Mode = 'COMPLETE'

			PlayerBot.game()
			if PlayerBot.Data.Mode == 'COMPLETE' and PlayerMy.Data.Mode == 'COMPLETE':
				print('\nGAME COMPLETE!!!!')
				break

		resultGame(PlayerBot,PlayerMy)

		#print(Bot.botsCount)
		#print(Player.playersCount)

		input('\nEnter any key to exit')
		break
#-MAIN LOOP-------------------------------------------------------------
if __name__ == '__main__':
	#procBuCo()
	objBotBot()
	#objBotPlayer()
#-MAIN LOOP-------------------------------------------------------------