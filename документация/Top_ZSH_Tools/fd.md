# fd (простая альтернатива find)

![Лого](https://raw.githubusercontent.com/sharkdp/fd/master/doc/screencast.svg)

## Описание
Быстрая и удобная альтернатива GNU find с:
- Цветным выводом
- Умным регистронезависимым поиском
- Игнорированием .gitignore по умолчанию
- В 3-5 раз быстрее find

## Установка
```bash
# Через Homebrew:
brew install fd

# Через apt (Ubuntu/Debian):
sudo apt install fd-find

# Вручную:
cargo install fd-find
```

## Основное использование
```bash
# Простой поиск:
fd pattern

# Поиск по расширению:
fd -e md

# Поиск с глубиной:
fd --max-depth 2
```

## Полезные примеры
```bash
# Поиск и редактирование:
vim $(fd -t f 'config' | fzf)

# Поиск с исполнением команды:
fd -0 '*.log' | xargs -0 rm

# Игнорирование node_modules:
fd --ignore-case --no-ignore-vcs react
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias find=fd  # Полная замена find
export FD_DEFAULT_OPTS="--color=always --hidden"
```

## Альтернативы
- GNU find
- ripgrep (для содержимого файлов)
- locate

## Ссылки
- [Официальный репозиторий](https://github.com/sharkdp/fd)
- [Документация](https://github.com/sharkdp/fd#how-to-use)
