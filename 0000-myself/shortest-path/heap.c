#include "./heap.h"

int main()
{
    Heap hp = {0};

    heappush(&hp, 8, 31);
    heappush(&hp, 4, 8);
    heappush(&hp, 7, 30);
    heappush(&hp, 5, 14);
    heappush(&hp, 6, 24);
    heappush(&hp, 1, 2);
    heappush(&hp, 3, 5);
    heappush(&hp, 2, 3);

    heapprint(hp);

    printf("idx popped : %d\n", heappop_idx(&hp));
    printf("idx popped : %d\n", heappop_idx(&hp));
    printf("idx popped : %d\n", heappop_idx(&hp));
    printf("idx popped : %d\n", heappop_idx(&hp));
    printf("idx popped : %d\n", heappop_idx(&hp));
    printf("idx popped : %d\n", heappop_idx(&hp));
    printf("idx popped : %d\n", heappop_idx(&hp));
    printf("idx popped : %d\n", heappop_idx(&hp));

    heapprint(hp);
}