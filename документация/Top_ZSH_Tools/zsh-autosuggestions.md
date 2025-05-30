# zsh-autosuggestions

![Демо](https://raw.githubusercontent.com/zsh-users/zsh-autosuggestions/master/img/demo.gif)

## Описание
Плагин для Zsh, который предлагает автоматические подсказки команд на основе истории. Особенности:
- Серые подсказки по мере ввода
- Принимаются клавишей → или Ctrl+E
- Не замедляет работу терминала

## Установка
```bash
# Для Oh My Zsh:
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Вручную:
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
```

## Основное использование
```bash
# Активация в .zshrc:
plugins=(zsh-autosuggestions)

# Или для ручной установки:
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
```

## Полезные примеры
```bash
# Изменение цвета подсказок:
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#ff00ff,bg=cyan,bold,underline"

# Игнорирование определённых команд:
ZSH_AUTOSUGGEST_HISTORY_IGNORE="cd *|ls *|rm *"
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
# Ускорение работы
ZSH_AUTOSUGGEST_USE_ASYNC=true
ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=20
```

## Альтернативы
- fish-style-autosuggestions
- zsh-completions

## Ссылки
- [Официальный репозиторий](https://github.com/zsh-users/zsh-autosuggestions)
- [Документация](https://github.com/zsh-users/zsh-autosuggestions/blob/master/README.md)
