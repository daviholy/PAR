#include <iostream>
#include "vcl/version2/vectorclass.h"
void smooth_signal_cpp(const double *__restrict y, double *__restrict result, int result_size){
    for (int i=0; i< (result_size + 2); i++){
        result[i] = (y[i] + y[i+1] + y[i+2])/3;
    }
}
void smooth_signal_cpp_vec(const double *__restrict y, double *__restrict result, int result_size){
    Vec4d va,vb,vc;
    int i;
    for (i = 0; i< (result_size/4); i +=4){
        va.load(y + i);
        vb.load(y + i + 1);
        vc.load(y + i + 2);
        vc += va + vb;
        vc /= 3;
        vc.store(result + i);
    }
    for(; i < result_size + 2; i++){
        result[i] = (y[i] + y[i+1] + y[i+2])/3;
    }
}