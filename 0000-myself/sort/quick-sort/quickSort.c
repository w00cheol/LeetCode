#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 100
#define MAX_NUM 100

void quickSort(int* arr, int left, int right){
    if (left >= right) return;
    
    int left_runner = left, right_runner = right;
    int pivot = arr[(left + right) / 2];

    // 피봇 정렬
    while (left_runner < right_runner){
        while (arr[left_runner] < pivot){
            left_runner += 1;
        }
        while (pivot < arr[right_runner]){
            right_runner -= 1;
        }

        if (left_runner <= right_runner){
            if(left_runner < right_runner){
                int temp = arr[left_runner];
                arr[left_runner] = arr[right_runner];
                arr[right_runner] = temp;
            }
            left_runner += 1;
            right_runner -= 1;
        }
    }

    quickSort(arr, left, right_runner);
    quickSort(arr, left_runner, right);
    return;
}

int main()
{
    srand((unsigned int)time(NULL));
    int arr[SIZE];

    printf("before quick sort\n");
    for (int i = 0; i < SIZE; i++){
        arr[i] = rand() % (MAX_NUM + 1);
        printf("%d ", arr[i]);
    }
    printf("\n");

    quickSort(arr, 0, SIZE - 1);

    printf("after quick sort\n");
    for (int i = 0; i < SIZE; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    for (int i = 0; i < SIZE - 1; i++){
        if (arr[i] > arr[i+1]){
            printf("false\n");
            return 0;
        }
    }

    printf("true\n");
    return 0;
}