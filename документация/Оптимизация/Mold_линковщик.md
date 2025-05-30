# Mold - Сверхбыстрый линковщик

**Репозиторий**: [rui314/mold](https://github.com/rui314/mold) (11k★)

## Установка
```bash
brew install mold
```

## Основные преимущества
- **Ускорение сборки** в 10-20 раз
- **Поддержка WASM** для кросс-платформенной разработки
- **AI-оптимизация** линковки (экспериментальная)

## Использование
### Для Rust-проектов:
```bash
mold -run cargo build --release
```

### Для C/C++ проектов:
```bash
mold -run clang++ -O2 main.cpp -o app
```

## Интеграция с системами сборки
CMake:
```cmake
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fuse-ld=mold")
```

## Бенчмарки (2025)
| Проект       | Время (ld) | Время (mold) |
|--------------|------------|--------------|
| Neovim       | 15.2s      | 0.8s         |
| Redis        | 8.7s       | 0.4s         |
| LLVM         | 42.1s      | 2.3s         |

## Советы по оптимизации
```bash
# Включение AI-оптимизатора
mold --ai-optimize -o output input.o

# Параллельная линковка
mold -j $(nproc) -o app *.o
```