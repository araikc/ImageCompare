@echo off

set image1=%1
set image2=%2
set t1=
set t2=
SHIFT & SHIFT

:loop
if not "%1"=="" (

	if "%1"=="-t1" (
		set t1=-t1 %2
		SHIFT
	)
	if "%1"=="-t2" (
		set t2=-t2 %2
		SHIFT
	)
	SHIFT
	GOTO :loop

)


python.exe .\isequal.py -i1 "%image1%" -i2 "%image2%" %t1% %t2%
