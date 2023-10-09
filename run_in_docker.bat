@echo off
call env_docker.bat

:: Enable delayed variable expansion
setlocal enabledelayedexpansion

:: Get the current date and time in ISO 8601 format
for /f "delims=" %%a in ('wmic os get LocalDateTime ^| find "."') do set DATE_WITH_TIME=%%a
set DATE_WITH_TIME=!DATE_WITH_TIME:~0,4!!DATE_WITH_TIME:~4,2!!DATE_WITH_TIME:~6,2!_!DATE_WITH_TIME:~8,2!!DATE_WITH_TIME:~10,2!!DATE_WITH_TIME:~12,2!

:: Run the Docker command with variable expansion using "!"
docker run --rm -it ^
-v %cd%\mbtest:/automation/mbtest ^
-e WC_KEY=%WC_KEY% ^
-e WC_SECRET=%WC_SECRET% ^
-e WP_HOST=%WP_HOST% ^
-e MACHINE=%MACHINE% ^
-e DB_USER=%DB_USER% ^
-e DB_PASSWORD=%DB_PASSWORD% ^
mbtest_api_python ^
pytest -c /automation/mbtest/pytest.ini ^
--html /automation/mbtest/results/report_!DATE_WITH_TIME!.html ^
-m tcid55

:: End the local scope with delayed variable expansion
endlocal
