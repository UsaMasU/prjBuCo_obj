"""Human player and AI bot player classes"""

from BuCo_AI import *

# class Player
class Player:
    """Player"""
    playersCount = 0
    stepNum = 0
    playerTryList = []
    playerSetList = []
    opponentList = []
    attemptsCollect = []
    Generator = Generator()
    Analyze = Analyze()
    Data = Data()

    def __init__(self, name=''):
        self.name=name
        self.stepNum = 0
        self.playerTryList = []
        self.playerSetList = []
        self.opponentList = []
        self.attemptsCollect = []
        self.Generator = Generator()
        self.Analyze = Analyze()
        self.Data = Data()
        Player.playersCount += 1

    def __del__(self):
        Player.playersCount -= 1

    @classmethod
    def players(cls):
        """Objects counter"""
        return cls.playersCount

    def gameStep(self, cmd = None,val = None):
        """Operation wight game step number"""
        if cmd.lower() == '+':
            if val == None:
                self.stepNum += 1
            else:
                self.stepNum += val
        elif cmd.lower() == '-':
            if val == None:
                self.stepNum -= 1
            else:
                self.stepNum -= val
        return self.stepNum

    def inputTry(self,opponentList):
        step=self.gameStep('+')
        self.playerTryList = list(input('\nPlayer Try\nPlease enter:>'))
        checkBC = self.Analyze.findBullsCows(opponentList, self.playerTryList)
        print('Bulls:', checkBC[0],' Cows:',checkBC[1])
        self.statistic(step,self.playerTryList,checkBC)
        return checkBC

    def setList(self):
        self.playerSetList=list(input('Make player list:> '))
        return self.playerSetList

    def statistic(self,step, inputlist, result):
        self.Data.StepCollect.append((step, tuple(inputlist),result))
        self.Data.StepNumber.append(step)
        self.Data.StepData.append(inputlist)
        self.Data.StepResult.append(result)

    def autoGenerateList(self, mode = ''):
        self.playerSetList = self.Generator.GL(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 4)

        if mode == 'Show':
            print('Auto make list for',self.name,'player:> ',self.playerSetList)

        else:
            print('Auto make list for', self.name, 'player complete.')


        return self.playerSetList

class Bot(Player):
    """Bot"""
    botsCount = 0
    genList = []
    stepCollect = []

    stepNum = 0
    playerTryList = []
    playerSetList = []
    opponentList = []
    attemptsCollect = []
    Generator = None
    Analyze = None
    Data = []

    def __init__(self,name=''):
        self.name=name
        self.genList = []
        self.stepCollect = []

        self.stepNum = 0
        self.playerTryList = []
        self.playerSetList = []
        self.opponentList = []
        self.attemptsCollect = []
        self.Generator = Generator()
        self.Analyze = Analyze()
        self.Data = Data()

        Bot.botsCount += 1

    def __del__(self):
        Bot.botsCount -= 1

    @classmethod
    def bots(cls):
        """Objects counter"""
        return cls.botsCount

    def game(self):
        """Steps of game using AI"""
        while(self.Data.Mode != 'COMPLETE'):
            step=self.gameStep('+')
            print('\n---Player:',self.name,',Step:',step,'---------------')
            if step == 1:
                self.genList = self.Generator.GL(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 4)
                resBullsCows = self.Analyze.findBullsCows(self.genList,self.opponentList)
                analyzeResult = self.Analyze.analyzer(step,self.genList,resBullsCows,self.Data.DigitsList)
                mode = self.Data.Mode = analyzeResult[0]
                if mode == ('FULL'):
                    self.Data.AcceptList = self.genList
                elif mode == ('EMPTY'):
                    self.Data.ExceptList = self.Data.ExceptList + self.genList
                else:
                    self.Data.WorkList = self.genList

            if step == 2:
                mode = self.Data.Mode
                if mode == 'FULL':
                    self.genList = self.Generator.genListFromList(self.Data.AcceptList,self.Data.StepData)
                elif mode == 'EMPTY':
                    self.genList = self.Generator.generateListWithExcept(self.Data.ExceptList,self.Data.StepData,self.Data.DigitsList,[])
                else:
                    self.genList = self.Generator.generateListWithExcept(self.Data.ExceptList, self.Data.StepData,self.Data.DigitsList, [])
                resBullsCows = self.Analyze.findBullsCows(self.genList,self.opponentList)
                analyzeResult = self.Analyze.analyzer(step,self.genList,resBullsCows,self.Data.DigitsList)
                #print(analyzeResult[0])
                mode = self.Data.Mode = analyzeResult[0]

                if mode == ('FULL'):
                    self.Data.AcceptList = self.genList
                #elif mode == ('EMPTY'):
                #    self.Data.ExceptList = self.Data.ExceptList + genList
                else:
                    self.Data.WorkList = self.genList

                self.Data.analyzeResultSave = analyzeResult

            if step >= 3:
                genWay = random.randint(0, 1)
                mode = self.Data.Mode
                if mode == 'FULL':
                    self.genList = self.Generator.genListFromList(self.Data.AcceptList, self.Data.StepData)
                elif mode == 'EMPTY':
                    self.genList = self.Generator.genListFromAnalyzeResult(self.Data.analyzeResultSave,self.Data.StepData)
                else:
                    self.genList = self.Generator.genListFromAnalyzeResult(self.Data.analyzeResultSave, self.Data.StepData)
                resBullsCows = self.Analyze.findBullsCows(self.genList, self.opponentList)
                analyzeResult = self.Analyze.analyzer(step, self.genList, resBullsCows, self.Data.DigitsList)
                mode = self.Data.Mode = analyzeResult[0]
                BullsList_Pos1 = analyzeResult[3]
                BullsList_Pos2 = analyzeResult[4]
                BullsList_Pos3 = analyzeResult[5]
                BullsList_Pos4 = analyzeResult[6]

                if mode == ('FULL'):
                    self.Data.AcceptList = self.genList
                # elif mode == ('EMPTY'):
                #    self.Data.ExceptList = self.Data.ExceptList + genList
                else:
                    self.Data.WorkList = self.genList

                self.Data.analyzeResultSave = analyzeResult

            ##print(mode)
            print('GenList:', self.genList,'\nBulls:',resBullsCows[0], 'Cows:',resBullsCows[1], '\n')
            ##print('AcceptList:', self.Data.AcceptList)
            ##print('ExceptList:', self.Data.ExceptList)
            ##print('WorkList:', self.Data.WorkList)

            #print('result:',step, self.genList, resBullsCows)
            self.stepCollect.append((step, tuple(self.genList), resBullsCows))
            self.Data.StepCollect.append((step, tuple(self.genList), resBullsCows))
            ##print('Collect:')
            ##for line in range(len(self.Dat.StepCollect)):
            ##    print(self.Dat.StepCollect[line])

            ##print('local step collect:',self.stepCollect)
            self.Data.StepNumber.append(step)
            self.Data.StepData.append(self.genList)
            self.Data.StepResult.append(resBullsCows)

            self.Data.matrix()
            print('---Step compete---------------------------')
            return step, self.genList, resBullsCows