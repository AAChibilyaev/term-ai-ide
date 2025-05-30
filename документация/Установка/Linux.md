# Установка на Linux

## Поддерживаемые дистрибутивы
- Ubuntu/Debian
- CentOS/RHEL
- Arch Linux
- Fedora

## Способ 1: Через пакетный менеджер
```bash
# Для Ubuntu/Debian
sudo apt update && sudo apt install package-name

# Для CentOS/RHEL
sudo yum install package-name

# Для Arch
sudo pacman -S package-name
```

## Способ 2: Ручная установка
1. Скачайте последнюю версию:
```bash
wget https://example.com/package-latest.tar.gz
```
2. Распакуйте и установите:
```bash
tar -xzf package-latest.tar.gz
cd package
./configure
make
sudo make install
```
