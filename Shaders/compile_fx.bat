@echo off
fxc /D PS_2_X=ps_2_a /T fx_2_0 /Gpp /O3 /Fo mb_2a.fxo mbsrc.fx
fxc /D PS_2_X=ps_2_b /T fx_2_0 /Gpp /O3 /Fo mb_2b.fxo mbsrc.fx


echo Script processing has ended.
echo Press any key to exit. . .
pause>nul