const moviesData = {
    f1: {
        id: 'f1',
        title: 'F1：狂飙飞车',
        year: '2025',
        rating: '5.0',
        genres: ['动作', '冒险', '运动'],
        poster: 'C:\\Users\\19256\\Desktop\\设艺\\作业\\用户体验设计\\网页\\素材\\p2921935298.webp'
    },
    fast_furious: {
        id: 'fast_furious',
        title: '速度与激情10',
        year: '2023',
        rating: '9.2',
        genres: ['动作', '犯罪', '冒险'],
        poster: 'picture/aa/A.webp'
    },
    blade_runner: {
        id: 'blade_runner',
        title: '银翼杀手2049',
        year: '2017',
        rating: '8.7',
        genres: ['科幻', '惊悚', '悬疑'],
        poster: 'picture/bb/B.webp'
    },
    shawshank: {
        id: 'shawshank',
        title: '肖申克的救赎',
        year: '1994',
        rating: '9.0',
        genres: ['剧情', '犯罪'],
        poster: 'picture/cc/C.webp'
    },
    king_of_comedy: {
        id: 'king_of_comedy',
        title: '喜剧之王',
        year: '1999',
        rating: '8.5',
        genres: ['喜剧', '剧情', '爱情'],
        poster: 'picture/dd/D.webp'
    },
    seven: {
        id: 'seven',
        title: '七宗罪',
        year: '1995',
        rating: '8.8',
        genres: ['惊悚', '犯罪', '悬疑'],
        poster: 'picture/ee/E.webp'
    },
    titanic: {
        id: 'titanic',
        title: '泰坦尼克号',
        year: '1997',
        rating: '9.3',
        genres: ['爱情', '剧情', '灾难'],
        poster: 'picture/ff/F.webp'
    },
    green_book: {
        id: 'green_book',
        title: '绿皮书',
        year: '2018',
        rating: '9.5',
        genres: ['友情', '剧情'],
        poster: 'picture/gg/G.webp'
    },
    green_mile: {
        id: 'green_mile',
        title: '绿里奇迹',
        year: '1999',
        rating: '8.9',
        genres: ['剧情', '犯罪'],
        poster: 'picture/hh/H.webp'
    },
    interstellar: {
        id: 'interstellar',
        title: '星际穿越',
        year: '2014',
        rating: '9.4',
        genres: ['科幻', '冒险'],
        poster: 'picture/ii/I.webp'
    },
    godfather: {
        id: 'godfather',
        title: '教父',
        year: '1972',
        rating: '9.2',
        genres: ['犯罪', '剧情'],
        poster: 'picture/jj/J.webp'
    },
    amazing_spider_man: {
        id: 'amazing_spider_man',
        title: '超凡蜘蛛侠',
        year: '2012',
        rating: '8.1',
        genres: ['超能力', '动作', '科幻'],
        poster: 'picture/kk/K.webp'
    },
    iron_man: {
        id: 'iron_man',
        title: '钢铁侠',
        year: '2008',
        rating: '8.5',
        genres: ['超能力', '超级英雄', '科幻'],
        poster: 'picture/ll/L.webp'
    },
    inception: {
        id: 'inception',
        title: '盗梦空间',
        year: '2010',
        rating: '9.3',
        genres: ['科幻', '悬疑', '动作'],
        poster: 'picture/pp/P.webp'
    },
    wall_e: {
        id: 'wall_e',
        title: '机器人总动员',
        year: '2008',
        rating: '9.3',
        genres: ['科幻', '动画', '喜剧'],
        poster: 'picture/qq/Q.webp'
    },
    truman: {
        id: 'truman',
        title: '楚门的世界',
        year: '1998',
        rating: '9.3',
        genres: ['喜剧', '剧情', '科幻'],
        poster: 'picture/rr/R.webp'
    },
    catch_me: {
        id: 'catch_me',
        title: '猫鼠游戏',
        year: '2002',
        rating: '9.0',
        genres: ['犯罪', '剧情', '传记'],
        poster: 'picture/ss/S.webp'
    },
    flipped: {
        id: 'flipped',
        title: '怦然心动',
        year: '2010',
        rating: '9.1',
        genres: ['爱情', '友情', '青春'],
        poster: 'picture/tt/T.webp'
    },
    forrest_gump: {
        id: 'forrest_gump',
        title: '阿甘正传',
        year: '1994',
        rating: '9.5',
        genres: ['剧情', '爱情', '传记'],
        poster: 'picture/uu/U.webp'
    },
    dark_knight: {
        id: 'dark_knight',
        title: '蝙蝠侠：黑暗骑士',
        year: '2008',
        rating: '9.4',
        genres: ['动作', '超级英雄', '犯罪'],
        poster: 'picture/vv/V.webp'
    },
    pulp_fiction: {
        id: 'pulp_fiction',
        title: '低俗小说',
        year: '1994',
        rating: '9.1',
        genres: ['犯罪', '剧情', '黑色幽默'],
        poster: 'picture/ww/W.webp'
    },
    gladiator: {
        id: 'gladiator',
        title: '角斗士',
        year: '2000',
        rating: '9.1',
        genres: ['动作', '历史', '剧情'],
        poster: 'picture/xx/X.webp'
    },
    matrix: {
        id: 'matrix',
        title: '黑客帝国',
        year: '1999',
        rating: '9.1',
        genres: ['科幻', '动作', '悬疑'],
        poster: 'picture/yy/Y.webp'
    },
    schindlers_list: {
        id: 'schindlers_list',
        title: '辛德勒的名单',
        year: '1993',
        rating: '9.5',
        genres: ['剧情', '历史', '传记'],
        poster: 'picture/zz/Z.webp'
    },
    goodfellas: {
        id: 'goodfellas',
        title: '好家伙',
        year: '1990',
        rating: '9.0',
        genres: ['犯罪', '剧情', '传记'],
        poster: 'picture/zz1/Z1.webp'
    },
    lion_king: {
        id: 'lion_king',
        title: '狮子王',
        year: '1994',
        rating: '9.1',
        genres: ['动画', '家庭', '冒险'],
        poster: 'picture/zz2/Z2.webp'
    },
    saving_private_ryan: {
        id: 'saving_private_ryan',
        title: '拯救大兵瑞恩',
        year: '1998',
        rating: '9.0',
        genres: ['战争', '剧情', '动作'],
        poster: 'picture/zz3/Z3.webp'
    },
    departed: {
        id: 'departed',
        title: '无间道风云',
        year: '2006',
        rating: '8.9',
        genres: ['犯罪', '惊悚', '剧情'],
        poster: 'picture/zz4/Z4.webp'
    },
    whiplash: {
        id: 'whiplash',
        title: '爆裂鼓手',
        year: '2014',
        rating: '8.7',
        genres: ['剧情', '音乐', '励志'],
        poster: 'picture/zz5/Z5.webp'
    },
    la_la_land: {
        id: 'la_la_land',
        title: '爱乐之城',
        year: '2016',
        rating: '8.9',
        genres: ['爱情', '音乐', '剧情'],
        poster: 'picture/zz6/Z6.webp'
    },
    intouchables: {
        id: 'intouchables',
        title: '触不可及',
        year: '2011',
        rating: '9.2',
        genres: ['喜剧', '剧情', '友情'],
        poster: 'picture/zz7/Z7.webp'
    },
    gone_girl: {
        id: 'gone_girl',
        title: '消失的爱人',
        year: '2014',
        rating: '8.7',
        genres: ['惊悚', '悬疑', '剧情'],
        poster: 'picture/zz8/Z8.webp'
    },
    mad_max: {
        id: 'mad_max',
        title: '疯狂的麦克斯',
        year: '2015',
        rating: '8.6',
        genres: ['动作', '科幻', '冒险'],
        poster: 'picture/zz9/Z9.webp'
    },
    room: {
        id: 'room',
        title: '十二怒汉',
        year: '1957',
        rating: '9.4',
        genres: ['剧情'],
        poster: 'picture/zz10/Z10.webp'
    },
    big_short: {
        id: 'big_short',
        title: '控方证人',
        year: '1957',
        rating: '9.6',
        genres: ['剧情', '悬疑'],
        poster: 'picture/zz11/Z11.webp'
    },
    brooklyn: {
        id: 'brooklyn',
        title: '布鲁克林',
        year: '2015',
        rating: '8.3',
        genres: ['剧情', '爱情', '移民'],
        poster: 'picture/zz12/Z12.webp'
    },
    revenant: {
        id: 'revenant',
        title: '荒野猎人',
        year: '2015',
        rating: '8.6',
        genres: ['动作', '冒险', '剧情'],
        poster: 'picture/zz13/Z13.webp'
    },
    spotlight: {
        id: 'spotlight',
        title: '死亡诗社',
        year: '1989',
        rating: '8.9',
        genres: ['剧情'],
        poster: 'picture/zz14/Z14.webp'
    },
    shape_of_water: {
        id: 'shape_of_water',
        title: '水形物语',
        year: '2017',
        rating: '8.3',
        genres: ['奇幻', '爱情', '剧情'],
        poster: 'picture/zz15/Z15.webp'
    },
    three_billboards: {
        id: 'three_billboards',
        title: '三块广告牌',
        year: '2017',
        rating: '8.7',
        genres: ['剧情', '犯罪', '黑色幽默'],
        poster: 'picture/zz16/Z16.webp'
    },
    call_me_by_your_name: {
        id: 'call_me_by_your_name',
        title: '飞越疯人院',
        year: '1975',
        rating: '9.1',
        genres: ['剧情'],
        poster: 'picture/zz17/Z17.webp'
    },
    dunkirk: {
        id: 'dunkirk',
        title: '敦刻尔克',
        year: '2017',
        rating: '8.4',
        genres: ['战争', '动作', '历史'],
        poster: 'picture/zz18/Z18.webp'
    },
    get_out: {
        id: 'get_out',
        title: '逃出绝命镇',
        year: '2017',
        rating: '7.8',
        genres: ['恐怖', '惊悚', '悬疑'],
        poster: 'picture/zz19/Z19.webp'
    },
    a_star_is_born: {
        id: 'a_star_is_born',
        title: '一个明星的诞生',
        year: '2018',
        rating: '8.2',
        genres: ['音乐', '爱情', '剧情'],
        poster: 'picture/zz20/Z20.webp'
    },
    roma: {
        id: 'roma',
        title: '罗马',
        year: '2018',
        rating: '8.2',
        genres: ['剧情', '家庭', '传记'],
        poster: 'picture/zz21/Z21.webp'
    },
    bohemian_rhapsody: {
        id: 'bohemian_rhapsody',
        title: '波西米亚狂想曲',
        year: '2018',
        rating: '8.6',
        genres: ['传记', '音乐', '剧情'],
        poster: 'picture/zz22/Z22.webp'
    },
    joker: {
        id: 'joker',
        title: '小丑',
        year: '2019',
        rating: '8.7',
        genres: ['剧情', '惊悚', '犯罪'],
        poster: 'picture/zz23/Z23.webp'
    },
    parasite: {
        id: 'parasite',
        title: '寄生虫',
        year: '2019',
        rating: '9.0',
        genres: ['剧情', '惊悚', '黑色幽默'],
        poster: 'picture/zz24/Z24.webp'
    },
    avengers: {
        id: 'avengers',
        title: '复仇者联盟',
        year: '2012',
        rating: '8.8',
        genres: ['科幻', '超级英雄', '动作'],
        poster: 'picture/oo/O.webp'
    },
    apes: {
        id: 'apes',
        title: '猩球崛起',
        year: '2011',
        rating: '8.1',
        genres: ['科幻', '剧情'],
        poster: 'picture/nn/N.webp'
    },
    legally_blonde: {
        id: 'legally_blonde',
        title: '政律俏佳人',
        year: '2001',
        rating: '7.6',
        genres: ['喜剧', '剧情', '爱情'],
        poster: 'picture/mm/M.webp'
    },
    the_big_short: {
        id: 'the_big_short',
        title: '大空头',
        year: '2015',
        rating: '8.5',
        genres: ['剧情', '金融'],
        poster: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=big%20short%20movie%20poster%2C%20wall%20street%2C%20finance&image_size=portrait_4_3'
    },
    comedy_king: {
        id: 'comedy_king',
        title: '喜剧之王',
        year: '1999',
        rating: '8.8',
        genres: ['喜剧', '剧情', '爱情'],
        poster: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=king%20of%20comedy%20stephen%20king%20movie%20poster%2C%20dark%20comedy&image_size=portrait_4_3'
    }
};

function getFavoriteMovies() {
    const favorites = [];
    for (let key in moviesData) {
        const saved = localStorage.getItem('favorite_' + key);
        if (saved === 'true') {
            favorites.push(moviesData[key]);
        }
    }
    return favorites;
}

function isMovieFavorited(movieId) {
    return localStorage.getItem('favorite_' + movieId) === 'true';
}

function toggleFavorite(movieId) {
    const isFavorited = localStorage.getItem('favorite_' + movieId) === 'true';
    localStorage.setItem('favorite_' + movieId, !isFavorited);
    return !isFavorited;
}
