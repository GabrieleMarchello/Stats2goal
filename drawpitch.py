import matplotlib.pyplot as plt

def draw_bckgnd():
    
    ptlx=0
    ptly=0
    pblx=0
    pbly=80
    ptrx=120
    ptry=0
    pbrx=120
    pbry=80
    
    ctx=60
    cty=0
    cbx=60
    cby=80
    
    a1tlx=0
    a1tly=18 
    a1blx=0
    a1bly=62 
    a1trx=18
    a1try=18 
    a1brx=18
    a1bry=62
    
    a2tlx=120
    a2tly=18
    a2blx=120
    a2bly=62
    a2trx=102
    a2try=18
    a2brx=102
    a2bry=62

    pnl1x=12
    pnl1y=40
    cpx=60
    cpy=40
    pnl2x=108
    pnl2y=40
    
    gl1tx=0
    gl1ty=36
    gl1bx=0
    gl1by=44
    
    gl2tx=120
    gl2ty=36
    gl2bx=120
    gl2by=44
    
    cl='white'
    cg='black'
    
    # fig=plt.figure()
    # fig.patch.set_facecolor('white')
    ax=plt.gca()
    ax.set_facecolor('xkcd:light green')
    ax.set(xlim=(-7,128),ylim=(-7,85))
    ax.invert_yaxis()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    
    plt.plot([ptlx,ptrx],[ptly,ptry],linewidth=3,color=cl,zorder=1)
    plt.plot([pblx,pbrx],[pbly,pbry],linewidth=3,color=cl,zorder=1)
    plt.plot([ptlx,pblx],[ptly,pbly],linewidth=3,color=cl,zorder=1)
    plt.plot([ptrx,pbrx],[ptry,pbry],linewidth=3,color=cl,zorder=1)
    plt.plot([ctx,cbx],[cty,cby],linewidth=3,color=cl,zorder=1)
    plt.plot([a1tlx,a1trx],[a1tly,a1try],linewidth=3,color=cl,zorder=1)
    plt.plot([a1blx,a1brx],[a1bly,a1bry],linewidth=3,color=cl,zorder=1)
    plt.plot([a1trx,a1brx],[a1try,a1bry],linewidth=3,color=cl,zorder=1)
    plt.plot([a2tlx,a2trx],[a2tly,a2try],linewidth=3,color=cl,zorder=1)
    plt.plot([a2blx,a2brx],[a2bly,a2bry],linewidth=3,color=cl,zorder=1)
    plt.plot([a2trx,a2brx],[a2try,a2bry],linewidth=3,color=cl,zorder=1)
    plt.plot([pnl1x,cpx,pnl2x],[pnl1y,cpy,pnl2y],marker='o',color=cl,markerfacecolor=cl,linestyle='none',zorder=1)
    plt.plot([gl1tx,gl1bx],[gl1ty,gl1by],linewidth=3,color=cg,zorder=2)
    plt.plot([gl2tx,gl2bx],[gl2ty,gl2by],linewidth=3,color=cg,zorder=2)
    
    return 0