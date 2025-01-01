#include <stdio.h>
struct node {
    unsigned dist[20];
    unsigned from[20];
} rt[20];

int main() {
    int costmat[20][20], nodes, i, j, k, update;
    printf("Enter the number of nodes: ");
    scanf("%d", &nodes);
    printf("Enter the cost matrix:\n");
    for (i = 0; i < nodes; i++) {
        for (j = 0; j < nodes; j++) {
            scanf("%d", &costmat[i][j]);
            rt[i].dist[j] = costmat[i][j];
            rt[i].from[j] = j;
        }
    }
    do {
        update = 0;
        for (i = 0; i < nodes; i++)
            for (j = 0; j < nodes; j++)
                for (k = 0; k < nodes; k++)
                    if (rt[i].dist[j] > costmat[i][k] + rt[k].dist[j]) {
                        rt[i].dist[j] = costmat[i][k] + rt[k].dist[j];
                        rt[i].from[j] = k;
                        update = 1;
                    }
    } while (update);
    for (i = 0; i < nodes; i++) {
        printf("\nRouter %d:\n", i + 1);
        for (j = 0; j < nodes; j++)
            printf("To node %d via %d Distance %d\n", j + 1, rt[i].from[j] + 1, rt[i].dist[j]);
    }
    return 0;
}