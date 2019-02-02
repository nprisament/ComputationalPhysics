#include <iostream>
#include <limits>
#include <cmath>

using namespace std;

class function {
public:
	double operator()(double x) const {
		return 3.0 * x * x - 1.5 * x;
	}
};

double trap_rule(const function & f, double a, double b, double h) {
	double sum = 0, inc = (b - a) / h;
	b = h * inc + a;
	for (double i = a; i <= b; i += inc) {
		double w = 1;
		if (i == 0 || i == b) w = 0.5;
		sum += w * inc * f(i);
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

double gauss(const function & f, double a, double b) {
	double c1 = 0.5555555556, c2 = 0.8888888889, c3 = 0.5555555556;
	double x1 = -0.774596669, x2 = 0.0, x3 = 0.774596669;
	double half = (b - a) / 2;
	x2 += (a + half);
	x1 *= half; x1 += x2;
	x3 *= half; x3 += x2;
	return (c1 * f(x1) + c2 * f(x2) + c3 * f(x3)) * half;
}

double localGauss(const function & f, double a, double b, double h) {
	double sum = 0, inc = (b - a) / h;
	b = h * inc + a;
	for (double i = a; i < b; i += inc) sum += gauss(f, i, i + inc);
	return sum;
}

int main(){
	function f;
	cout.precision(numeric_limits<double>::max_digits10);
	double exact = 306.25, ans = 0;
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
		cout << h << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	for(unsigned h = 100; h < 1000; h += 100){
		ans = simp(f, 0, 7, h);
		cout << h << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	for(unsigned h = 1000; h <= 10000000; h *= 10) {
		ans = simp(f, 0, 7, h);
		cout << h << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	cout << "Gaussian Quadrature" << endl;
	for(unsigned h = 1; h <= 10000000; h *= 10) {
		ans = localGauss(f, 0, 7, h);
		cout << h << " " << ans << " " << abs(ans - exact) / exact << endl;
	}
	return 1;
}
