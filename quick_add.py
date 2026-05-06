# -*- coding: utf-8 -*-
"""
快速添加收藏功能到电影详情页面
"""
import os

# 定义要添加的内容
CSS = """        /* 收藏按钮 */
        .favorite-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: rgba(0, 255, 170, 0.2);
            color: #00ffaa;
            border: 1px solid #00ffaa;
            padding: 12px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .favorite-btn:hover {
            background-color: #00ffaa;
            color: #000;
            transform: scale(1.05);
        }
        
        .favorite-btn.favorited {
            background-color: #00ffaa;
            color: #000;
        }
        
        .movie-actions {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }
"""

BUTTON = """                <div class="movie-actions">
                    <button class="favorite-btn" onclick="toggleFavorite()">
                        <span class="favorite-icon">⭐</span>
                        <span class="favorite-text">加入收藏</span>
                    </button>
                </div>"""

JS = """    <script>
        let isFavorited = false;
        
        function toggleFavorite() {
            isFavorited = !isFavorited;
            const btn = document.querySelector('.favorite-btn');
            const text = document.querySelector('.favorite-text');
            
            if (isFavorited) {
                btn.classList.add('favorited');
                text.textContent = '已收藏';
                alert('已添加到收藏！');
            } else {
                btn.classList.remove('favorited');
                text.textContent = '加入收藏';
                alert('已取消收藏');
            }
        }
    </script>"""

# 需要处理的文件列表
files = [
    'movie_detail_shawshank.html',
    'movie_detail_king_of_comedy.html', 
    'movie_detail_seven.html',
    'movie_detail_titanic.html',
    'movie_detail_green_book.html',
    'movie_detail_green_mile.html',
    'movie_detail_interstellar.html',
    'movie_detail_godfather.html',
    'movie_detail_amazing_spider_man.html'
]

def process_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    if not os.path.exists(filepath):
        print(f"❌ 文件不存在: {filename}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经处理过
    if 'favorite-btn' in content:
        print(f"✓ {filename} 已处理，跳过")
        return True
    
    original = content
    
    # 1. 添加CSS
    content = content.replace(
        '.back-btn:hover {\n            background-color: #00ffaa;\n            color: #000;\n        }\n    </style>',
        '.back-btn:hover {\n            background-color: #00ffaa;\n            color: #000;\n        }\n' + CSS + '    </style>'
    )
    
    # 2. 找到剧情简介结束的位置，添加按钮
    # 找到剧情简介结束的模式
    lines = content.split('\n')
    synopsis_end_idx = -1
    button_inserted = False
    
    for i, line in enumerate(lines):
        if '剧情简介' in line:
            # 找到这个剧情简介区域结束的位置
            for j in range(i, min(i + 100, len(lines))):
                if '</div>' in lines[j] and '</div>' in lines[j+1]:
                    synopsis_end_idx = j
                    break
    
    if synopsis_end_idx != -1:
        # 在找到的位置后面插入按钮
        lines.insert(synopsis_end_idx + 1, BUTTON)
        button_inserted = True
    
    if button_inserted:
        content = '\n'.join(lines)
    
    # 3. 添加JS在</body>前
    content = content.replace('</body>', JS + '\n</body>')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ 已处理: {filename}")
        return True
    else:
        print(f"⚠️ 无法处理: {filename}")
        return False

if __name__ == '__main__':
    print("开始批量添加收藏功能...\n")
    count = 0
    for f in files:
        if process_file(f):
            count += 1
    print(f"\n完成！共处理了 {count}/{len(files)} 个文件")
