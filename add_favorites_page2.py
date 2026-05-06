# -*- coding: utf-8 -*-
"""
批量为第二页电影详情页添加收藏功能
"""
import os

# 需要处理的电影文件列表（第二页的12部电影）
movies = [
    ('movie_detail_wall_e.html', 'wall_e'),
    ('movie_detail_truman.html', 'truman'),
    ('movie_detail_catch_me.html', 'catch_me'),
    ('movie_detail_flipped.html', 'flipped'),
    ('movie_detail_forrest_gump.html', 'forrest_gump'),
    ('movie_detail_dark_knight.html', 'dark_knight'),
    ('movie_detail_pulp_fiction.html', 'pulp_fiction'),
    ('movie_detail_gladiator.html', 'gladiator'),
    ('movie_detail_matrix.html', 'matrix'),
    ('movie_detail_schindlers_list.html', 'schindlers_list'),
    ('movie_detail_goodfellas.html', 'goodfellas')
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
    </script>'''

def process_file(filepath, movie_id):
    """处理单个电影文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有收藏功能
        if 'favorite-btn' in content:
            print(f"✓ {filepath} 已包含收藏功能，跳过")
            return True
        
        # 1. 添加CSS样式
        content = content.replace(
            '.back-btn:hover {\n            background-color: #00ffaa;\n            color: #000;\n        }\n    </style>',
            '.back-btn:hover {\n            background-color: #00ffaa;\n            color: #000;\n        }\n' + css_to_add + '    </style>'
        )
        
        # 2. 在剧情简介后面添加按钮
        content = content.replace(
            '</div>\n            </div>\n        </div>\n        <!-- 视频图片模块 -->',
            button_html + '\n            </div>\n        </div>\n        <!-- 视频图片模块 -->'
        )
        
        # 3. 添加JavaScript
        content = content.replace(
            '</body>\n</html>',
            js_code.format(movie_id=movie_id) + '\n</body>\n</html>'
        )
        
        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ 已处理: {filepath}")
        return True
        
    except Exception as e:
        print(f"✗ 处理 {filepath} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("开始批量为第二页电影详情页添加收藏功能...\n")
    
    success_count = 0
    for filename, movie_id in movies:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if os.path.exists(filepath):
            if process_file(filepath, movie_id):
                success_count += 1
        else:
            print(f"✗ 文件不存在: {filename}")
    
    print(f"\n完成！共处理了 {success_count}/{len(movies)} 个文件")

if __name__ == '__main__':
    main()
