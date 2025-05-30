# Documentation Structure

This is the root directory for markdown documentation.

## Русская структура документации

Основная документация теперь организована в папке `документация`:

```
документация/
├── Терминалы/       # Warp, WezTerm, Zellij
├── Редакторы/       # Helix, Neovim  
├── ИИ_Инструменты/  # Tabby, Continue, Ollama
├── Оптимизация/     # Bun, Mold, eBPF
├── Shell_Утилиты/   # bat, exa, ripgrep
└── Плагины/         # Плагины для терминалов
```

## Английская структура (legacy)
- `/guides` - Tutorials and how-to guides
- `/reference` - API reference
- `/examples` - Code snippets
- `/images` - Assets
- `/templates` - Style guides

## Basic Usage
1. Place new markdown files in appropriate subdirectories
2. Use relative links between documents
3. Follow the style guide in `/templates/style-guide.md`