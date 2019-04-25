#include <iostream>
#include <limits>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <mutex>

#include "parallel_for.h"

using namespace std;

double a = 15;

double distance2(const vector<double> & r1, const vector<double> & r2){
	return pow(min(abs(r1[0] - r2[0]), abs(r2[0] + a - r1[0])), 2)
		+ pow(min(abs(r1[1] - r2[1]), abs(r2[1] + a - r1[1])), 2)
		+ pow(min(abs(r1[2] - r2[2]), abs(r2[2] + a - r1[2])), 2);
}

double distance(const vector<double> & r1, const vector<double> & r2){
	return sqrt(pow(min(abs(r1[0] - r2[0]), abs(r2[0] + a - r1[0])), 2)
		+ pow(min(abs(r1[1] - r2[1]), abs(r2[1] + a - r1[1])), 2)
		+ pow(min(abs(r1[2] - r2[2]), abs(r2[2] + a - r1[2])), 2));
}

double LJ(const vector<double> & r1, const vector<double> & r2) {
	double d = distance2(r1, r2);
	return 1 / pow(d, 6) - 1 / pow(d, 3);
}

double energy(const vector<vector<double>> & p, vector<vector<double>> & energies, unsigned int n) {
	double e = 0.0;
	if (n == p.size()) {
		for(unsigned i = 0; i < p.size() - 1; ++i) {
			for(unsigned j = i + 1; j < p.size(); ++j) {
				energies[i][j] = LJ(p[i],p[j]);	
			}
		}
	} else {
		mutex m;
		parallel_for(p.size() - 1, [&](int start, int end){ 
			for(unsigned i = start; i < (unsigned) end; ++i) {
				for(unsigned j = i + 1; j < p.size(); ++j) {
					if (i == n || j == n) {
						lock_guard<std::mutex> guard(m);
						energies[i][j] = LJ(p[i],p[j]);	
					}
				}
			}
		});
	}
	for(unsigned i = 0; i < p.size() - 1; ++i) {
		for(unsigned j = i + 1; j < p.size(); ++j) {
			e += energies[i][j];	
		}
	}
	return e;
}

double g(const vector<vector<double>> & p, double r, double dr, double V, double N) {
	unsigned int count = 0;
	mutex m;
	parallel_for(p.size(), [&](int start, int end){ 
		for(unsigned i = start; i < (unsigned) end; ++i) {
			for(unsigned j = 0; j < p.size(); ++j) {
				if (i == j) continue;
				double d = distance(p[i], p[j]);
				if (d > r && d < r + dr) {
					lock_guard<std::mutex> guard(m);
					count++;
				}
			}
		}
	});
	double dN = ((double) count) / ((double) p.size());
	double dV = M_PI * (pow(r + dr, 2) - r * r);
	return (dN * V) / (dV * N);
}

int main(){
	double max = pow(10,6), N = 50, dx = 0.1, dr = 0.01, kT = 0.30, dT = kT / max, low = numeric_limits<double>::max(), V = a * a;
	unsigned pair_dist_count = 0;
	vector<vector<double>> particles(N, vector<double>(3, 0.0));
	vector<vector<double>> energies(N-1, vector<double>(N-1, 0.0));
	vector<double> pair_dist((unsigned) a/(2 * dr));
	srand (time(NULL));
	for(unsigned i = 0; i < N; ++i) {
		particles[i][0] = ((double) rand() / (RAND_MAX)) * a;
		particles[i][1] = ((double) rand() / (RAND_MAX)) * a;
		particles[i][2] = ((double) rand() / (RAND_MAX)) * a; 
	}
	double E_0 = energy(particles,energies,N);
	for(unsigned i = 0; i < max; ++i) {
		unsigned n = (int) (((double) rand() / (RAND_MAX)) * N);
		double theta = ((double) rand() / (RAND_MAX)) * 2 * M_PI;
		double phi = ((double) rand() / (RAND_MAX)) * M_PI;
		vector<vector<double>> energies_old(energies);
		vector<double> old(particles[n]);
		particles[n][0] += cos(theta) * sin(phi) * dx;
		if (particles[n][0] >= a) particles[n][0] -= a; //periodic boundary conditions
		if (particles[n][0] < 0) particles[n][0] += a;
		particles[n][1] += sin(theta) * sin(phi) * dx;
		if (particles[n][1] >= a) particles[n][1] -= a;
		if (particles[n][1] < 0) particles[n][1] += a;
		particles[n][2] += cos(phi) * dx;
		if (particles[n][2] >= a) particles[n][2] -= a;
		if (particles[n][2] < 0) particles[n][2] += a;
		double E_1 = energy(particles,energies,n);
		if (E_1 < E_0) E_0 = E_1;
		else if (exp(-(E_1 - E_0) / kT) > ((double) rand() / (RAND_MAX))) E_0 = E_1;
		else {
			energies = energies_old;
			particles[n] = old;
		}
		if (E_0 < low) low = E_0;
		//kT -= dT;
		if (i >= max / 2 && i % 100 == 0) {
			cout << E_0 << " " << low << "\n";
			for(double j = 0; j < pair_dist.size(); j++) {
				pair_dist[j] += g(particles, j * dr, dr, V, N);
			}
			++pair_dist_count;
		}
	}
	cout << low << endl << endl << endl;

	cout << "x" << endl;
	for(unsigned i = 0; i < particles.size(); ++i) {
		cout << particles[i][0] << endl;
	}
	cout << "y" << endl;
	for(unsigned i = 0; i < particles.size(); ++i) {
		cout << particles[i][1] << endl;
	}
	cout << "z" << endl;
	for(unsigned i = 0; i < particles.size(); ++i) {
		cout << particles[i][2] << endl;
	}
	cout << endl;

	for(unsigned i = 0; i < pair_dist.size(); ++i) {
		pair_dist[i] /= pair_dist_count;
	}

	for(unsigned i = 0; i < pair_dist.size(); ++i) {
		cout << pair_dist[i] << endl;
	}

	return 1;
}
