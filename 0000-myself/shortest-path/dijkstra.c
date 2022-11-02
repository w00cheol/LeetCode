#include "./heap.h"
#include <string.h>

#define VERTEX_SIZE 10
#define VERTEX_NAME_SIZE 10
#define INF 100000

enum BOOL {FALSE, TRUE};
enum REGIONS {KR, KJ, NS, DG, DJ, BS, SU, WJ, CA, PH};

typedef struct Vertex {
    int index;
    int weight[VERTEX_SIZE];
    enum BOOL visit[VERTEX_SIZE];
} Vertex;

// 각 Vertex 초기화 함수
void init_vertex(Vertex* v, int idx, int w[VERTEX_SIZE]){
    v->index = idx;
    for(int i = 0; i < VERTEX_SIZE; i++){
        v->weight[i] = w[i];
        v->visit[i] = FALSE;
    }
}

// 해당 Vertex로부터 모든 Vertex까지의 거리 출력
void print_weight(Vertex v, char** vertexes){
    printf("%s -> ", *(vertexes + v.index));
    for(int i = 0; i < VERTEX_SIZE; i++){
        printf("%s: %d ", *(vertexes + i), *(v.weight + i));
    }
    printf("\n\n");
}

// 아직 확정(방문)되지 않은 Vertex 중 최소 거리 Vertex index 반환
int get_min_vertex(Vertex v){
    int min_v = -1;
    int min_w = INF;
    for(int i = 0; i < VERTEX_SIZE; i++){
        // 아직 방문하지 않은 Vertex 중, 최소 거리 Vertex 검색
        if((v.visit[i] == FALSE) && (v.weight[i] < min_w)){
            min_v = i;
            min_w = v.weight[i];
        }
    }

    // 최소 거리 Vertex index 반환
    return min_v;
}

// Vertex 확정(방문) 후 메인 Vertex의 거리 배열 갱신
void visit_vertex_with_heap(Vertex* v, Vertex next, int next_index, Heap* heap){
    // Vertex 확정(방문) 처리
    v->visit[next_index] = TRUE;

    for(int i = 0; i < VERTEX_SIZE; i++){
        if(v->visit[i] == FALSE){
            // 확정된 Vertex(next)를 거칠 경우 i까지의 거리가 더 짧아진다면 갱신
            if(v->weight[i] > (v->weight[next_index] + next.weight[i])) {
                v->weight[i] = v->weight[next_index] + next.weight[i];
                heappush(heap, i, v->weight[i]);
            }
        }
    }
}

void visit_vertex(Vertex* v, Vertex next, int next_index){
    // Vertex 확정(방문) 처리
    v->visit[next_index] = TRUE;
    for(int i = 0; i < VERTEX_SIZE; i++){
        if(v->visit[i] == FALSE){
            // 확정된 Vertex(next)를 거칠 경우 i까지의 거리가 더 짧아진다면 갱신
            if(v->weight[i] > (v->weight[next_index] + next.weight[i])) {
                v->weight[i] = v->weight[next_index] + next.weight[i];
            }
        }
    }
}

// 힙을 이용한 다익스트라 실행 함수
void dijkstra_with_heap(Vertex* v, int target){
    Heap heap = {0};
    int next_vertex;
    for(int i = 0; i < VERTEX_SIZE; i++){
        if((v+target)->weight[i] != INF){
            heappush(&heap, i, (v+target)->weight[i]);
        }
    }

    while (heap.size > 0) {
        // 다음 확정시킬 Vertex index
        next_vertex = heappop_idx(&heap);
        if((v+target)->visit[next_vertex] == TRUE){
            continue;
        }
        // vertex 확정(방문) 후 거리 갱신
        visit_vertex_with_heap(v+target, v[next_vertex], next_vertex, &heap);
    }
}

// 일반 배열 다익스트라 실행 함수
void dijkstra(Vertex* v, int target){
    int next_vertex;
    (v+target)->visit[target] = TRUE;

    for(int i = 0; i < VERTEX_SIZE - 1; i++){
        // 다음 확정시킬 Vertex index
        next_vertex = get_min_vertex(v[target]);
        // vertex 확정(방문) 후 거리 갱신
        visit_vertex(v+target, v[next_vertex], next_vertex);
    }
}

int main()
{
    Vertex v[10] = {0};

    // 순서: "강릉", "광주", "논산", "대구", "대전", "부산", "서울", "원주", "천안", "포항"
    char* vertexes[] = {"강릉", "광주", "논산", "대구", "대전", "부산", "서울", "원주", "천안", "포항"};
    // 거리 초기화
    int init_weights[VERTEX_SIZE][VERTEX_SIZE] = {
        {0, INF, INF, INF, INF, INF, INF, 21, INF, 25}, // 강릉
        {INF, 0, 13, INF, INF, 15, INF, INF, INF, INF}, // 광주
        {INF, 13, 0, INF, 3, INF, INF, INF, 4, INF}, // 논산
        {INF, INF, INF, 0, 10, 9, INF, 7, INF, 19}, // 대구
        {INF, INF, 3, 10, 0, INF, INF, INF, 10, INF}, // 대전
        {INF, 15, INF, 9, INF, 0, INF, INF, INF, 5}, // 부산
        {INF, INF, INF, INF, INF, INF, 0, 15, 12, INF}, // 서울
        {21, INF, INF, 7, INF, INF, 15, 0, INF, INF}, // 원주
        {INF, INF, 4, INF, 10, INF, 12, INF, 0, INF}, // 천안
        {25, INF, INF, 19, INF, 5, INF, INF, INF, 0}, // 포항
    };

    // Vertex 구조체 배열 초기화
    for(int i = 0; i < VERTEX_SIZE; i++){
        init_vertex(&v[i], i, init_weights[i]);
    }
    
    // 서울 선정 (서울 코드: SU -> 6)
    // int target = SU;

    printf("<<일반 배열을 사용한 다익스트라 알고리즘 수행>>\n");
    for(int i = 0; i < VERTEX_SIZE; i++){
        dijkstra(v, i);
        print_weight(v[i], vertexes);
    }

    // Vertex 구조체 배열 초기화
    for(int i = 0; i < VERTEX_SIZE; i++){
        init_vertex(&v[i], i, init_weights[i]);
    }

    // 모든 지역에 대해 다익스트라 알고리즘 수행
    printf("<<우선순위 큐를 사용한 다익스트라 알고리즘 수행>>\n");
    for(int i = 0; i < VERTEX_SIZE; i++){
        dijkstra_with_heap(v, i);
        print_weight(v[i], vertexes);
    }

    return 0;
}