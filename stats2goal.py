import json
import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

import utils as fn

cwd=os.getcwd()

if sys.platform=='win32':
    path=cwd+'\statsbomb\data'
else:
    path=cwd+'/statsbomb/data'

compet_df=fn.load_competition(path)

gender='male'
country='Spain'

team='Barcelona'
opp_team='Real Madrid'

sel_comp_df=fn.find_comp(compet_df,gender,country)

dpi=80
fps=1.5

# loop over seasons
for cid,sid in zip(sel_comp_df['competition_id'],sel_comp_df['season_id']): 
    
    matches_df=fn.sel_matches(path,cid,sid)
    year=matches_df['season'][0].get('season_name')
        
    match_id=fn.sel_stats(matches_df,team,opp_team)
    
    # loop over games
    for ev in match_id:

        event_df=fn.sel_match_file(path,ev)   
        
        out=fn.find_gol(event_df,team,opp_team,year,dpi,fps)