#include <stdio.h>

#define N 20

double x(int n) {
	if (n < 0 || n > 5) return 0;
	else if (n < 4) return n + 1;
	else return 6 - n;
}

double y(int n) {
	if (n < 0) return 0;
	else return x(n) + x(n-2) - 0.5 * y(n-1);
}

int main() {
	FILE *fp = fopen("y.dat", "w");
	for (int i = 0; i < N; i++) {
		fprintf(fp, "%lf\n", y(i));
	}

    fclose(fp);
	return 0;
}