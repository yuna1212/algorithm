/*
    크루스칼 사용: 파이썬 코드와 똑같은 논리전개
*/
#include <iostream>
#include <queue>
using namespace std;
struct edge
{
    int here, other, cost;
};
struct compare
{
    bool operator()(edge &i, edge &o)
    {
        return i.cost > o.cost;
    }
};

int get_cost(pair<int, int> point1, pair<int, int> point2)
{
    int dx = point1.first - point2.first;
    int dy = point1.second - point2.second;
    return dx * dx + dy * dy;
}

priority_queue<edge, vector<edge>, compare> get_edges(int n)
{
    priority_queue<edge, vector<edge>, compare> edges;
    pair<int, int> *vertexes = new pair<int, int>[n];
    for (int i = 0; i < n; i++)
    {
        pair<int, int> p;
        cin >> p.first >> p.second;
        vertexes[i] = p;
        for (int j = 0; j < i; j++)
        {
            edge e;
            e.cost = get_cost(vertexes[i], vertexes[j]);
            e.here = i;
            e.other = j;
            edges.push(e);
        }
    }
    return edges;
}

int *parents, *heights;
int find(int v)
{

    while (v != parents[v])
        v = parents[v];
    return v;
}
void merge(int v, int u) // union 함수
{
    u = find(u);
    v = find(v);
    if (u == v)
        return;
    if (heights[u] > heights[v])
        parents[v] = u;
    else
    {
        parents[u] = v;
        if (heights[u] == heights[v])
            heights[v]++;
    }
}

int main()
{
    priority_queue<edge, vector<edge>, compare> edges;
    int n, c; // 정점 개수, 최소 비용
    cin >> n >> c;
    parents = new int[n];
    for (int i = 0; i < n; i++)
        parents[i] = i;
    heights = new int[n]();
    edges = get_edges(n);

    /* 크루스칼 시작 */
    unsigned int ret = 0;
    while (!edges.empty())
    {
        edge e = edges.top();
        edges.pop();
        if (find(e.here) == find(e.other))
            continue;
        if (e.cost < c)
            continue;
        merge(e.here, e.other);
        ret += e.cost;
    }

    int group = find(0);
    bool is_successed = true;
    for (int i = 0; i < n; i++)
    {
        if (group != find(i))
        {
            is_successed = false;
            break;
        }
    }
    if (is_successed)
        cout << ret;

    else
        cout << -1;
    return 0;
}