# Helix - Редактор на Rust

**Репозиторий**: [helix-editor/helix](https://github.com/helix-editor/helix) (27k★)

## Установка
```bash
brew install helix
```

## Ключевые особенности 2025
- **Встроенный tree-sitter** для подсветки синтаксиса
- **LSP-поддержка** из коробки
- **AI-интеграция** через отдельный LSP

## Настройка AI
1. Установите AI-LSP:
```bash
brew install helix-ai-lsp
```

2. Добавьте в конфиг (`~/.config/helix/config.toml`):
```toml
[language-server]
python = { command = "ai-lsp", args = ["--model", "llama3"] }
```

## Горячие клавиши
| Комбинация | Действие |
|------------|----------|
| `Space + A` | Вызов AI-ассистента |
| `Ctrl + P` | AI-дополнение кода |
| `;g` | Генерация тестов |

## Пример использования
```bash
hx --ai "Добавь обработку ошибок" main.rs
```