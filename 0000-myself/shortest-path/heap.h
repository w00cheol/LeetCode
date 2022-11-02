#include <stdio.h>
#define MAX_SIZE 100

typedef struct NodeType{
    int idx;
    int value;
} Node;

typedef struct ArrayHeapType{
    int size;
    Node arr[MAX_SIZE];
} Heap;

void heappush(Heap* heap, int idx, int value){
    int i = heap->size++;
    int parent = (i-1) / 2;

    heap->arr[i].idx = idx;
    heap->arr[i].value = value;

    while((i > 1) && (heap->arr[parent].value > value)){
        int temp_idx = heap->arr[parent].idx;
        int temp_value = heap->arr[parent].value;
        heap->arr[parent].idx = idx;
        heap->arr[parent].value = value;
        heap->arr[i].idx = temp_idx;
        heap->arr[i].value = temp_value;

        i = parent;
        parent = (i-1) / 2;
    }
}

int heappop_idx(Heap* heap){
    int i = 0;
    int min = heap->arr[i].idx;

    int size = --heap->size;
    heap->arr[i].idx = heap->arr[size].idx;
    heap->arr[i].value = heap->arr[size].value;

    while(i+1 <= size - 1){ // 왼쪽 자식 존재할 때
        int child;
        if(i+2 <= size - 1){ // 또한 오른쪽 자식이 존재할 때
            child = (heap->arr[i+1].value < heap->arr[i+2].value) ? i+1 : i+2;
        }
        else {
            child = i+1;
        }
        
        int parent = (child-1) / 2;
        if(heap->arr[parent].value > heap->arr[child].value){
            int temp_idx = heap->arr[child].idx;
            int temp_value = heap->arr[child].value;
            heap->arr[child].idx = heap->arr[(child-1) / 2].idx;
            heap->arr[child].value = heap->arr[(child-1) / 2].value;
            heap->arr[(child-1) / 2].idx = temp_idx;
            heap->arr[(child-1) / 2].value = temp_value;
        }
        else{
            break;
        }
        // 왼쪽 자식 바로 직전 인덱스로 초기화
        i = child * 2;
    }
    return min;
}

void heapprint(Heap heap){
    printf("size: %d -> \n", heap.size);
    for(int i = 0; i < heap.size; i++){
        printf("id: %d value: %d\n", heap.arr[i].idx, heap.arr[i].value);
    }
}