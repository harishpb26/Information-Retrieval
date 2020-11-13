import query
from Elasticsearch.ES import search_snippet
import json



def metrics(query_string):
  """
  A helper function to obtain performance metrics for the search engine for a particular query.
  Uses the results from elasticsearch as the true labels
  """
  results = query.main(query_string)
  es_results = search_snippet(query_string)
  es_doc_ids = {x['_source']['id'] for x in[i for i in es_results['hits']['hits']]}
  doc_ids = {x['id'] for x in [i for i in results['hits']]}

  tp = len(doc_ids.intersection(es_doc_ids))
  fp = len(doc_ids) - tp
  fn = len(es_doc_ids) - tp
  tn = query.index.ndocs - tp - fp - fn
  return (tp, fp, fn, tn)
if __name__ == "__main__":
  print(metrics("brazil's government was defending its plan to build dozens of huge hydro-electric dams"))