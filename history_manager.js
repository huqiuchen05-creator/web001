// 历史记录管理模块
const HistoryManager = (function() {
    const STORAGE_KEY = 'movie_history';
    const MAX_RECORDS = 50;
    
    // 获取历史记录
    function getHistory() {
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            return [];
        }
    }
    
    // 保存历史记录
    function saveHistory(history) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
    }
    
    // 添加观看记录
    function addHistory(movieData) {
        let history = getHistory();
        
        // 移除已存在的记录（避免重复）
        history = history.filter(item => item.id !== movieData.id);
        
        // 添加新记录到开头
        history.unshift({
            ...movieData,
            timestamp: Date.now(),
            progress: 0
        });
        
        // 限制记录数量
        if (history.length > MAX_RECORDS) {
            history = history.slice(0, MAX_RECORDS);
        }
        
        saveHistory(history);
        return history;
    }
    
    // 删除单条记录
    function removeHistory(movieId) {
        let history = getHistory();
        history = history.filter(item => item.id !== movieId);
        saveHistory(history);
        return history;
    }
    
    // 清空所有记录
    function clearHistory() {
        localStorage.removeItem(STORAGE_KEY);
        return [];
    }
    
    // 检查是否存在记录
    function hasHistory(movieId) {
        const history = getHistory();
        return history.some(item => item.id === movieId);
    }
    
    // 获取记录数量
    function getHistoryCount() {
        return getHistory().length;
    }
    
    return {
        getHistory,
        saveHistory,
        addHistory,
        removeHistory,
        clearHistory,
        hasHistory,
        getHistoryCount
    };
})();

// 在电影详情页自动记录访问
function recordMovieVisit(movieData) {
    if (movieData && movieData.id && movieData.title) {
        HistoryManager.addHistory(movieData);
    }
}