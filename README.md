# AnomETAS: Detection of non-ETAS seismic activities
The detection of non-ETAS seismic activity analysis presented here follow the work presented here:

Moutote, L., Marsan, D., Lengliné, O., Duputel, Z., 2021. Rare Occurrences of Non‐cascading Foreshock Activity in Southern California. Geophys Res Lett 48. https://doi.org/10.1029/2020GL091757

- We selected 53 mainshock (M>=4) in Southern california over a very complete catalog from template matching (QTM catalog : https://scedc.caltech.edu/data/qtm-catalog.html)
- We focused on the seismicity over 10 year within a 20 by 20 km box around each mainshock.
- We extracted typical temporal Epidemic Type Aftershock Sequence (ETAS) model parameter over the 10-year seismicity.
- We use the extracted ETAS model parameter to compute the number of event expected in short time widow and compare it with the number of event actually observed.
- Following a Poisson hypothesis for the natural variation of the expected number of event, we extracted a probability that the expected ETAS number of event explain the observed number of event in a short time window.
- We specifically focus on the result of the foreshock window (i.e. the window just before a mainshock), but we compute the probability using a 1-day shift slinding window over the full length of the local catalog.

# What you need:
- A numpy .npz file containing:
  - A temporal catalog of seismicity (Time vs Magnitude). The spatial ranges of the catalog must be small
  - The ETAS parameter of the catalog: A, c, p, alpha, mu and mc (see Eq. 1 in Moutote et al, 2021)

- The length of the window where will be computed the probability.

# What you get:
For each window in the slinding analysis:
  - The ETAS expected number of event that depend on the magnitude distribution observed before and within the window. This number is distributed along a Poisson law
  - The probability of observing at least the observed number of events considering the ETAs expected number of events. 
