#include <iostream>
#include <thread>
#include <chrono>
#include <algorithm>
using namespace std;
using namespace std::chrono;
typedef unsigned long long ull;

//variaveis com muitos bits para o contador perder muito tempo com eles
ull OddSum = 0;
ull EvenSum = 0;

//Funcoes para testar a eficacia das threads
void findEven(ull start, ull end){
    for(ull i = start; i<= end; ++i){
        if((i & 1) == 0){
            EvenSum += 1;
        }
    }
}

void findOdd(ull start, ull end){
    for(ull i = start; i<= end; ++i){
        if((i & 1) == 0){
            OddSum += 1;
        }
    }
}
int main(){
    ull start = 0, end = 1900000000;

    //inicio da contagem
    auto startTime = high_resolution_clock::now();

    //Antes de colocar essas threads, o tempo foi de 15 s
    std::thread t1(findEven, start, end);
    std::thread t2(findEven, start, end);

    //iniciando as threads
    t1.join();
    t2.join();

    //Apos criar as threads estas funcoes nao tem mais serventia, porque t1 e t2 jah estao chamada as funcoes
    /*findOdd(start, end);
    findEven(start, end);*/

    //final da contagem e estamacao da duracao
    auto stopTime = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stopTime - startTime);

    //impressao do valor dos contadores para verificar se realmente estao gastando o tempo
    cout << "OddSum : " << OddSum << endl;
    cout << "EvenSum : " << EvenSum << endl;

    //impressao do tempo convertida de microssegundos para segundos.
    cout << duration.count()/1000000 << endl;
    return 0;
}
