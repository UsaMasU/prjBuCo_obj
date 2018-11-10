"""Artificial Intelligence classes"""

import random

# class Data
class Data:
    """Data"""
    ExceptList = []
    WorkList = []
    MyExceptList = []
    AcceptList = []
    PythonList = []
    MyList = []
    opponentList = []
    BullsList_Pos1 = []
    BullsList_Pos2 = []
    BullsList_Pos3 = []
    BullsList_Pos4 = []
    Mode = ''
    StepNum = 0
    StepNumber = []
    StepData = []
    StepResult = []
    StepCollect = []
    analyzeResultSave = []
    MyTry = 0
    DigitsList = [''] * 10

    def __init__(self, name=''):
        """constructor"""
        self.name = name

        self.analyzeResultSave = []
        self.StepData = []
        self.StepNumber = []
        self.StepData = []
        self.StepResult = []
        self.StepCollect = []
        self.ExceptList = []
        self.WorkList = []
        self.MyExceptList = []
        self.AcceptList = []
        self.PythonList = []
        self.MyList = []
        self.opponentList = []
        self.BullsList_Pos1 = []
        self.BullsList_Pos2 = []
        self.BullsList_Pos3 = []
        self.BullsList_Pos4 = []
        self.Mode = ''
        self.StepNum = 0
        self.StepNumber = []
        self.StepData = []
        self.StepResult = []
        self.StepCollect = []
        self.analyzeResultSave = []
        self.MyTry = 0
        self.DigitsList = [''] * 10

        # Заполнение таблицы цифр начальными значениями x,x,x,x
        for stringNum in range(len(list(range(10)))):
            self.DigitsList[stringNum] = ['x', 'x', 'x', 'x']

    def matrix(self):
        """Show matrix"""
        for stringNum in range(len(self.DigitsList)):
            print(stringNum, self.DigitsList[stringNum])

# class Generator
class Generator:
    """Class generator"""
    def __init__(self, name=''):
        """constructor"""
        self.name = name

    def generateListWithExcept(self, inExceptList, inPastLists, DigList, inAnalizeResultSave):
        """Generate list with exceptions"""
        attempts = 0
        sameAttempts = 0
        print('\nStart generation...')
        ##print('Except List:', inExceptList)
        ##print('Past Lists:', inPastLists)
        ##print('ANALYZE RESULT:', inAnalizeResultSave)
        while (True):
            inList = [0] * 4
            for i in range(len(inList)):
                ##print('\nList index:', i, ',List:', inList)

                while (True):
                    xRnd = random.randint(0, 9)
                    Digit = DigList[xRnd]
                    xRndFindA = inList.count(str(xRnd))
                    ##print('Random X:', xRnd, ', Count in other pleces:', xRndFindA)

                    if Digit[i] == 'N':
                        attempts += 1
                        ##print('There is no possible Bulls!. Bad attempt:', attempts, ' Generate new digit.')
                        ##if attempts > 100:
                            ##print('This is maximum limit of attempts to generate digit')

                    if (((xRndFindA != True) & (Digit[i] != 'N')) | (attempts > 100)):
                        attempts = 0
                        break

                inList[i] = str(xRnd)
                ##print('Modified List:', inList)

            if (self.findSameAttempts(inList, inPastLists) != 'YES!!!'):
                sameAttempts = 0
                break
            else:
                sameAttempts += 1
                if sameAttempts > 50:
                    ##print('This is maximum limit of attempts to generate digit')
                    sameAttempts = 0
                    if self.checkUnicList(inList) == 0:
                        break

        print('Generation finished.\n')
        return inList

    def genListFromAnalyzeResult(self, inAnalizeResultSave, inPastLists):
        attempts = 0
        sameAttempts = 0
        while (True):
            attempts += 1
            outList = []
            print('Start generation...')
            MayBull_Pos0 = str(
                self.genSimbolFromPosBulls(inAnalizeResultSave[3][3], inAnalizeResultSave[3][2], outList))
            ##print('Possible bull in pos 0:', MayBull_Pos0, '\n')
            outList.append(str(MayBull_Pos0))

            MayBull_Pos1 = str(
                self.genSimbolFromPosBulls(inAnalizeResultSave[4][3], inAnalizeResultSave[4][2], outList))
            ##print('Possible bull in pos 1:', MayBull_Pos1, '\n')
            outList.append(str(MayBull_Pos1))

            MayBull_Pos2 = str(
                self.genSimbolFromPosBulls(inAnalizeResultSave[5][3], inAnalizeResultSave[5][2], outList))
            ##print('Possible bull in pos 2:', MayBull_Pos2, '\n')
            outList.append(str(MayBull_Pos2))

            MayBull_Pos3 = str(
                self.genSimbolFromPosBulls(inAnalizeResultSave[6][3], inAnalizeResultSave[6][2], outList))
            ##print('Possible bull in pos 3:', MayBull_Pos3, '\n')
            outList.append(str(MayBull_Pos3))

            print('out list:', outList)

            if (self.findSameAttempts(outList, inPastLists) != 'YES!!!') | (attempts > 10):
                sameAttempts = 0
                break
            else:
                sameAttempts += 1
                if sameAttempts > 50:
                    ##print('This is maximum limit of attempts to generate digit')
                    sameAttempts = 0
                    break

        print('Generation finished.\n')
        return outList

    def genSimbolFromPosBulls(self, listPosBulls, listMayBeBulls, listException):
        listCommon = []
        listNotExcept = []

        ##print('List pos bulls:', listPosBulls)
        ##print('List may be bulls:', listMayBeBulls)
        ##print('List exception:', listException)

        for exceptElem in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if listException.count(exceptElem) == 0:
                listNotExcept.append(exceptElem)

        ##print('List not except:', listNotExcept)

        for digFromList in listPosBulls:
            if listException.count(digFromList) == 0:
                listCommon.append(digFromList)

        ##print('List common:', listCommon)

        if int(len(listCommon)) == 0:
            xRnd = random.choice(listNotExcept)
            ##print('Digit from list not exception:', xRnd)
        else:
            xRnd = random.choice(listCommon)
            ##print('Digit from list common:', xRnd)

        if int(len(listMayBeBulls)) > 3:
            xRndMB = random.choice(listMayBeBulls)
            ##print('Digit from list may be bulls:', xRndMB)
            if listException.count(xRndMB) == 0:
                xRnd = xRndMB
                ##print('Digit from list may be bulls finaly:', xRnd)

        return xRnd

    def checkUnicList(self, inList):
        checkRes = 0
        for simbol in inList:
            scount = inList.count(simbol)
            if scount > 1:
                checkRes = 1
        return checkRes

    def genSimbolFromList(self, inList):
        PastLists = [] * 4
        print('\nStart generation...')
        xRnd = random.choice(inList)
        print('Generate simbol from list ', inList, ':', xRnd)
        print('Generation finished.\n')
        return xRnd

    def genListFromList(self, inList, inPastLists):
        PastLists = [] * 4
        sameAttempts = 0
        print('\nStart generation...')
        # print ('Start List:',inList)
        while (True):
            random.shuffle(inList)
            if (self.findSameAttempts(inList, inPastLists) != 'YES!!!'):
                break
            else:
                sameAttempts += 1
                if sameAttempts > 50:
                    ##print('This is maximum limit of attempts to generate digit')
                    sameAttempts = 0
                    break
        print('Modified List:', inList)
        print('Generation finished.\n')
        return inList

    def GL(sel, inList, inQ):
        ##print('\nStart generation...')
        outList = random.sample(inList, inQ)
        # print ('List:',outList)
        ##print('Generation finished.\n')
        return outList

    def genList(self):
        inList = [0] * 4
        print('\nStart generation...')
        for i in range(len(inList)):
            ##print('\nList index:', i, ',List:', inList)
            while (True):
                xRnd = random.randint(0, 9)
                xRndFind = inList.count(str(xRnd))
                ##print('Random X:', xRnd, ', Count of simbols:', xRndFind)
                if xRndFind != True:
                    break
            inList[i] = str(xRnd)
            print('Modified List:', inList)
        print('Generation finished.\n')
        return inList

    def setInList(self, inList, Position, Value):
        inList[Position] = str(Value)

    def findSameAttempts(self, inList, inPastLists):
        FindResult = 'NO'
        GenList = []
        OurList = [0] * 4
        for i in range(len(inPastLists)):
            GenList = inPastLists[i]
            for t in range(len(GenList)):
                OurList[t] = GenList[t]
            # print('List:',inList,' Past list:',OurList)
            if (inList == OurList):
                FindResult = 'YES!!!'
                ##print('Find the same:', FindResult)
                break
        # print('Find the same:',FindResult)
        return FindResult

# class Analyze
class Analyze:
    """Class analyze"""

    def __init__(self, name=''):
        """constructor"""
        self.name = name

    def findBullsCows(self, inListA, inListB, Bulls=0, Cows=0):
        """Find bulls and cows"""
        for i in range(len(inListA)):
            FindCows = inListA.count(inListB[i])
            if FindCows == True:
                if inListA[i] == inListB[i]:
                    Bulls += 1
                else:
                    Cows += 1
        return Bulls, Cows

    # -Bulls selector--------------------------------------------------------
    def bullsSelector(self, List):
        CountFoundN = 1
        BullList = []

        for Pos in range(0, 10):
            GetSimbol = List[Pos]

            # print('pos:',Pos,'simbol',GetSimbol)

            if (GetSimbol == 'N'):
                continue
            if (GetSimbol == 'x') | (GetSimbol == 'M'):
                BullList.append(str(Pos))

        return BullList

    # _Bull & Cows Analyze---------------------------------------------------
    def analyzeBuCo(self, Position, DigList):
        Result = ('Good')
        HorList = [0] * 10
        ListN = []
        ListM = []
        ListBulls = []
        CountM = 0
        CountN = 0
        ##print('___ANALYZE______for_index:', Position)
        for i in range(len(list(range(10)))):
            Digit = DigList[i]
            HorList[i] = Digit[Position]

        CountX = HorList.count('x')
        if (CountX < 10):
            ##print('Find x:', CountX)

            CountN = HorList.count('N')
            if (CountN > 0):
                FoundPosN = HorList.index('N')
                # ListN.append(str(FoundPosN))
                ListN.append(str(FoundPosN))  ####
                ##print('Find N:', CountN)
            ##else:
                ##print('Find M: 0')

            CountM = HorList.count('M')
            if (CountM > 0):
                FoundPosM = HorList.index('M')
                # ListM.append(str(FoundPosM))
                ListM.append(str(FoundPosM))  ####
                ##print('Find M:', CountM)
            ##else:
                ##print('Find M: 0')

            if (CountN > 1):
                CountFoundN = 1
                for OtherPos in range(FoundPosN + 1, 10):
                    FoundOtherPosN = HorList.index('N', OtherPos, 10)
                    # print('pos:',OtherPos,'count:',CountFoundN,'Find N in pos',FoundOtherPosN)
                    if (FoundOtherPosN == OtherPos):
                        # ListN.append(str(FoundOtherPosN))
                        ListN.append(str(FoundOtherPosN))  ####
                        CountFoundN += 1
                    if (CountN == CountFoundN):
                        break
        ##print('Horizontal List:', Position, HorList)

        ##print('List not bulls:', ListN)
        ##print('List maybe bulls:', ListM)

        ListBulls = (self.bullsSelector(HorList))
        ##print('List possible bulls:', ListBulls)
        ##print('_________________________')
        return Result, ListN, ListM, ListBulls

    # -Analyzer--------------------------------------------------------------
    def analyzer(self, StepNum, List, Result, DigList):
        GoodList = []
        BadList = []
        ResultStep = 'WTF'

        if (Result[0] + Result[1]) > 0 & (Result[0] + Result[1]) < 4:
            ResultStep = ('MIDDLE')
            GoodList = 0
            BadList = List
        if Result[0] + Result[1] == 4:
            ResultStep = ('FULL')
            GoodList = List
        if Result[0] + Result[1] == 0:
            ResultStep = ('EMPTY')
            BadList = List

        if Result[0] == 4:
            ResultStep = ('COMPLETE')
            GoodList  = List

        if ((Result[0] == 0) & (Result[1] == 0)):
            for i in range(len(list(range(4)))):
                DigList[int(List[i])] = ['N', 'N', 'N', 'N']

        if ((Result[0] == 0) & (Result[1] >= 0)):
            for i in range(len(list(range(4)))):
                Digit = DigList[int(List[i])]
                Digit[i] = 'N'
                DigList[int(List[i])] = Digit

        if ((Result[0] > 0) & (Result[1] == 0)):
            for i in range(len(list(range(4)))):
                Digit = DigList[int(List[i])]
                Digit[i] = 'M'
                DigList[int(List[i])] = Digit
        ##if (StepNum >= 0):
        #3    print('Bulls:', Result[0], ' Cows:', Result[1], '\n')

        AnalyzePos_1 = self.analyzeBuCo(0, DigList)
        ##print('Result 0', AnalyzePos_1[3])
        AnalyzePos_2 = self.analyzeBuCo(1, DigList)
        ##print('Result 1', AnalyzePos_2[3])
        AnalyzePos_3 = self.analyzeBuCo(2, DigList)
        ##print('Result 2', AnalyzePos_3[3])
        AnalyzePos_4 = self.analyzeBuCo(3, DigList)
        ##print('Result 3', AnalyzePos_4[3])

        return ResultStep, GoodList, BadList, AnalyzePos_1, AnalyzePos_2, AnalyzePos_3, AnalyzePos_4
