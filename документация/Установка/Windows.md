# Установка на Windows

## Вариант 1: Через WSL2
1. Установите WSL2 и Ubuntu
2. Следуйте инструкциям для Linux

## Вариант 2: Нативная установка
1. Скачайте установщик .exe
2. Запустите от имени администратора
3. Добавьте в PATH:
```powershell
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;C:\Program Files\Package")
```
