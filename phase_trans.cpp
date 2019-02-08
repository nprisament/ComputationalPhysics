#include <iostream>
#include <limits>
#include <cmath>
#include <vector>
#include <utility>

using namespace std;

double LJ(const pair<double,double> & r1, const pair<double,double> & r2) {
	double a = 5;
	double d = sqrt(pow(min(abs(r1.first - r2.first), abs(r2.first + a - r1.first)), 2)
		+ pow(min(abs(r1.second - r2.second), abs(r2.second + a - r1.second)), 2));
	return 1 / pow(d, 12) - 1 / pow(d, 6);
}

double energy(const vector<pair<double,double>> & p) {
	double e = 0.0;
	for(unsigned i = 0; i < p.size() - 1; ++i) {
		for(unsigned j = i + 1; j < p.size(); ++j) {
			e += LJ(p[i],p[j]);	
		}
	}
	return e;
}

int main(){
	double max = pow(10,7), N = 20, a = 5, dx = 0.2, kT = .02, dT = kT / max, low = numeric_limits<double>::max();
	vector<pair<double,double>> particles(N);
	srand (time(NULL));
	for(unsigned i = 0; i < N; ++i) {
		particles[i].first = ((double) rand() / (RAND_MAX)) * a;
		particles[i].second = ((double) rand() / (RAND_MAX)) * a; 
	}
	double E_0 = energy(particles);
	for(unsigned i = 0; i < max; ++i) {
	 	cout << E_0 << " " << low << endl;
	 	unsigned n = (int) (((double) rand() / (RAND_MAX)) * N);
	 	double theta = ((double) rand() / (RAND_MAX)) * 2 * M_PI;
	 	pair<double,double> old = particles[n];
	 	particles[n].first += cos(theta) * dx;
		if (particles[n].first >= a) particles[n].first -= a; //periodic boundary conditions
		if (particles[n].first < 0) particles[n].first += a;
		particles[n].second += sin(theta) * dx;
		if (particles[n].second >= a) particles[n].second -= a;
		if (particles[n].second < 0) particles[n].second += a;
		double E_1 = energy(particles);
		if (E_1 < E_0) E_0 = E_1;
		else if (exp(-(E_1 - E_0) / kT) > ((double) rand() / (RAND_MAX))) E_0 = E_1;
		else particles[n] = old;
		if (E_0 < low) low = E_0;
		kT -= dT;
	}
	cout << energy(particles) << endl;
	return 1;
}
