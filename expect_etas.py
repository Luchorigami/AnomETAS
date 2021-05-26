import numpy as np
import glob
import time
import scipy.stats as sc
plt.close('all')

# Load Etas estimation file's paths
fittedpaths = glob.glob('localcatalogs_and_etas_parameter_estimations/*npz')


for ipath in range(len(fittedpaths)):
    # Load estimation
    fittedETAS      = np.load(fittedpaths[ipath])
    A               = fittedETAS.f.A
    c               = fittedETAS.f.c
    p               = fittedETAS.f.p
    alpha           = fittedETAS.f.alpha
    mu              = fittedETAS.f.mu
    mc              = fittedETAS.f.mc
    IDmain          = fittedETAS.f.IDmain
    ID              = fittedETAS.f.ID
    tday            = fittedETAS.f.tday
    mag             = fittedETAS.f.mag

    print('\nMainshock %d / %d n°%d\n'%(ipath+1,len(fittedpaths),int(IDmain)))
     
    # Mainshock caracteristics 
    imain           = np.where(ID==IDmain)[0]    
    tmain           = tday  [imain]
    magmain         = mag   [imain]
    
    # Length of foreshock window in days
    fw              = 20
    # 1-day shift slinding window analysis : End time of each windows 
    twinends        = np.concatenate( [ np.flip( np.arange(tmain,tday[0],-1)) , np.arange(tmain+1,tday[-1],1)] ) 
  
    Naft            = [] # Nb of expected aftershocks in each windows
    bgd             = [] # Nb of expected background earthquakes in each windows
    Nobs            = [] # Observed Nb of earthqukes in each windows

    # 1-day shift slinding window analysis
    for twe in twinends:
        # Integration of ETAS formula for events before the current window
        i_out       = np.where(tday < twe-fw)[0]
        t_out       = tday[i_out]
        m_out       = mag [i_out]
        Naft_out    = np.sum( A*np.exp(alpha*(m_out-mc))/(1-p) * ((twe-t_out + c)**(1-p) - (twe-fw-t_out + c)**(1-p)) )

        # Integration of ETAS formula for event within the current window
        i_in        = np.where((tday >= twe-fw)*(tday<twe))[0]
        t_in        = tday[i_in]
        m_in        = mag [i_in]
        Naft_in     = np.sum( A*np.exp(alpha*(m_in-mc))/(1-p)  * ((twe-t_in + c)**(1-p) -c**(1-p)) )

        # Number of aftershock = in + out
        Naft        .append(Naft_out + Naft_in)   

        # Real observed number
        Nobs        .append(len(i_in))

    Nobs            = np.array(Nobs) 
    
    # Expected number of event = Naft + background seismicity
    bgd             = mu*fw
    Nexpect         = np.array(Naft) + np.array(bgd)
      
    # Evaluate the probabilty of observing at least Nobs along a poisson law of mean Nexpect
    prob            = sc.poisson.cdf(Nobs,Nexpect)
    prob            = 1-prob
    
    # Case Nobs=0 => p(Netas>=Nobs) = 1 
    prob[np.where(Nobs==0)[0]]=1

    # Center time axis on the mainshock 
    twinendsmain    = twinends-tmain
    
    # position of the foreshock window (i.e. the window just before the mainshsock ) 
    iwin            = np.where(twinendsmain == 0)[0]
    probw           = prob[iwin]

    if len(probw)==0:
        probw = 1

    np.savez('%s.expect.alf'%IDmain,prob=prob,Nexpect=Nexpect,probw=probw,Naft=Naft,bgd=bgd,twinendsmain=twinendsmain,IDmain=IDmain,tday=tday,mag=mag,tmain=tmain,magmain=magmain)



