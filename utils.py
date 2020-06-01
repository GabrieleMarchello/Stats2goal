from PIL import Image

import json
import pandas as pd
import numpy as np
import sys
import os
import glob
import imageio

import plots as plot

def load_competition(path):

    if sys.platform=='win32':
        dir_path=path+'\competitions.json'
    else:
        dir_path=path+'/competitions.json'
        
    compet_data=json.load(open(dir_path,encoding='utf-8'))
    compet_df=pd.DataFrame(compet_data)
    
    return compet_df



def find_comp(df,gender,country):
    
    sel_row=df.loc[(df['competition_gender']==gender)&(df['country_name']==country)]
    
    comp_df=pd.DataFrame(columns=['season_name','competition_id','season_id'])
    
    compet_id=sel_row['competition_id']
    season_id=sel_row['season_id']
    season_year=sel_row['season_name']
    
    comp_df['season_name']=season_year
    comp_df['competition_id']=compet_id
    comp_df['season_id']=season_id
    
    return comp_df



def sel_matches(path,compet_id,season_id):
    
    if sys.platform=='win32':
        dir_path=path+'\matches\{0}\{1}.json'.format(compet_id,season_id)
    else:
        dir_path=path+'/matches/{0}/{1}.json'.format(compet_id,season_id)
        
    matches_data=json.load(open(dir_path,encoding='utf-8'))
    matches_df=pd.DataFrame(matches_data)
    
    return matches_df
    


def sel_stats(df,team,opp_team):
    
    match_id=[]
            
    for data_a,data_h,data_m in zip(df['away_team'],df['home_team'],df['match_id']):
        
        a=data_a['away_team_name']==team
        h=data_h['home_team_name']==team  
        
        a_opp=data_a['away_team_name']==opp_team
        h_opp=data_h['home_team_name']==opp_team  
        
        if (np.array(a) | np.array(h)) & (np.array(a_opp) | np.array(h_opp)):
            match_id.append(data_m)
    
    return match_id



def sel_match_file(path,match_id):
    
    if sys.platform=='win32':
        dir_path=path+'\events\{}.json'.format(match_id)
    else:
        dir_path=path+'/events/{}.json'.format(match_id)
        
    event_data=json.load(open(dir_path,encoding='utf-8'))
    event_df=pd.DataFrame(event_data)
    
    return event_df



def find_gol(df,team,opp_team,year,dpi,fps):
    
    gol_temp=[]
    df_gol=pd.DataFrame(columns=df.columns)
    df_gol_action_temp=pd.DataFrame(columns=df.columns)
    df_gol_action=pd.DataFrame(columns=df.columns)
    
    df_temp=df[df['shot'].notna()].copy()   
    
    home_team_temp=df['team'].iloc[0]
    home_team=home_team_temp.get('name')
    away_team_temp=df['team'].iloc[1]
    away_team=away_team_temp.get('name')
    
    for dshot in df_temp['shot']:
        
        shot_out_v=dshot.get('outcome')
        shot_out=shot_out_v['name']
        
        if shot_out=='Goal':
            gol_temp+=[df.loc[df['shot']==dshot].values[0]]
    
    df_gol=pd.DataFrame(gol_temp,columns=df.columns)

    cnt_gol_home=0
    cnt_gol_away=0

    for gol_id,gol_team in zip(df_gol['id'],df_gol['team']):
        
        gol_team_name=gol_team.get('name')
        
        if gol_team_name==home_team :
            cnt_gol_home+=1
        else:
            cnt_gol_away+=1
            
        if df_gol[df_gol['id']==gol_id].index[0]==0:
            index0=0
        else:
            index0=index_out+1
            
        indexf=df[df['id']==gol_id].index[0]+1
            
        df_gol_action_temp=df[index0:indexf]
        df_gol_action_temp=df_gol_action_temp.reindex(index=df_gol_action_temp.index[::-1])

        for dtype,did,dduel,dpass in zip(df_gol_action_temp['type'],
                                         df_gol_action_temp['id'],
                                         df_gol_action_temp['duel'],
                                         df_gol_action_temp['pass']):
            poss=dtype.get('name')
            
            if poss=='Duel':
                if dduel.get('outcome'):
                    duel_temp=dduel.get('outcome')
                    duel_out=duel_temp['name']
                
                    if  duel_out=='Won':
                        index_out=df_gol_action_temp[df_gol_action_temp['id']==did].index[0]+1
                        
                        break
                
            elif poss=='Pass':
                if dpass.get('outcome'):
                    pass_temp=dpass.get('outcome')
                    pass_out=pass_temp['name']
                
                    if  pass_out=='Incomplete' or pass_out=='Out':
                        index_out=df_gol_action_temp[df_gol_action_temp['id']==did].index[0]+1
                        
                        break
                
            elif ((poss=='Dispossessed') or
                  (poss=='Goal Keeper') or
                  (poss=='Foul won') or
                  (poss=='Ball Recovery') or
                  (poss=='Clearance') or
                  (poss=='Offside') or
                  (poss=='Interception') or
                  (poss=='Foul Committed')):
                
                index_out=df_gol_action_temp[df_gol_action_temp['id']==did].index[0]+1
                
                break

        df_gol_action=df_gol_action_temp[0:indexf-index_out+1]
        df_gol_action=df_gol_action.reindex(index=df_gol_action.index[::-1])
        
        fname=plot.draw_gol(df_gol_action,team,opp_team,home_team,away_team,year,cnt_gol_home,cnt_gol_away,dpi)
        imgs2list(fname,fps)
        
    return df_gol_action    
    



def imgs2list(fname,fps):
    
    cwd=os.getcwd()

    path=os.path.join(cwd,fname)

    img_list=[]
    
    for filename in glob.glob(path+'*.jpg'):
        im=Image.open(filename)
        img_list.append(im)
        
    imageio.mimsave(path+'.gif',img_list,format='GIF',fps=fps)
    
    return 0