# yq (jq для YAML)

![Лого](https://raw.githubusercontent.com/mikefarah/yq/master/logo.png)

## Описание
Мощный инструмент для работы с YAML/JSON/XML:
- Конвертация между форматами
- Поддержка синтаксиса jq
- Редактирование на лету
- Поддержка потоковой обработки

## Установка
```bash
# Через Homebrew:
brew install yq

# Через pip:
pip install yq

# Вручную:
wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/local/bin/yq && chmod +x /usr/local/bin/yq
```

## Основное использование
```bash
# Чтение значения:
yq '.key.path' file.yaml

# Редактирование:
yq -i '.image.tag = "latest"' k8s.yaml

# Конвертация в JSON:
yq -o=json file.yaml
```

## Полезные примеры
```bash
# Обновление массива:
yq -i '.services += ["nginx"]' docker-compose.yml

# Извлечение секретов:
yq '.secrets[] | select(.type == "password")' config.yaml

# Слияние файлов:
yq eval-all 'select(fileIndex == 0) * select(fileIndex == 1)' file1.yaml file2.yaml
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias yaml2json='yq -o=json'
alias json2yaml='yq -P'
```

## Альтернативы
- jq (только JSON)
- dasel
- yaml-cli

## Ссылки
- [Официальный репозиторий](https://github.com/mikefarah/yq)
- [Документация](https://mikefarah.gitbook.io/yq/)
