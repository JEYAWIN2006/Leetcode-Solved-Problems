class Solution {
public:
    int minAreaRect(vector<vector<int>>& v) {
        int n = v.size(), area = INT_MAX;
        unordered_map<int, unordered_set<int>> mp;
        for (int i = 0; i < n; i++) {
            mp[v[i][0]].insert(v[i][1]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = v[i][0], y1 = v[i][1];
                int x2 = v[j][0], y2 = v[j][1];
                if (x1 == x2 || y1 == y2) continue;
                if (mp[x1].find(y2) != mp[x1].end() && mp[x2].find(y1) != mp[x2].end()) {
                    int currentArea = abs(x2 - x1) * abs(y2 - y1);
                    area = min(area, currentArea);
                }
            }
        }
        
        return area == INT_MAX ? 0 : area;
    }
};