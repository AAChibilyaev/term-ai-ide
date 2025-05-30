# delta (просмотрщик git diff)

![Демо](https://raw.githubusercontent.com/dandavison/delta/master/assets/delta-demo.png)

## Описание
Современный просмотрщик различий для git с:
- Синтаксической подсветкой
- Боковым сравнением
- Поддержкой pager
- Настраиваемыми темами

## Установка
```bash
# Через Homebrew:
brew install git-delta

# Через apt (Ubuntu/Debian):
sudo apt install git-delta

# Вручную:
wget https://github.com/dandavison/delta/releases/latest/download/delta-x86_64-unknown-linux-gnu.tar.gz
tar -xzf delta-*.tar.gz && sudo mv delta-*/delta /usr/local/bin
```

## Основное использование
```bash
# Использование с git:
git config --global core.pager "delta"

# Просмотр файла:
delta file1.txt file2.txt

# Темный режим:
delta --dark
```

## Полезные примеры
```bash
# Игнорирование пробелов:
delta --ignore-space-change file1 file2

# Сравнение директорий:
delta -d dir1/ dir2/

# Настройка git:
git config --global interactive.diffFilter "delta --color-only"
```

## Интеграция с Zsh
Добавить в ~/.zshrc:
```bash
export DELTA_PAGER="less -RFX"
export DELTA_FEATURES="+side-by-side"
```

## Альтернативы
- diff-so-fancy
- icdiff
- git diff с цветами

## Ссылки
- [Официальный репозиторий](https://github.com/dandavison/delta)
- [Документация](https://github.com/dandavison/delta#get-started)
