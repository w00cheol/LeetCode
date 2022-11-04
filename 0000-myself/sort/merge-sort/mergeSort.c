#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX_NUM 9999
#define SORT_SIZE 10000
#define PRINT_SIZE 10

void merge(int* list, int left, int right, int size){
    int mid = (left + right)/2;
    int left_runner = left;
    int right_runner = mid + 1;
    int tmp[size];
    
    for(int i = 0; i < size; i++){
        tmp[i] = list[i];
    }

    while(left_runner <= mid && right_runner <= right){
        if(tmp[left_runner] <= tmp[right_runner]){
            list[left++] = tmp[left_runner++];
        }
        else {
            list[left++] = tmp[right_runner++];
        }
    }

    while(left_runner <= mid){
        list[left++] = tmp[left_runner++];
    }
    while(right_runner <= right){
        list[left++] = tmp[right_runner++];
    }

    return;
}
void mergeSort(int* list, int left, int right, int size){
    if(left < right){
        int mid = (left + right)/2;
        mergeSort(list, left, mid, size);
        mergeSort(list, mid+1, right, size);
        merge(list, left, right, size);
    }
    
    return;
}

int main()
{
    int randNums[SORT_SIZE];
    srand((unsigned int)time(NULL));

    for(int i = 0; i < SORT_SIZE; i++){
        randNums[i] = rand()%(MAX_NUM + 1);
    }

    mergeSort(randNums, 0, SORT_SIZE - 1, SORT_SIZE);

    int printNums[PRINT_SIZE];
    for(int i = 0; i < PRINT_SIZE; i++){
        printNums[i] = rand()%SORT_SIZE;
    }

    mergeSort(printNums, 0, PRINT_SIZE - 1, PRINT_SIZE);

    for(int i = 0; i < PRINT_SIZE; i++){
        printf("%d번째 인덱스: %d\n", printNums[i], randNums[printNums[i]]);
    }

    return 0;
}