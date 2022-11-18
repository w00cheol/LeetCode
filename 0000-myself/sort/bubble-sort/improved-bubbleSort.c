#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX_NUM 9999
#define SORT_SIZE 10000

void bubbleSort (int* arr) {
    for (int i = 0; i < SORT_SIZE - 1; i++) {
        int count = 0;
        for (int j = 0; j < SORT_SIZE - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
                count = 1;
            }
        }
        if (count == 0) {
            printf("completed in progress %d.\n", i + 1);
            return;
        }
    }
};

int main()
{
    int rand_nums[SORT_SIZE];
    srand((unsigned int)time(NULL));

    for (int i = 0; i < SORT_SIZE; i++) {
        rand_nums[i] = rand()%(MAX_NUM) + 1; // range : 0 ~ 9999
    }

    bubbleSort(rand_nums);
    
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