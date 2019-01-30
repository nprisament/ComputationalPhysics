#include <iostream>
#include <cmath>

using namespace std;

class function {
public:
	unsigned int operator()(double x) const {
		return exp(x);
	}
};

double trap_rule(const function & f, double a, double b) {
	double sum = 0, h = 0.000001;
	for (double i = a; i <= b; i += h) {
		double w = 1;
		if (i == 0 || i == 1) w = 0.5;
		sum += w * h * f(i);
	}
	return sum;
}

int main(){
	function f;
	cout << trap_rule(f, 0, 1) << endl;
	
	return 1;
}