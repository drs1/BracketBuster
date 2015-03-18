import xml.etree.ElementTree as ET
from regional import Regional
import time


stats = ['second_chance_pts', 'points_off_turnovers','paint_pts', 'fast_break_pts', 'points', 'blocked_att', 'turnovers' ,'free_throws_att', 'field_goals_att', 'off_rebounds', 'two_points_att', 'assists', 'blocks', 'personal_fouls', 'two_points_made', 'flagrant_fouls', 'rebounds', 'three_points_made', 'minutes', 'def_rebounds', 'free_throws_made', 'field_goals_made', 'steals', 'three_points_att']

def pickTourneyOn(stat):
    marchMadness = ET.parse('2015MarchMadness.xml')
    #we are in round 2
    round2 = marchMadness.getroot()[0][1]
    for r in round2:
        regional = Regional(r)
        print regional.simRegional(stat)
        
for s in stats:
    print s 
    pickTourneyOn(s)
    print '\n'


