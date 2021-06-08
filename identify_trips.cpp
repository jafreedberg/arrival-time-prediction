#include<Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
DataFrame identify_trips(DataFrame df){

    CharacterVector trip_id = df["trip_id"];

    int len = trip_id.size();
    IntegerVector service(len);
    int trip_service = 0;


    for(int i = 0; i < len - 1; i++){
        service[i] = trip_service;
        if(trip_id[i] != trip_id[i + 1]){
            trip_service++;
        }
    }
    return  DataFrame::create(Named("service")=service);
}