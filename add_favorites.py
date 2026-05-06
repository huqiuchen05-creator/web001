#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为电影详情页面添加收藏功能
"""
import os
import re

# 需要处理的电影文件列表（第一页的9部电影）
movies_to_process = [
    'movie_detail_shawshank.html',       # 肖申克的救赎
    'movie_detail_king_of_comedy.html',  # 喜剧之王
    'movie_detail_seven.html',           # 七宗罪
    'movie_detail_titanic.html',         # 泰坦尼克号
    'movie_detail_green_book.html',      # 绿皮书
    'movie_detail_green_mile.html',      # 绿里奇迹
    'movie_detail_interstellar.html',    # 星际穿越
    'movie_detail_godfather.html',       # 教父1
    'movie_detail_amazing_spider_man.html' # 超凡蜘蛛侠
]

# CSS样式
css_to_add = '''        /* 收藏按钮 */
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
'''

# 按钮HTML
button_html = '''                <div class="movie-actions">
                    <button class="favorite-btn" onclick="toggleFavorite()">
                        <span class="favorite-icon">⭐</span>
                        <span class="favorite-text">加入收藏</span>
                    </button>
                </div>'''

# JavaScript代码
js_code = '''    <script>
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
    </script>'''

def add_favorite_to_file(file_path):
    """为单个文件添加收藏功能"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有收藏功能了
        if 'favorite-btn' in content:
            print(f'✓ {file_path} 已包含收藏功能，跳过')
            return True
        
        original_content = content
        
        # 1. 添加CSS样式
        # 找到 .back-btn:hover 后面
        css_pattern = re.compile(r'(\.back-btn:hover\s*\{\s*[^\}]*\s*\})', re.DOTALL)
        match = css_pattern.search(content)
        if match:
            content = content.replace(match.group(1), match.group(1) + '\n' + css_to_add)
        
        # 2. 在剧情简介后面添加按钮
        # 找到 </div> 结束标签（在剧情简介后面）
        # 先找到剧情简介部分的位置
        synopsis_end_pattern = re.compile(r'(</div>\s*)\s*(</div>\s*)\s*(</div>\s*)\s*(<!-- 视频图片模块 -->)', re.DOTALL)
        match = synopsis_end_pattern.search(content)
        if match:
            # 在第三个 </div> 后面插入按钮
            before = content[:match.start(4)]
            after = content[match.start(4):]
            # 找到剧情简介结束的位置
            # 更精确的方法：找到最后一个剧情简介的段落后面
            synopsis_part_pattern = re.compile(r'(</div>\s*)\s*(</div>\s*)\s*(</div>\s*)', re.DOTALL)
            synopsis_match = synopsis_part_pattern.search(before)
            if synopsis_match:
                insert_pos = synopsis_match.start(3)
                before = before[:insert_pos] + button_html + '\n' + before[insert_pos:]
                content = before + after
        
        # 3. 在 </body> 前添加JavaScript
        if '<script>' not in content:
            body_end_pattern = re.compile(r'(</div>\s*)\s*(</body>\s*)\s*(</html>)', re.DOTALL)
            match = body_end_pattern.search(content)
            if match:
                insert_pos = match.start(2)
                content = content[:insert_pos] + '\n' + js_code + '\n' + content[insert_pos:]
        
        # 保存文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'✓ 已成功为 {file_path} 添加收藏功能')
            return True
        else:
            print(f'✗ {file_path} 没有找到合适的位置插入内容')
            return False
            
    except Exception as e:
        print(f'✗ 处理 {file_path} 时出错: {e}')
        return False

def main():
    """主函数"""
    print('开始批量添加收藏功能...\n')
    
    success_count = 0
    for movie_file in movies_to_process:
        file_path = os.path.join(os.path.dirname(__file__), movie_file)
        if os.path.exists(file_path):
            if add_favorite_to_file(file_path):
                success_count += 1
        else:
            print(f'✗ 文件不存在: {movie_file}')
    
    print(f'\n完成！共处理了 {success_count}/{len(movies_to_process)} 个文件')

if __name__ == '__main__':
    main()
