import os
import requests
from pathlib import Path

def create_md_from_url(url, task, category):
    # Get content from URL
    response = requests.get(url)
    content = response.text
    
    # Create filename from task
    filename = f"{task.replace(' ', '_')}.md"
    
    # Determine target directory
    categories = {
        'терминал': '1_Терминалы',
        'редактор': '2_Редакторы', 
        'ai': '3_AI_Инструменты',
        'оптимизация': '4_Оптимизация',
        'плагин': '5_Плагины'
    }
    
    target_dir = categories.get(category.lower(), '')
    if not target_dir:
        return "Неизвестная категория"
    
    # Create MD file
    filepath = os.path.join(target_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {task}\n\n")
        f.write(f"## Источник: {url}\n\n")
        f.write(content)
    
    return f"Файл создан: {filepath}"

if __name__ == '__main__':
    url = input("Введите URL: ")
    task = input("Введите задачу: ")
    category = input("Введите категорию (терминал/редактор/ai/оптимизация/плагин): ")
    print(create_md_from_url(url, task, category))