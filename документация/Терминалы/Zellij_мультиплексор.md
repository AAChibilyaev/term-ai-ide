# Zellij - Мультиплексор нового поколения

**Репозиторий**: [zellij-org/zellij](https://github.com/zellij-org/zellij) (15k★)

## Установка
```bash
brew install zellij
zellij setup --generate-completion zsh
```

## Основные возможности 2025
- **WASM-плагины** на Rust
- **AI-ассистент** в статус-баре
- **Автоматическая** оптимизация layout

## Конфигурация
Создайте файл `~/.config/zellij/config.kdl`:
```kdl
plugins {
  path "~/.config/zellij/plugins/ai.wasm"
}

keybinds {
  bind "Ctrl+g" { SwitchToMode "locked"; }
}
```

## Работа с сессиями
```bash
# Создать сессию с AI-плагином
zellij --layout ai

# Прикрепиться к существующей сессии
zellij attach -c
```