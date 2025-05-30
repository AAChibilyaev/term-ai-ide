# exa (современная замена ls)

![Демо](https://raw.githubusercontent.com/ogham/exa/master/screenshots.png)

## Описание
Продвинутая замена ls с:
- Цветным выводом и иконками
- Встроенной поддержкой git
- Древовидным отображением
- Метаданными в компактном формате

## Установка
```bash
# Через Homebrew:
brew install exa

# Через apt (Ubuntu/Debian):
sudo apt install exa

# Вручную:
cargo install exa
```

## Основное использование
```bash
# Стандартный вывод:
exa

# Детализированный вывод:
exa -l

# Древовидное отображение:
exa -T
```

## Полезные примеры
```bash
# Сортировка по размеру:
exa -l --sort=size

# Показ git статуса:
exa -l --git

# Рекурсивный просмотр:
exa -R
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias ls=exa  # Полная замена ls
alias ll='exa -l --git'
alias la='exa -la --git'
```

## Альтернативы
- GNU ls
- lsd
- colorls

## Ссылки
- [Официальный репозиторий](https://github.com/ogham/exa)
- [Документация](https://github.com/ogham/exa#options)
