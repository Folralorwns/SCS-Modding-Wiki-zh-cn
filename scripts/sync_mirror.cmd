@echo off
rem Daily sync of the SCS Modding Wiki mirror (English + Chinese merge).
rem Register with:
rem   schtasks /Create /SC DAILY /ST 03:00 /TN "scs-wiki-sync" /TR "E:\SCS-Modding-Wiki-zh-cn\scripts\sync_mirror.cmd"
cd /d "%~dp0.."
python scripts\sync_mirror.py --log
