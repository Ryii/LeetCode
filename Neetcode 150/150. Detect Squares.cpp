class DetectSquares {
private:
    int pCount[1001][1001] = {};
    vector<pair<int, int>> points;
public:
    DetectSquares() {}
    
    void add(vector<int> point) {
        pCount[point[0]][point[1]]++;
        points.emplace_back(point[0], point[1]);
    }
    
    int count(vector<int> point) {
        int x1 = point[0];
        int y1 = point[1];
        int ans = 0;
        for (auto &[x3, y3] : points) {
            if (abs(x1 - x3) != abs(y1 - y3) || x1 == x3) continue;
            ans += pCount[x1][y3] * pCount[x3][y1];
        }
        return ans;
    }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */