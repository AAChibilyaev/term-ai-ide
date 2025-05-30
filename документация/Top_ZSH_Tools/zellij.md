# zellij (современный терминальный мультиплексор)

![Демо](https://raw.githubusercontent.com/zellij-org/zellij/main/assets/demo.gif)

## Описание
Современная альтернатива tmux с:
- Встроенными панелями и вкладками
- Поддержкой плагинов
- Автоматическим layout-менеджером
- Подсветкой синтаксиса

## Установка
```bash
# Через Homebrew:
brew install zellij

# Через cargo:
cargo install zellij

# Вручную:
curl -L https://github.com/zellij-org/zellij/releases/latest/download/zellij-x86_64-unknown-linux-musl.tar.gz | tar xz
sudo install zellij /usr/local/bin
```

## Основное использование
```bash
# Запуск:
zellij

# Горячие клавиши:
Ctrl+g n  # Новая вкладка
Ctrl+g h  # Разделить горизонтально
Ctrl+g v  # Разделить вертикально
```

## Полезные примеры
```bash
# Запуск с layout:
zellij --layout ~/.config/zellij/dev.yaml

# Прикрепление к сессии:
zellij attach -c mysession

# Просмотр всех сессий:
zellij list-sessions
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
# Автозапуск zellij
if [[ -z "$ZELLIJ" && -z "$TMUX" ]]; then
  zellij attach -c default || zellij
fi
```

## Альтернативы
- tmux
- screen
- wezterm (встроенный мультиплексор)

## Ссылки
- [Официальный репозиторий](https://github.com/zellij-org/zellij)
- [Документация](https://zellij.dev/documentation/)
