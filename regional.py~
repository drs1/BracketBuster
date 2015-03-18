import xml.etree.ElementTree as ET

# game order
# 1-16
# 8-9
# 5-12
# 4-13
# 6-11
# 3-14
# 7-10
# 2-15

class Regional:
    def __init__(self,bracket):
        self.bracket = bracket
        self.teams = [0]*16
        self.getTeams()
    def getTeams(self):
        for game in self.bracket:
            home = game[0].get('alias')
            away = game[1].get('alias')
            h_seed = int(game[0].get('seed'))
            if game[1].get('seed') is not None:
                a_seed = int(game[1].get('seed'))
            else: 
                a_seed = 16
            self.teams[h_seed-1] = home
            self.teams[a_seed-1] = away
    def simRegional(self,stat):
       return self.simRound(self.simFirstRound(stat),stat)

    def simRound(self,teams,stat):
        if len(teams) == 1:
            return teams
        else: 
            half = len(teams)/2
            nextRound = [0]*half
            for i in range(half):
                nextRound[i] = self.pick(teams[2*i],teams[2*i+1],stat)
            return self.simRound(nextRound,stat)

    def simFirstRound(self,stat):
        order = [1,8,5,4,6,3,7,2]
        x=0
        roundOf32 = [0]*8
        for number in order:
            roundOf32[x]=self.pick(self.teams[number-1],self.teams[16-number],stat)
            x+=1
        return roundOf32

    def pick(self,home, away, stat):
            #lookup their xml file
        home_stat = self.getStat(home,stat)
        away_stat = self.getStat(away,stat)
        return away if away_stat>home_stat else home  #break the ties to home team/higher seed
    
    def getStat(self,team, stat):
            #find the teams stat we're concerned with
        try:
            file = open('%s.xml'%team)
        except IOError:
            return 0
        tree = ET.parse(file)
        root = tree.getroot()[0][0][0][1]
        return root.get('%s'%stat)

