# bat (лучшая замена cat)

![Демо](https://raw.githubusercontent.com/sharkdp/bat/master/assets/demo.gif)

## Описание
Современная замена cat с:
- Подсветкой синтаксиса для 200+ языков
- Интеграцией с git (показывает изменения)
- Автоматической пагинацией
- Поддержкой UTF-8 и цветов

## Установка
```bash
# Через Homebrew:
brew install bat

# Через apt (Ubuntu/Debian):
sudo apt install bat

# Вручную:
cargo install bat
```

## Основное использование
```bash
# Просмотр файла:
bat file.txt

# Показ номеров строк:
bat -n file.js

# Вывод без оформления:
bat --plain file.log
```

## Полезные примеры
```bash
# Просмотр нескольких файлов:
bat src/*.js

# Поиск с подсветкой:
bat -p file.txt | grep --color "pattern"

# Сравнение через дельту:
bat -d file1.txt file2.txt
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias cat=bat  # Полная замена cat
export BAT_THEME="TwoDark"
```

## Альтернативы
- GNU cat
- highlight
- ccat

## Ссылки
- [Официальный репозиторий](https://github.com/sharkdp/bat)
- [Документация](https://github.com/sharkdp/bat#how-to-use)
