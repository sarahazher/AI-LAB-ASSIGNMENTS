#include <iostream>
#include <conio.h>
using namespace std;

int main() {
    int nn;
    cout << "Enter Number of Nodes: ";
    cin >> nn;

    int graph[50][50] = {0};
    char ch[7] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};

    for (int i = 0; i < nn; i++) {
        for (int j = i + 1; j < nn; j++) {
            cout << "Enter Distance between " << ch[i] << " - " << ch[j] << ": ";
            cin >> graph[i][j];
            graph[j][i] = graph[i][j];
        }
    }

    int final[50][50], via[50][50];

    for (int i = 0; i < nn; i++) {
        for (int j = 0; j < nn; j++) {
            final[i][j] = graph[i][j];
            via[i][j] = i;
        }
    }

    for (int k = 0; k < nn; k++) {
        for (int i = 0; i < nn; i++) {
            for (int j = 0; j < nn; j++) {
                if (final[i][j] == -1 || (final[i][j] > final[i][k] + final[k][j] && final[i][k] != -1 && final[k][j] != -1)) {
                    final[i][j] = final[i][k] + final[k][j];
                    via[i][j] = k;
                }
            }
        }
    }

    cout << "After Update:" << endl;
    for (int i = 0; i < nn; i++) {
        cout << ch[i] << " Table" << endl;
        cout << "Node\tDist\tVia" << endl;
        for (int j = 0; j < nn; j++) {
            cout << ch[j] << "\t" << final[i][j] << "\t" << (i == via[i][j] ? "-" : ch[via[i][j]) << endl;
        }
    }

    return 0;
}
