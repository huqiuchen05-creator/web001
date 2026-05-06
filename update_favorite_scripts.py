# -*- coding: utf-8 -*-
"""
批量更新电影详情页的收藏脚本，添加storage事件监听
"""
import os

movies = [
    'fast_furious', 'blade_runner', 'shawshank', 'king_of_comedy', 'seven',
    'titanic', 'green_book', 'green_mile', 'interstellar', 'godfather',
    'amazing_spider_man', 'iron_man', 'inception', 'wall_e', 'truman',
    'catch_me', 'flipped', 'forrest_gump', 'dark_knight', 'pulp_fiction',
    'gladiator', 'matrix', 'schindlers_list', 'goodfellas', 'lion_king',
    'saving_private_ryan', 'departed', 'whiplash', 'la_la_land', 'intouchables',
    'gone_girl', 'mad_max', 'room', 'big_short', 'brooklyn', 'revenant',
    'spotlight', 'shape_of_water', 'three_billboards', 'call_me_by_your_name',
    'dunkirk', 'get_out', 'a_star_is_born', 'roma', 'bohemian_rhapsody',
    'joker', 'parasite', 'avengers', 'apes', 'legally_blonde', 'the_big_short',
    'comedy_king'
]

old_script = '''    <script>
        const MOVIE_ID = '{movie_id}';
        let isFavorited = false;
        
        function initFavorite() {
            const saved = localStorage.getItem('favorite_' + MOVIE_ID);
            isFavorited = saved === 'true';
            
            const btn = document.querySelector('.favorite-btn');
            const text = document.querySelector('.favorite-text');
            
            if (isFavorited) {
                btn.classList.add('favorited');
                text.textContent = '已收藏';
            } else {
                btn.classList.remove('favorited');
                text.textContent = '加入收藏';
            }
        }
        
        function toggleFavorite() {
            isFavorited = !isFavorited;
            const btn = document.querySelector('.favorite-btn');
            const text = document.querySelector('.favorite-text');
            
            localStorage.setItem('favorite_' + MOVIE_ID, isFavorited);
            
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
        
        document.addEventListener('DOMContentLoaded', initFavorite);
    </script>'''

new_script = '''    <script>
        const MOVIE_ID = '{movie_id}';
        let isFavorited = false;
        
        function initFavorite() {
            const saved = localStorage.getItem('favorite_' + MOVIE_ID);
            isFavorited = saved === 'true';
            
            const btn = document.querySelector('.favorite-btn');
            const text = document.querySelector('.favorite-text');
            
            if (isFavorited) {
                btn.classList.add('favorited');
                text.textContent = '已收藏';
            } else {
                btn.classList.remove('favorited');
                text.textContent = '加入收藏';
            }
        }
        
        function toggleFavorite() {
            isFavorited = !isFavorited;
            const btn = document.querySelector('.favorite-btn');
            const text = document.querySelector('.favorite-text');
            
            localStorage.setItem('favorite_' + MOVIE_ID, isFavorited);
            
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
        
        function syncFavoriteStatus() {
            const saved = localStorage.getItem('favorite_' + MOVIE_ID);
            const currentStatus = saved === 'true';
            
            if (currentStatus !== isFavorited) {
                isFavorited = currentStatus;
                const btn = document.querySelector('.favorite-btn');
                const text = document.querySelector('.favorite-text');
                
                if (isFavorited) {
                    btn.classList.add('favorited');
                    text.textContent = '已收藏';
                } else {
                    btn.classList.remove('favorited');
                    text.textContent = '加入收藏';
                }
            }
        }
        
        document.addEventListener('DOMContentLoaded', initFavorite);
        window.addEventListener('storage', syncFavoriteStatus);
    </script>'''

def update_file(movie_id):
    filepath = f"movie_detail_{movie_id}.html"
    if not os.path.exists(filepath):
        print(f"✗ 文件不存在: {filepath}")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_script.format(movie_id=movie_id) in content:
            content = content.replace(old_script.format(movie_id=movie_id), new_script.format(movie_id=movie_id))
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ 已更新: {filepath}")
            return True
        else:
            print(f"✓ {filepath} 已包含最新脚本")
            return True
    except Exception as e:
        print(f"✗ 更新 {filepath} 时出错: {e}")
        return False

def main():
    print("开始更新电影详情页的收藏脚本...\n")
    
    success_count = 0
    for movie_id in movies:
        if update_file(movie_id):
            success_count += 1
    
    print(f"\n完成！共更新了 {success_count}/{len(movies)} 个文件")

if __name__ == '__main__':
    main()
