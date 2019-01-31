#include <iostream>
#include <cmath>
#include <vector>
#include <limits>

using namespace std;

double approx(double x, unsigned int N, vector<double> & fact) {
	double sum = 0;
	for (unsigned int i = 0; i <= N; i++)
		sum += pow(-x, i) / (double)fact[i];
	return sum;
}

int main(){
	int N = 31;
	vector<double> fact(N);
	double x = 10, ans = exp(-x);
	cout.precision(numeric_limits<double>::max_digits10);
	fact[0] = 1;
	for(unsigned i = 1; i < N; ++i)
		fact[i] = fact[i - 1] * i;
	for(unsigned i = 1; i < N; ++i) {
		double test = approx(x, i, fact);
		cout << test << " ";
		cout << abs(ans + test) << endl;
	}
	
	cout << ans << endl;
	return 1;
}