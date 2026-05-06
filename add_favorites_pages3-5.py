# -*- coding: utf-8 -*-
"""
批量为第三、四、五页电影详情页添加收藏功能
"""
import os

# 需要处理的电影文件列表（第三、四、五页的电影）
movies = [
    # 第三页 (第21-30部)
    ('movie_detail_lion_king.html', 'lion_king'),
    ('movie_detail_saving_private_ryan.html', 'saving_private_ryan'),
    ('movie_detail_departed.html', 'departed'),
    ('movie_detail_whiplash.html', 'whiplash'),
    ('movie_detail_la_la_land.html', 'la_la_land'),
    ('movie_detail_intouchables.html', 'intouchables'),
    ('movie_detail_gone_girl.html', 'gone_girl'),
    ('movie_detail_mad_max.html', 'mad_max'),
    ('movie_detail_room.html', 'room'),
    ('movie_detail_big_short.html', 'big_short'),
    
    # 第四页 (第31-40部)
    ('movie_detail_brooklyn.html', 'brooklyn'),
    ('movie_detail_revenant.html', 'revenant'),
    ('movie_detail_spotlight.html', 'spotlight'),
    ('movie_detail_shape_of_water.html', 'shape_of_water'),
    ('movie_detail_three_billboards.html', 'three_billboards'),
    ('movie_detail_call_me_by_your_name.html', 'call_me_by_your_name'),
    ('movie_detail_dunkirk.html', 'dunkirk'),
    ('movie_detail_get_out.html', 'get_out'),
    ('movie_detail_a_star_is_born.html', 'a_star_is_born'),
    ('movie_detail_roma.html', 'roma'),
    
    # 第五页 (第41-45部)
    ('movie_detail_bohemian_rhapsody.html', 'bohemian_rhapsody'),
    ('movie_detail_joker.html', 'joker'),
    ('movie_detail_parasite.html', 'parasite'),
    ('movie_detail_avengers.html', 'avengers'),
    ('movie_detail_apes.html', 'apes'),
    ('movie_detail_legally_blonde.html', 'legally_blonde'),
    ('movie_detail_the_big_short.html', 'the_big_short'),
    ('movie_detail_comedy_king.html', 'comedy_king')
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
    print("开始批量为第三、四、五页电影详情页添加收藏功能...\n")
    
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
