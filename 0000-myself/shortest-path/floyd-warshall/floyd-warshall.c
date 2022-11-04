#include <stdio.h>

#define VERTEX_SIZE 10
#define INF 100000
#define min(a, b) a < b ? a : b

enum REGIONS {KR, KJ, NS, DG, DJ, BS, SU, WJ, CA, PH};

int main()
{
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

    for(int i = 0; i < VERTEX_SIZE; i++){
        for(int j = 0; j < VERTEX_SIZE; j++){
            for(int k = 0; k < VERTEX_SIZE; k++){
                init_weights[j][k] = min(init_weights[j][k], init_weights[j][i] + init_weights[i][k]);
            }
        }
    }

    for(int i = 0; i < VERTEX_SIZE; i++){
        printf("%s -> ", vertexes[i]);
        for(int j = 0; j < VERTEX_SIZE; j++){
            printf("%s:%d\t", vertexes[j], init_weights[i][j]);
        }
        printf("\n");
    }
    

    return 0;
}