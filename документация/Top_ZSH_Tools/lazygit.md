# lazygit (терминальный Git-клиент)

![Демо](https://raw.githubusercontent.com/jesseduffield/lazygit/master/docs/static/lazygit-demo.gif)

## Описание
Терминальный интерфейс для Git с:
- Визуализацией веток и коммитов
- Интерактивным rebase
- Управлением сташингом
- Диффами в реальном времени

## Установка
```bash
# Через Homebrew:
brew install lazygit

# Через Go:
go install github.com/jesseduffield/lazygit@latest

# Вручную:
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v*([^"]+)".*/\1/') &&
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz" &&
tar xf lazygit.tar.gz lazygit &&
sudo install lazygit /usr/local/bin
```

## Основное использование
```bash
# Запуск:
lazygit

# В конкретном репозитории:
lazygit -p ~/projects/my-repo
```

## Полезные примеры
```bash
# Просмотр логов:
lazygit log

# Интерактивный rebase:
lazygit rebase -i HEAD~5

# Отмена последнего коммита:
lazygit reset HEAD~1
```

## Интеграция с Zsh
Добавить алиас в ~/.zshrc:
```bash
alias lg='lazygit'
export LAZYGIT_CONFIG_DIR='~/.config/lazygit'
```

## Альтернативы
- tig
- gitui
- magit (для Emacs)

## Ссылки
- [Официальный репозиторий](https://github.com/jesseduffield/lazygit)
- [Документация](https://github.com/jesseduffield/lazygit#keybindings)
