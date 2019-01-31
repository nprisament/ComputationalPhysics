#include <iostream>
#include <limits>
#include <cmath>

using namespace std;

class function {
public:
	double operator()(double x) const {
		return 7.2 * x * x * x * x - 4.0 * x * x + 2;
	}
};

double trap_rule(const function & f, double a, double b, double h) {
	double sum = 0;
	h = 1 / h;
	for (double i = a; i <= b; i += h) {
		double w = 1;
		if (i == 0 || i == 1) w = 0.5;
		sum += w * h * f(i);
	}
	return sum;
}

double simp(const function & f, double a, double b, double h) {
	if ((int) h % 2 == 0) h += 1.0;
	double sum = 0, w = 1, inc = (b - a) / h; 
	b = h * inc + a;
	for (double i = a; i <= b; i += inc) {
		if (i == a || i == b) w = 1;
		else if (w == 1 || w == 2) w = 4;
		else w = 2;
		sum += w * inc * f(i) / 3.0;
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
	double exact = 23758.746666666666, ans = 0;
	cout << "Trapezoidal Rule" << endl;
	for(unsigned h = 10; h < 100; h += 10) {
		ans = trap_rule(f, 0, 7, h);
		cout << h << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	for(unsigned h = 100; h < 1000; h += 100){
		ans = trap_rule(f, 0, 7, h);
		cout << h << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	for(unsigned h = 1000; h <= 10000000; h *= 10) {
		ans = trap_rule(f, 0, 7, h);
		cout << h << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	cout << "Simpson's Rule" << endl;
	for(unsigned h = 10; h < 100; h += 10) {
		ans = simp(f, 0, 7, h);
		cout << h + 1.0 << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	for(unsigned h = 100; h < 1000; h += 100){
		ans = simp(f, 0, 7, h);
		cout << h + 1.0 << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	for(unsigned h = 1000; h <= 10000000; h *= 10) {
		ans = simp(f, 0, 7, h);
		cout << h + 1.0 << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	cout << "Gaussian Quadrature" << endl;
	cout << guass(f, 0, 7) << endl;
	return 1;
}