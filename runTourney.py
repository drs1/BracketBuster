import xml.etree.ElementTree as ET
import time


def pickTourneyOn(stat):
    marchMadness = ET.parse('2015MarchMadness.xml')
    #we are in round 2
    round2 = marchMadness.getroot()[0][1]
    for bracket in round2:
        time.sleep(2.0)
        for game in bracket:
            home = game[0].get('alias')
            away = game[1].get('alias')
            print home,away


def pick(home, away, ordering):
    #lookup their xml file
    home_stat = getStat(home,ordering)
    away_stat = getStat(away,ordering)
    return away if away_stat>home_stat else home  #break the ties to home team/higher seed

def getStat(team, stat):
    #find the teams stat we're concerned with
    try:
        file = open('%s.xml'%team)
    except IOError:
        return 0
    tree = ET.parse(file)
    root = tree.getroot()[0][0][0][1]
    return root.get('%s'%stat)

pickTourneyOn('second_chance_pts')
    


