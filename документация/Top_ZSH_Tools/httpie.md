# httpie (современный curl)

![Демо](https://raw.githubusercontent.com/httpie/httpie/master/docs/httpie-animation.gif)

## Описание
Удобный HTTP-клиент для командной строки с:
- Цветным выводом
- Поддержкой JSON
- Автодополнением
- Простым синтаксисом

## Установка
```bash
# Через Homebrew:
brew install httpie

# Через pip:
pip install httpie

# Через apt (Ubuntu/Debian):
sudo apt install httpie
```

## Основное использование
```bash
# GET запрос:
http GET example.com

# POST с JSON:
http POST example.com name=John age:=30

# С заголовками:
http example.com User-Agent:X-My-App
```

## Полезные примеры
```bash
# Сохранение cookies:
http --session=user example.com/login username=foo password=bar

# Загрузка файла:
http -d example.com/file @localfile.txt

# Отладка:
http -v example.com
```

## Интеграция с Zsh
Добавить алиасы в ~/.zshrc:
```bash
alias https='http --default-scheme=https'
export HTTPIE_CONFIG_DIR="$HOME/.config/httpie"
```

## Альтернативы
- curl
- wget
- httpx

## Ссылки
- [Официальный репозиторий](https://github.com/httpie/httpie)
- [Документация](https://httpie.io/docs/cli)
