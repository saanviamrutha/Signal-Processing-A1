#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "header.h"

int main() {
	FILE *fp = fopen("fft.dat", "w");
	double complex x[8] = {1, 2, 3, 4, 2, 1, 0, 0};
	double complex *X = fft(x, 8);
	for (int i = 0; i < 8; i++) {
		printf("%lf %lf\n", creal(X[i]), cimag(X[i]));
		fprintf(fp, "%lf\n", creal(X[i]));
	}
	fclose(fp);
	return 0;
}