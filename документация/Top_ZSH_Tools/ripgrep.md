# ripgrep (rg) - молниеносный поиск

![Демо](https://raw.githubusercontent.com/BurntSushi/ripgrep/master/benchsuite/bench-speed.png)

## Описание
Современная замена grep с:
- Автоматическим игнорированием .gitignore
- Поддержкой UTF-8
- В 5-10 раз быстрее grep
- Цветным выводом и нумерацией строк

## Установка
```bash
# Через Homebrew:
brew install ripgrep

# Через apt (Ubuntu/Debian):
sudo apt install ripgrep

# Вручную:
cargo install ripgrep
```

## Основное использование
```bash
# Простой поиск:
rg "pattern"

# Поиск в определённых файлах:
rg "React" -g "*.jsx"

# Поиск без .gitignore:
rg -uuu "password"
```

## Полезные примеры
```bash
# Поиск с контекстом:
rg "error" -A 3 -B 2

# Поиск только имён файлов:
rg -l "TODO"

# Поиск с JSON выводом:
rg --json "pattern"
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias grep=rg  # Полная замена grep
export RIPGREP_CONFIG_PATH="$HOME/.ripgreprc"
```

## Альтернативы
- GNU grep
- ack
- silver searcher (ag)

## Ссылки
- [Официальный репозиторий](https://github.com/BurntSushi/ripgrep)
- [Документация](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)
