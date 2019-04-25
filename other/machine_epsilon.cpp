#include <iostream>
#include <limits>

using namespace std;

int main(){
	float feps = 1.0;
	double deps = 1.0;
	
	while(1.0 + (float)(feps / 2.0) > 1.0) {
		feps /= 2;
	}

	while(1.0 + (double)(deps / 2.0) > 1.0) {
		deps /= 2;
	}

	cout.precision(numeric_limits<float>::max_digits10);
	cout << feps << endl;

	cout.precision(numeric_limits<double>::max_digits10);
	cout << deps << endl;
	return 1;
}