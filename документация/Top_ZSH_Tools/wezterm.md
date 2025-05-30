# wezterm (современный терминал)

![Демо](https://raw.githubusercontent.com/wez/wezterm/main/assets/demo/shell.png)

## Описание
Мощный кросс-платформенный терминал с:
- GPU-ускорением
- Встроенным мультиплексором
- Поддержкой лигатур
- Кастомными вкладками и панелями

## Установка
```bash
# Через Homebrew:
brew install --cask wezterm

# Через apt (Ubuntu/Debian):
curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/wezterm.gpg
echo "deb [signed-by=/usr/share/keyrings/wezterm.gpg] https://apt.fury.io/wez/ * *" | sudo tee /etc/apt/sources.list.d/wezterm.list
sudo apt update && sudo apt install wezterm

# Вручную:
curl -LO https://github.com/wez/wezterm/releases/latest/download/wezterm-ubuntu20.04.AppImage
chmod +x wezterm-*.AppImage && ./wezterm-*.AppImage
```

## Основное использование
```bash
# Запуск:
wezterm start

# Горячие клавиши:
Ctrl+Shift+n  # Новое окно
Ctrl+Shift+t  # Новая вкладка
Ctrl+Shift+w  # Закрыть вкладку
```

## Полезные примеры
```bash
# Запуск команды:
wezterm start -- zellij

# Удалённое подключение:
wezterm ssh user@host

# Создание конфига:
wezterm cli spawn --config-file ~/.config/wezterm/wezterm.lua
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
# Автозапуск zellij в wezterm
if [[ "$TERM_PROGRAM" == "WezTerm" ]]; then
  eval "$(zellij setup --generate-auto-start zsh)"
fi
```

## Альтернативы
- Alacritty
- Kitty
- iTerm2 (macOS)

## Ссылки
- [Официальный репозиторий](https://github.com/wez/wezterm)
- [Конфигурация](https://wezfurlong.org/wezterm/config/files.html)
