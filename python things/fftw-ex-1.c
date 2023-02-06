#include <fftw3.h>              // includes the header file needed in order to use FFTW3

int main(void) {                // main method
    int N;                      // contains integer N which has the dimension of the input and output data of the FFT
    fftw_complex *in, *out;     // pointers in and out will contain the input and output of the FFT (to allocate memory we use fftw_malloc
    fftw_plan my_plan;          // stores the type of FFT that we want to perform
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex)*N);                       // pointer
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex)*N);                      // pointer
    my_plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);            // declares the type of plan
        // we're performing a 1D DFT
        // int N: the dimension of the pointers in and out
        // fftw_complex *in: the pointer that stores the input data
        // fftw_complex *out: the pointer that stores the output data
        // int FFTW_FORWARD: FFTW_FORWARD is an int constant of the package
        // unsigned FFTW_ESTIMATE: FFTW_ESTIMATE is a flag that tells the function how well must be optimized

    fftw_execute(my_plan);          // executes the FFT stored in my_plan

    fftw_destroy_plan(my_plan);     // deallocate the memory stored by the plan
    fftw_free(in);                  // deallocate the memory stored in the in pointer
    fftw_free(out);                 // deallocate the memory stored in the out pointer

    return 0;
}