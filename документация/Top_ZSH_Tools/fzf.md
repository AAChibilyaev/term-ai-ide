# fzf (Fuzzy Finder)

![Демо](https://raw.githubusercontent.com/junegunn/i/master/fzf.gif)

## Описание
Универсальный инструмент для нечеткого поиска с:
- Интерактивным интерфейсом
- Поддержкой предпросмотра файлов
- Интеграцией с Zsh, Vim и другими инструментами
- Молниеносной скоростью работы

## Установка
```bash
# Через Homebrew:
brew install fzf

# Установка скриптов:
$(brew --prefix)/opt/fzf/install

# Вручную:
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

## Основное использование
```bash
# Поиск файлов:
fzf

# Поиск в истории команд:
Ctrl+R

# Поиск процессов:
ps aux | fzf
```

## Полезные примеры
```bash
# Открытие выбранного файла в Vim:
vim $(fzf)

# Поиск и переход в директорию:
cd $(find * -type d | fzf)

# Интеграция с Git:
git checkout $(git branch | fzf)
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border'
```

## Альтернативы
- skim
- peco
- percol

## Ссылки
- [Официальный репозиторий](https://github.com/junegunn/fzf)
- [Документация](https://github.com/junegunn/fzf#usage)
