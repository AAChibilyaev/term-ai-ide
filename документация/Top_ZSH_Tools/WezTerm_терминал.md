# WezTerm - GPU-ускоренный терминал

**Репозиторий**: [wez/wezterm](https://github.com/wez/wezterm) (24k★)

## Установка (MacOS)
```bash
brew install --cask wezterm
```

## Ключевые фичи 2025
- **Рендеринг через Metal API** (120 FPS)
- **Lua-конфигурация**:
  ```lua
  return {
    enable_wayland = true,
    color_scheme = "Ayu Dark",
    default_prog = { "zellij", "attach", "-c" }
  }
  ```

## AI-интеграция
Добавьте чат-ассистента в статус-бар:
```lua
wezterm.on("update-status", function(window)
  window:set_right_status("🤖 " .. os.date("%H:%M"))
end)
```