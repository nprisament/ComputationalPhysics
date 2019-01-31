#include <iostream>
#include <cmath>

using namespace std;

inline bool func(double rx, double ry) {
	if (ry < 1.00 / rx) {
		return true;
	}
}

int main(){
	srand (time(NULL));
	double a = 0.00, tot = 1000000;
	for (int i = 0; (double) i <= tot; i++) {
		double rx = (double) rand() / (RAND_MAX) + 1;
		double ry = (double) rand() / (RAND_MAX);
		if (ry < 1.00 / rx) a++; 
	}
	double area = a/tot * 1;
	double ee = pow(2, (1/area));
	cout << ee << endl;
	return 1;
}