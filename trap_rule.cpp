#include <iostream>
#include <cmath>

using namespace std;

int main(){
	double sum = 0, h = 0.000001;
	for (double i = 0; i <= 1; i += h) {
		double w = 1;
		if (i == 0 || i == 1) w = 0.5;
		sum += w * h * exp(i);
	}
	cout << sum << endl;
	return 1;
}