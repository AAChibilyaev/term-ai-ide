# zsh-syntax-highlighting

![Демо](https://raw.githubusercontent.com/zsh-users/zsh-syntax-highlighting/master/images/after.png)

## Описание
Плагин для подсветки синтаксиса команд в Zsh в реальном времени:
- Подсвечивает корректные команды зеленым
- Некорректные команды - красным
- Подсказывает ошибки до выполнения
- Работает с 256 цветами

## Установка
```bash
# Для Oh My Zsh:
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Вручную:
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting
```

## Основное использование
```bash
# Активация в .zshrc:
plugins=(zsh-syntax-highlighting)

# Или для ручной установки:
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

## Полезные примеры
```bash
# Изменение цветов:
ZSH_HIGHLIGHT_STYLES[command]='fg=blue,bold'
ZSH_HIGHLIGHT_STYLES[path]='fg=cyan'

# Игнорирование определенных паттернов:
ZSH_HIGHLIGHT_REGEXP+=('^rm -rf')
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
# Оптимизация производительности
ZSH_HIGHLIGHT_MAXLENGTH=300
```

## Альтернативы
- fish-syntax-highlighting
- bash-syntax-highlighting

## Ссылки
- [Официальный репозиторий](https://github.com/zsh-users/zsh-syntax-highlighting)
- [Документация](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/README.md)
