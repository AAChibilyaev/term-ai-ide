# tmux (терминальный мультиплексор)

![Демо](https://raw.githubusercontent.com/tmux/tmux/master/tmux.gif)

## Описание
Мощный инструмент для управления терминальными сессиями:
- Разделение экрана на панели
- Фоновые сессии
- Сессии сохраняются после разрыва соединения
- Полная кастомизация

## Установка
```bash
# Через Homebrew:
brew install tmux

# Через apt (Ubuntu/Debian):
sudo apt install tmux

# Сборка из исходников:
git clone https://github.com/tmux/tmux.git
cd tmux && sh autogen.sh && ./configure && make
```

## Основное использование
```bash
# Новая сессия:
tmux new -s mysession

# Разделение экрана:
Ctrl+b %  # Вертикально
Ctrl+b "  # Горизонтально

# Список сессий:
tmux ls
```

## Полезные примеры
```bash
# Автозапуск команд:
tmux new -d 'top'

# Копирование в буфер:
Ctrl+b [  # Режим копирования

# Подключение к сессии:
tmux attach -t mysession
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
# Автозапуск tmux
if [[ -z "$TMUX" ]] && [ "$SSH_CONNECTION" != "" ]; then
  tmux attach || tmux new
fi
```

## Альтернативы
- screen
- zellij
- byobu

## Ссылки
- [Официальный репозиторий](https://github.com/tmux/tmux)
- [Шпаргалка](https://tmuxcheatsheet.com/)
