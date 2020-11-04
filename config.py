config_params={
  'preprocess_type': 1,
  "stopword_removal" : 1,
  "index" : 1,
  "tf_scheme" : 1
}
#preprocess_type : 1 is for stemming, 2 is for lemmatization , 3 is for none
#stop-word removal : 1 is to do stop-word removal , 0 is to not do stop word removal
#index : 1 is for tf-idf, 2 is for boolean query(only and is working now)
#tf scheme : 1 is directly taking tf, 2 is 1+log(tf), 3 is log(1+tf)
