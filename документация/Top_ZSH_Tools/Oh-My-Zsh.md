# Oh My Zsh

![Лого](https://ohmyz.sh/img/OMZLogo_BnW.png)

## Описание
Oh My Zsh - это популярный фреймворк для управления конфигурацией Zsh. Включает:
- 250+ плагинов
- 150+ тем
- Автоматические обновления
- Упрощенную настройку

## Установка
```bash
# Стандартная установка:
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Через Homebrew:
brew install oh-my-zsh
```

## Основное использование
```bash
# Смена темы:
sed -i 's/ZSH_THEME=".*"/ZSH_THEME="agnoster"/' ~/.zshrc

# Добавление плагина:
plugins=(git zsh-autosuggestions)
```

## Полезные примеры
```bash
# Просмотр всех тем:
ls $ZSH/themes

# Обновление:
omz update
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
export ZSH="$HOME/.oh-my-zsh"
source $ZSH/oh-my-zsh.sh
```

## Альтернативы
- Prezto
- Zim
- Antibody

## Ссылки
- [Официальный репозиторий](https://github.com/ohmyzsh/ohmyzsh)
- [Документация](https://ohmyz.sh/)
