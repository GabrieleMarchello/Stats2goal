import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time

import drawpitch as pitch

def draw_gol(df,team,opp_team,home,away,year,gol_home,gol_away,dpi):
    
    cnt_draw=0
    score='{0}-{1}'.format(gol_home,gol_away)
    
    for dtype,dpl,dloc,dteam,dpass,dcar,dshot in zip(df['type'],
                                                     df['player'],
                                                     df['location'],
                                                     df['team'],df['pass'],
                                                     df['carry'],df['shot']):
        
        type_name=dtype.get('name')
        
        if (('Camera On' not in type_name) and
            ('Camera off' not in type_name) and
            ('Bad Behaviour' not in type_name) and
            ('Miscontrol' not in type_name) and
            ('Block' not in type_name) and
            ('Tactical Shift' not in type_name)):
            
            fig=plt.figure() 
            pitch.draw_bckgnd() 
            plt.title(home+' Vs '+away+' - '+year)
            
            player=dpl.get('name')
            player_label=player
            
            xloc=dloc[0]
            yloc=dloc[1]
            
            team_name=dteam.get('name')
            if team_name==opp_team:
                xloc=120-xloc
                yloc=80-yloc
                marker_face_color='white'
                marker_edge_color='gold'
            else:
                marker_face_color='blue'
                marker_edge_color='crimson'
                                     
            if type_name=='Dispossessed':
                marker_type='o'
            elif type_name=='Duel' or type_name=='Foul Won' or type_name=='Ball Recovery' or type_name=='Offside' or type_name=='Interception':
                marker_type='X'
            elif type_name=='Pass':
                if dpass.get('outcome'):
                    marker_type='x'
                    endloc=dpass.get('end_location')
                    line_style='dashed'
                    xeloc=endloc[0]
                    yeloc=endloc[1]
                    dx=xeloc-xloc
                    dy=yeloc-yloc
                    if dx==0:
                        dx=1
                    if dy==0:
                        dy=1
                    plt.arrow(xloc,yloc,dx,dy,length_includes_head=True,head_width=2, head_length=3,color='black',zorder=2)
                    plt.scatter(xeloc,yeloc,marker=marker_type,color=marker_face_color,edgecolors=marker_edge_color,linewidths=2,s=100,zorder=2)            
                else:
                    marker_type='o'
                    rx_temp=dpass.get('recipient')
                    rx=rx_temp['name']
                    h_temp=dpass.get('height')
                    h=h_temp['name']
                    endloc=dpass.get('end_location')
                    line_style='dashed'
                    xeloc=endloc[0]
                    yeloc=endloc[1]
                    dx=xeloc-xloc
                    dy=yeloc-yloc
                    if dx==0:
                        dx=1
                    if dy==0:
                        dy=1
                    plt.arrow(xloc,yloc,dx,dy,length_includes_head=True,head_width=2, head_length=3,color='black',zorder=2)
                    plt.scatter(xeloc,yeloc,marker=marker_type,color=marker_face_color,edgecolors=marker_edge_color,linewidths=2,s=100,zorder=2)            
                    plt.text(xeloc-len(rx),yloc-10,rx)    
            elif type_name=='Pressure' or type_name=='Clearance':
                marker_type='o'
            elif type_name=='Ball Receipt*':
                marker_type='o'
            elif type_name=='Carry':
                marker_type='o'
                car_loc=dcar.get('end_location')
                xeloc=car_loc[0]
                yeloc=car_loc[1]
                dx=xeloc-xloc
                dy=yeloc-yloc
                if dx==0:
                    dx=1
                if dy==0:
                    dy=1
                plt.arrow(xloc,yloc,dx,dy,length_includes_head=True,head_width=2, head_length=3,color='black',zorder=2)
                plt.scatter(xeloc,yeloc,marker=marker_type,color=marker_face_color,edgecolors=marker_edge_color,linewidths=2,s=100,zorder=2)            
            elif type_name=='Shot':
                marker_type='*'     
                gol_loc=dshot.get('end_location')
                xeloc=gol_loc[0]
                yeloc=gol_loc[1]
                dx=xeloc-xloc
                dy=yeloc-yloc
                if dx==0:
                    dx=1
                if dy==0:
                    dy=1
                plt.arrow(xloc,yloc,dx,dy,length_includes_head=True,head_width=2, head_length=3,color='black',zorder=2)
                plt.text(30,43,'Gooooool',fontsize=30)
                plt.text(100,10,score,fontsize=22)
            elif type_name=='Goal Keeper':
                marker_type='o'
            elif type_name=='Dribble Past':
                marker_type='D'
            elif type_name=='Foul Committed':
                marker_type='X'
                
            plt.scatter(xloc,yloc,marker=marker_type,color=marker_face_color,edgecolors=marker_edge_color,linewidths=2,s=100,zorder=2)            
            plt.text(xloc-len(player_label),yloc+10,player_label)
            plt.text(2,76,type_name,fontsize=18) 
            
            fname=year[-7:-5]+year[-2:]+home+'Vs'+away+score
            
            plt.savefig(fname+'_{}.jpg'.format(str(cnt_draw).zfill(3)),dpi=dpi)
            cnt_draw+=1
        
    return fname