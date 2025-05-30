# dust (анализ дискового пространства)

![Демо](https://raw.githubusercontent.com/bootandy/dust/master/assets/example.png)

## Описание
Более интуитивная замена du с:
- Визуализацией использования пространства
- Сортировкой по размеру
- Поддержкой цветного вывода
- Быстрой работой

## Установка
```bash
# Через Homebrew:
brew install dust

# Через cargo:
cargo install du-dust

# Вручную:
wget https://github.com/bootandy/dust/releases/latest/download/dust-x86_64-unknown-linux-gnu.tar.gz
tar -xzf dust-*.tar.gz && sudo mv dust-*/dust /usr/local/bin
```

## Основное использование
```bash
# Анализ текущей директории:
dust

# Анализ конкретной папки:
dust ~/Downloads

# Показ N самых больших элементов:
dust -n 10
```

## Полезные примеры
```bash
# Игнорирование скрытых файлов:
dust -i

# Вывод в плоском формате:
dust -f

# Анализ только 3 уровней вложенности:
dust -d 3
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias du='dust'
alias dus='dust -s'
```

## Альтернативы
- ncdu
- duf
- gdu

## Ссылки
- [Официальный репозиторий](https://github.com/bootandy/dust)
- [Документация](https://github.com/bootandy/dust#usage)