# -*- coding: utf-8 -*-
"""
批量更新所有电影详情页的收藏功能，添加localStorage持久化支持
"""
import os

# 需要处理的电影文件列表
movies = [
    ('movie_detail_shawshank.html', 'shawshank'),
    ('movie_detail_king_of_comedy.html', 'king_of_comedy'),
    ('movie_detail_seven.html', 'seven'),
    ('movie_detail_titanic.html', 'titanic'),
    ('movie_detail_green_book.html', 'green_book'),
    ('movie_detail_green_mile.html', 'green_mile'),
    ('movie_detail_interstellar.html', 'interstellar'),
    ('movie_detail_godfather.html', 'godfather'),
    ('movie_detail_amazing_spider_man.html', 'amazing_spider_man')
]

# 新的JavaScript代码模板
js_template = '''    <script>
        const MOVIE_ID = '{movie_id}';
        let isFavorited = false;
        
        function initFavorite() {{
            const saved = localStorage.getItem('favorite_' + MOVIE_ID);
            isFavorited = saved === 'true';
            
            const btn = document.querySelector('.favorite-btn');
            const text = document.querySelector('.favorite-text');
            
            if (isFavorited) {{
                btn.classList.add('favorited');
                text.textContent = '已收藏';
            }} else {{
                btn.classList.remove('favorited');
                text.textContent = '加入收藏';
            }}
        }}
        
        function toggleFavorite() {{
            isFavorited = !isFavorited;
            const btn = document.querySelector('.favorite-btn');
            const text = document.querySelector('.favorite-text');
            
            localStorage.setItem('favorite_' + MOVIE_ID, isFavorited);
            
            if (isFavorited) {{
                btn.classList.add('favorited');
                text.textContent = '已收藏';
                alert('已添加到收藏！');
            }} else {{
                btn.classList.remove('favorited');
                text.textContent = '加入收藏';
                alert('已取消收藏');
            }}
        }}
        
        document.addEventListener('DOMContentLoaded', initFavorite);
    </script>
</body>
</html>'''

# 旧的JavaScript代码模式
old_js_pattern = '''    <script>
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
    </script>
</body>
</html>'''

def update_file(filepath, movie_id):
    """更新单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换旧的JavaScript代码
        if old_js_pattern in content:
            content = content.replace(old_js_pattern, js_template.format(movie_id=movie_id))
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ 已更新: {filepath}")
            return True
        else:
            print(f"⚠️ 未找到旧代码: {filepath}")
            return False
            
    except Exception as e:
        print(f"✗ 处理 {filepath} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("开始批量更新电影详情页的收藏持久化功能...\n")
    
    success_count = 0
    for filename, movie_id in movies:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if os.path.exists(filepath):
            if update_file(filepath, movie_id):
                success_count += 1
        else:
            print(f"✗ 文件不存在: {filename}")
    
    print(f"\n完成！共更新了 {success_count}/{len(movies)} 个文件")

if __name__ == '__main__':
    main()
