# Warp (революционный терминал)

![Демо](https://raw.githubusercontent.com/warpdotdev/Warp/main/docs/.gitbook/assets/demo.gif)

## Описание
Инновационный терминал для разработчиков с:
- Встроенным AI-ассистентом
- Блоковой структурой команд
- Совместной работой
- Визуальной историей

## Установка
```bash
# Только для macOS (через Homebrew):
brew install --cask warp

# Вручную (macOS):
curl -L https://warp-releases.storage.googleapis.com/latest/warp.pkg -o warp.pkg && sudo installer -pkg warp.pkg -target /

# Linux (в разработке):
echo "Warp пока доступен только для macOS. Linux версия в разработке."
```

## Основное использование
```bash
# AI-помощник:
Ctrl+Space  # Открыть AI-подсказки

# Блоки команд:
Shift+Enter  # Создать новый блок

# Поиск:
Ctrl+R  # Поиск по истории
```

## Полезные примеры
```bash
# Запуск команд с AI:
/write docker compose file for nginx

# Шаринг сессии:
/whoami  # Показать ваш user ID
/share   # Начать совместную сессию

# Работа с git:
/git checkout -b new-feature
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
# Автодополнение для Warp
if [[ "$TERM_PROGRAM" == "WarpTerminal" ]]; then
  export WARPSH_COMMAND_TIMEOUT=10000
fi
```

## Альтернативы
- iTerm2 (macOS)
- wezterm
- Hyper

## Ссылки
- [Официальный сайт](https://www.warp.dev/)
- [Документация](https://docs.warp.dev/)
