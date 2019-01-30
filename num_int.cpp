#include <iostream>
#include <limits>

using namespace std;

class function {
public:
	double operator()(double x) const {
		return 3*x*x;
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

double simp(const function & f, double a, double b) {
	double sum = 0, h = (b - a) / 10001.0, w = 1;
	b = h * 10001.0 + a;
	for (double i = a; i <= b; i += h) {
		if ((i == a || i == b)) w = 1;
		else if (w == 1 || w == 2) w = 4;
		else w = 2;
		sum += w * h * f(i) / 3.0;
	}
	return sum;
}

double guass(const function & f, double a, double b) {
	double c1 = 0.5555555556, c2 = 0.8888888889, c3 = 0.5555555556;
	double x1 = -0.774596669, x2 = 0.0, x3 = 0.774596669;
	double half = (b - a) / 2;
	x2 += (a + half);
	x1 *= half; x1 += x2;
	x3 *= half; x3 += x2;
	return (c1 * f(x1) + c2 * f(x2) + c3 * f(x3)) * half;
}

int main(){
	function f;
	cout.precision(numeric_limits<double>::max_digits10);
	cout << trap_rule(f, 0, 2) << endl;
	cout << simp(f, 0, 2) << endl;
	cout << guass(f, 0, 2) << endl;
	return 1;
}