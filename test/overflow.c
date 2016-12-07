#include<stdio.h>
#include<string.h>

int main() {
    char c[4];
    read(0, c, 1);
    if (c[0]>127||c[0]<48)
        strcpy(c+4,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"); // crash it
    printf("Ah\n");
    return 0;
}
