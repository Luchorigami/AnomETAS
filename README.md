# Detection of non-ETAS seismic activities
The detecttion of non-ETAS seismicity analysis presented here follow the work presented here:

Moutote, L., Marsan, D., Lengliné, O., Duputel, Z., 2021. Rare Occurrences of Non‐cascading Foreshock Activity in Southern California. Geophys Res Lett 48. https://doi.org/10.1029/2020GL091757

- We selected 53 mainshock (M>=4) in Southern california over a very complete catalog from template matching (QTM catalog : https://scedc.caltech.edu/data/qtm-catalog.html)
- We focused on the seismicity over 10 year within a 20 by 20 km box around each mainshock.
- We extracted typical temporal Epidemic Type Aftershock Sequence (ETAS) model parameter over the 10-year seismicity.
- We use the extracted ETAS model parameter to compute the number of event expected in short time widow and compare it with the number of event actually observed.
- Following a Poisson hypothesis for the natural variation of the expected number of event, we extracted a probability that the expected ETAS number of event explain the observed number of event in a short time window.

# How to run
