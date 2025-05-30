# starship (кросс-шелл prompt)

![Демо](https://raw.githubusercontent.com/starship/starship/master/media/demo.gif)

## Описание
Быстрый и настраиваемый prompt для:
- Любых shell (Zsh, Bash, Fish)
- Показ git статуса, версий ПО и времени
- Минимальное влияние на скорость работы
- Поддержка иконок и кастомных модулей

## Установка
```bash
# Через Homebrew:
brew install starship

# Через curl:
curl -sS https://starship.rs/install.sh | sh

# Вручную:
cargo install starship
```

## Основное использование
```bash
# Инициализация в .zshrc:
eval "$(starship init zsh)"

# Проверка конфига:
starship explain
```

## Полезные примеры
```bash
# Показ всех модулей:
starship module --list

# Предпросмотр конфига:
starship print-config

# Быстрое обновление:
starship update
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
export STARSHIP_CONFIG=~/.config/starship.toml
export STARSHIP_CACHE=~/.starship/cache
```

## Альтернативы
- Powerlevel10k
- Spaceship
- Pure

## Ссылки
- [Официальный репозиторий](https://github.com/starship/starship)
- [Конфигуратор](https://starship.rs/config/)
