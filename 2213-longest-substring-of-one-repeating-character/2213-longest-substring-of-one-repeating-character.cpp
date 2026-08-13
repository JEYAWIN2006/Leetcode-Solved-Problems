struct Node {
    int cntFront, cntLast;
    char front, last;
    int maxi, len;
};

class segmentTree {
    vector<Node> seg;

  public:
    segmentTree(int n) {
        seg.resize(4 * n + 1);
    }

    void build(int idx, int low, int high, string &s) {
        if (low == high) {
            seg[idx].cntFront = seg[idx].cntLast = 1;
            seg[idx].front = seg[idx].last = s[low];
            seg[idx].maxi = seg[idx].len = 1;
            return;
        }
        int mid = (low + high) >> 1;
        build(2*idx+1, low, mid, s);
        build(2*idx+2, mid+1, high, s);
        seg[idx].len = seg[2*idx+1].len + seg[2*idx+2].len;
        int L = 2*idx+1, R = 2*idx+2;
        bool leftUniform  = seg[L].front == seg[L].last && seg[L].cntFront == seg[L].len;
        bool rightUniform = seg[R].front == seg[R].last && seg[R].cntFront == seg[R].len;
        if (seg[L].last == seg[R].front) {
            if (leftUniform && rightUniform) {
                int net = seg[L].maxi + seg[R].maxi;
                seg[idx].front = seg[idx].last = seg[L].last;
                seg[idx].maxi = seg[idx].cntFront = seg[idx].cntLast = net;
            } else {
                int cross = seg[L].cntLast + seg[R].cntFront;
                seg[idx].maxi = max({cross, seg[L].maxi, seg[R].maxi});
                seg[idx].front = seg[L].front;
                seg[idx].last  = seg[R].last;
                seg[idx].cntFront = leftUniform  ? (seg[L].len + seg[R].cntFront)
                                                 : seg[L].cntFront;
                seg[idx].cntLast  = rightUniform ? (seg[R].len + seg[L].cntLast)
                                                 : seg[R].cntLast;
            }
        } else {
            seg[idx].maxi     = max(seg[L].maxi, seg[R].maxi);
            seg[idx].front    = seg[L].front;
            seg[idx].last     = seg[R].last;
            seg[idx].cntFront = seg[L].cntFront;
            seg[idx].cntLast  = seg[R].cntLast;
        }
    }

    void update(int idx, int low, int high, int ind, char ch) {
        if (low == high) {
            seg[idx].cntFront = seg[idx].cntLast = 1;
            seg[idx].front = seg[idx].last = ch;
            seg[idx].maxi = seg[idx].len = 1;
            return;
        }
        int mid = (low + high) >> 1;
        if (ind <= mid)
            update(2*idx+1, low, mid, ind, ch);
        else
            update(2*idx+2, mid+1, high, ind, ch);
        seg[idx].len = seg[2*idx+1].len + seg[2*idx+2].len;

        int L = 2*idx+1, R = 2*idx+2;
        bool leftUniform  = seg[L].front == seg[L].last && seg[L].cntFront == seg[L].len;
        bool rightUniform = seg[R].front == seg[R].last && seg[R].cntFront == seg[R].len;

        if (seg[L].last == seg[R].front) {
            if (leftUniform && rightUniform) {
                int net = seg[L].maxi + seg[R].maxi;
                seg[idx].front = seg[idx].last = seg[L].last;
                seg[idx].maxi = seg[idx].cntFront = seg[idx].cntLast = net;
            } else {
                int cross = seg[L].cntLast + seg[R].cntFront;
                seg[idx].maxi = max({cross, seg[L].maxi, seg[R].maxi});
                seg[idx].front = seg[L].front;
                seg[idx].last  = seg[R].last;
                seg[idx].cntFront = leftUniform  ? (seg[L].len + seg[R].cntFront)
                                                 : seg[L].cntFront;
                seg[idx].cntLast  = rightUniform ? (seg[R].len + seg[L].cntLast)
                                                 : seg[R].cntLast;
            }
        } else {
            seg[idx].maxi     = max(seg[L].maxi, seg[R].maxi);
            seg[idx].front    = seg[L].front;
            seg[idx].last     = seg[R].last;
            seg[idx].cntFront = seg[L].cntFront;
            seg[idx].cntLast  = seg[R].cntLast;
        }
    }

    int query() {
        return seg[0].maxi;
    }
};

class Solution {
  public:
    vector<int> longestRepeating(string &s,string &queryCharacters,vector<int>& queryIndices) {
        int n = s.size(), k = queryCharacters.size();
        segmentTree sg(n);
        sg.build(0, 0, n - 1, s);

        vector<int> ans(k);
        for (int i = 0; i < k; i++) {
            sg.update(0, 0, n - 1, queryIndices[i], queryCharacters[i]);
            ans[i] = sg.query();
        }
        return ans;
    }
};