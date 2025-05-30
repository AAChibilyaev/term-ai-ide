# Ollama - Локальные LLM модели

**Репозиторий**: [jmorganca/ollama](https://github.com/jmorganca/ollama) (12k★)

## Установка
```bash
brew install ollama
```

## Основные команды
| Команда | Описание |
|---------|----------|
| `ollama pull llama3` | Скачать модель |
| `ollama list` | Показать установленные модели |
| `ollama run llama3` | Запустить чат с моделью |

## Интеграция с редакторами
### Для Neovim:
```lua
require('ollama').setup({
  model = "llama3",
  temperature = 0.7
})
```

### Для Helix:
Добавьте в `config.toml`:
```toml
[language-server.ollama]
command = "ollama"
args = ["run", "llama3"]
```

## Примеры использования
1. Оптимизация кода:
```bash
cat main.py | ollama run llama3 "Оптимизируй этот код"
```

2. Генерация документации:
```bash
ollama run llama3 "Напиши README для Go-проекта" > README.md
```

3. Поиск уязвимостей:
```bash
ollama run llama3 "Найди уязвимости в этом Dockerfile" < Dockerfile
```