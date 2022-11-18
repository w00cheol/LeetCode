#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX_NUM 9999
#define SORT_SIZE 10000

void selectionSort (int* arr) {
    for (int i = 0; i < SORT_SIZE - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < SORT_SIZE; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }
};

int main()
{
    int rand_nums[SORT_SIZE];
    srand((unsigned int)time(NULL));

    for (int i = 0; i < SORT_SIZE; i++) {
        rand_nums[i] = rand()%(MAX_NUM) + 1; // range : 0 ~ 9999
    }

    selectionSort(rand_nums);

    printf("0001번째 위치하는 숫자: %04d\n", rand_nums[0]);
    for (int i = 1; i < 10; i++) {
        printf("%d번째 위치하는 숫자: %04d\n", i*1000, rand_nums[i*1000 - 1]);
    }
    
    // check
    for (int i = 0; i < SORT_SIZE - 1; i++) {
        if (rand_nums[i] > rand_nums[i + 1]) {
            printf("False\n");
            return 0;
        }
    }

    printf("True\n");
    return 1;
}