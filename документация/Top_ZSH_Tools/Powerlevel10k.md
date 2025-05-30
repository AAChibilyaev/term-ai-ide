# Powerlevel10k

![Лого](https://raw.githubusercontent.com/romkatv/powerlevel10k-media/master/prompt-styles-high-contrast.png)

## Описание
Powerlevel10k - это быстрая и настраиваемая тема для Zsh с:
- Молниеносной скоростью работы
- Встроенными иконками
- Адаптивным промптом
- Визуализацией состояния Git

## Установка
```bash
# Для Oh My Zsh:
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Для чистого Zsh:
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
```

## Основное использование
```bash
# Активация в .zshrc:
ZSH_THEME="powerlevel10k/powerlevel10k"

# Настройка:
p10k configure
```

## Полезные примеры
```bash
# Просмотр всех сегментов:
typeset -pm 'POWERLEVEL9K_*'

# Быстрое обновление:
git -C ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k pull
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
# Опционально для ускорения
POWERLEVEL9K_DISABLE_CONFIGURATION_WIZARD=true
POWERLEVEL9K_INSTANT_PROMPT=quiet
```

## Альтернативы
- Starship
- Spaceship
- Agnoster

## Ссылки
- [Официальный репозиторий](https://github.com/romkatv/powerlevel10k)
- [Документация](https://github.com/romkatv/powerlevel10k#readme)
