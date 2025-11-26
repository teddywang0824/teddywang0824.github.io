import os
import random
import datetime

CONTENT_DIR = 'content'
CATEGORIES = ['Inspiration', 'Programming']
TITLES_INSPIRATION = [
    "午後的咖啡時光", "閱讀的一百種方式", "關於旅行的意義", 
    "城市角落的微光", "雨天的隨想", "書寫的溫度",
    "尋找生活的縫隙", "慢活的藝術", "清晨的思緒", "夜讀偶得"
]
TITLES_PROGRAMMING = [
    "Python 學習筆記", "React Hooks 實戰", "演算法初探",
    "Clean Code 心得", "Docker 部署教學", "Git 版本控制技巧",
    "VS Code 必備套件", "Web Performance 優化", "API 設計原則", "Linux 常用指令"
]

def create_dummy_posts():
    if not os.path.exists(CONTENT_DIR):
        os.makedirs(CONTENT_DIR)

    # Create 15 posts
    for i in range(15):
        category = random.choice(CATEGORIES)
        if category == 'Inspiration':
            title = random.choice(TITLES_INSPIRATION) + f" #{i+1}"
            tags = "life, reading, thoughts"
        else:
            title = random.choice(TITLES_PROGRAMMING) + f" #{i+1}"
            tags = "tech, code, learning"
        
        date = datetime.datetime.now() - datetime.timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d %H:%M")
        slug = f"post-{i+1}"
        
        content = f"""Title: {title}
Date: {date_str}
Category: {category}
Tags: {tags}
Slug: {slug}
Authors: User
Summary: 這是一篇關於 {title} 的測試文章摘要。這裡會顯示文章的前幾行內容，讓讀者快速了解文章的主題。

# {title}

這是一篇自動生成的測試文章。

## 內容章節

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

### 子標題

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""
        filename = os.path.join(CONTENT_DIR, f"dummy_post_{i+1}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {filename}")

if __name__ == "__main__":
    create_dummy_posts()
