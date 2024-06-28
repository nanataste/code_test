#include <stdio.h>

int power(int x, int y) {
    if (y == 0)
        return 1;
    else
        return x * power(x, y - 1);
}

int main() {
    int base, exponent;
    printf("밑과 지수를 입력하세요 ");
    scanf("%d %d", &base, &exponent);


    int result = power(base, exponent);
    printf("%d의 %d 제곱은: %d\n", base, exponent, result);

    return 0;
}
