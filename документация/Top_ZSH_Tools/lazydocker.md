# lazydocker (терминальный Docker-клиент)

![Демо](https://raw.githubusercontent.com/jesseduffield/lazydocker/master/docs/resources/demo.gif)

## Описание
Терминальный интерфейс для Docker с:
- Управлением контейнерами, образами и томами
- Просмотром логов в реальном времени
- Графическим представлением зависимостей
- Поддержкой docker-compose

## Установка
```bash
# Через Homebrew:
brew install lazydocker

# Через Go:
go install github.com/jesseduffield/lazydocker@latest

# Вручную:
curl -L https://github.com/jesseduffield/lazydocker/releases/latest/download/lazydocker_Linux_x86_64.tar.gz | tar xz -C /tmp
sudo mv /tmp/lazydocker /usr/local/bin
```

## Основное использование
```bash
# Запуск:
lazydocker

# Фильтрация контейнеров:
Ctrl+f

# Просмотр логов:
l
```

## Полезные примеры
```bash
# Запуск в конкретном проекте:
lazydocker --context my-project

# Перезагрузка контейнера:
r

# Очистка системы:
d (меню удаления)
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias lzd='lazydocker'
export LAZYDOCKER_CONFIG_DIR='~/.config/lazydocker'
```

## Альтернативы
- dockly
- ctop
- Portainer (web-интерфейс)

## Ссылки
- [Официальный репозиторий](https://github.com/jesseduffield/lazydocker)
- [Документация](https://github.com/jesseduffield/lazydocker#keybindings)
