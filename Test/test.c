#include <stdio.h>

int main() {
    int i, j;
    int n = 10; // 可以调整心形的大小

    for (i = n/2; i <= n; i+=2) {
        // 打印左边的星号
        for (j = 1; j < n-i; j+=2) {
            printf(" ");
        }

        // 打印左半边的星号
        for (j = 1; j <= i; j++) {
            printf("*");
        }

        // 打印中间的空格
        for (j = 1; j <= n-i; j++) {
            printf(" ");
        }

        // 打印右半边的星号
        for (j = 1; j <= i; j++) {
            printf("*");
        }

        printf("\n");
    }

    // 打印心形的下半部分
    for (i = n; i >= 1; i--) {
        for (j = i; j < n; j++) {
            printf(" ");
        }

        // 打印下半部分的星号
        for (j = 1; j <= (i*2)-1; j++) {
            printf("*");
        }

        printf("\n");
    }

    return 0;
}
