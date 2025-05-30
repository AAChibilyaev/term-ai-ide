# jq (командный JSON-процессор)

![Демо](https://raw.githubusercontent.com/stedolan/jq/master/screenshot.png)

## Описание
Мощный инструмент для обработки JSON с:
- Гибким языком запросов
- Поддержкой пайпов
- Фильтрацией и трансформацией данных
- Форматированием вывода

## Установка
```bash
# Через Homebrew:
brew install jq

# Через apt (Ubuntu/Debian):
sudo apt install jq

# Вручную:
wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -O ~/bin/jq && chmod +x ~/bin/jq
```

## Основное использование
```bash
# Чтение поля:
jq '.field' file.json

# Фильтрация массива:
jq '.[] | select(.price > 100)' data.json

# Форматирование:
curl -s api.com | jq .
```

## Полезные примеры
```bash
# Суммирование значений:
jq '[.[].value] | add' data.json

# Группировка:
jq 'group_by(.category)' items.json

# Создание нового JSON:
jq '{name, age: (.dob | fromdate | now - . | ./31536000 | floor)}' users.json
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias jsonfmt='jq .'
export JQ_COLORS="1;33:0;39:0;39:0;39:0;32:1;39:1;39"
```

## Альтернативы
- yq (для YAML)
- fx
- jello (Python-аналог)

## Ссылки
- [Официальный репозиторий](https://github.com/stedolan/jq)
- [Интерактивный учебник](https://jqplay.org/)
