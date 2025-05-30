# Telescope-AI - NLP-поиск кода

**Репозиторий**: [rockerBOO/telescope-ai](https://github.com/rockerBOO/telescope-ai) (3.4k★)

## Установка (для Neovim)
```lua
use {
  'rockerBOO/telescope-ai',
  requires = { 'nvim-telescope/telescope.nvim' },
  config = function()
    require('telescope').load_extension('ai')
  end
}
```

## Ключевые возможности
- **Поиск по смыслу** вместо точных совпадений
- **Контекстное понимание** кода
- **Поддержка 20+ языков** программирования

## Примеры использования
### Базовый поиск:
```vim
:Telescope ai grep="найди обработку ошибок"
```

### Поиск с фильтрами:
```vim
:Telescope ai grep="покажи все SQL-запросы" lang=python
```

### Интерактивный режим:
```vim
:Telescope ai interactive
```
(Затем введите запрос в появившемся prompt)

## Конфигурация
```lua
require('telescope').setup {
  extensions = {
    ai = {
      model = "gpt-4o",  -- Также поддерживает локальные модели
      temperature = 0.3,
      max_tokens = 1000
    }
  }
}
```

## Интеграция с другими инструментами
1. С Copilot.nvim:
```lua
-- Автодополнение на основе найденного кода
vim.keymap.set('n', '<leader>ca', ':Telescope ai complete<CR>')
```

2. С LSP:
```lua
-- Поиск по документации LSP
:Telescope ai lsp_documentation
```