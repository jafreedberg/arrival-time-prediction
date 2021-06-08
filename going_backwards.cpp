#include<Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
DataFrame going_backwards(DataFrame df){

    IntegerVector stop_seq = df["stop_sequence"];
    CharacterVector trip_id = df["trip_id"];
    CharacterVector status = df["status"];

    int len = stop_seq.size();;
    IntegerVector backwards(len);
    int last_stop_i = 0;
    int curr_stop_i = 0;


    for(int i = 0; i < len; i++){
      backwards[i] = 0;
        if(stop_seq[i] != stop_seq[curr_stop_i]){
            last_stop_i = curr_stop_i;
            curr_stop_i = i;
        }
        if(stop_seq[curr_stop_i] < stop_seq[last_stop_i] && trip_id[curr_stop_i] == trip_id[last_stop_i]){
          for(int j = last_stop_i; j < curr_stop_i; j++){
            backwards[j] = 1;
            status[j] = status[curr_stop_i];
          }
        }
    }
    return  DataFrame::create(Named("backwards")=backwards,
                              Named("status") =status);
}
    