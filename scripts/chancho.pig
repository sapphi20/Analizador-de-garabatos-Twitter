-- Este script agarra los batches de los tres países y corre un proceso UDF que saca los n gramas

REGISTER 'ngram-udf.jar';

raw_chile = LOAD 'hdfs://cm:9000/uhadoop2018/benjujolibre/chilean.tsv' USING PigStorage('\t') AS (id, user, timestamp, tweet, place);

raw_peru = LOAD 'hdfs://cm:9000/uhadoop2018/benjujolibre/peruvian.tsv' USING PigStorage('\t') AS (id, user, timestamp, tweet, place);

raw_argentina = LOAD 'hdfs://cm:9000/uhadoop2018/benjujolibre/argentinian.tsv' USING PigStorage('\t') AS (id, user, timestamp, tweet, place);

chile = FOREACH raw_chile GENERATE LOWER(tweet) as tweet:chararray;

argentina = FOREACH raw_argentina GENERATE LOWER(tweet) as tweet:chararray;
peru = FOREACH raw_peru GENERATE LOWER(tweet) as tweet:chararray;

tokens_c = FOREACH chile GENERATE flatten(org.apache.pig.tutorial.NGramGenerator(tweet)) as ngram;

tokens_a = FOREACH argentina GENERATE flatten(org.apache.pig.tutorial.NGramGenerator(tweet)) as ngram;

tokens_p = FOREACH peru GENERATE flatten(org.apache.pig.tutorial.NGramGenerator(tweet)) as ngram;

-- Group and count the ngrams
tokens_grouped_c = group tokens_c by ngram;
token_counts_c = foreach tokens_grouped_c generate group as token:chararray, COUNT(tokens_c) as count:long;

tokens_grouped_a = group tokens_a by ngram;
token_counts_a = foreach tokens_grouped_a generate group as token:chararray, COUNT(tokens_a) as count:long;

tokens_grouped_p = group tokens_p by ngram;
token_counts_p = foreach tokens_grouped_p generate group as token:chararray, COUNT(tokens_p) as count:long;


-- Sort and limit the ngrams
sorted_tokens_c = order token_counts_c by count desc;
top_100_tokens_c = limit sorted_tokens_c 100;

sorted_tokens_a = order token_counts_a by count desc;
top_100_tokens_a = limit sorted_tokens_a 100;

sorted_tokens_p = order token_counts_p by count desc;
top_100_tokens_p = limit sorted_tokens_p 100;

-- Store the output
store top_100_tokens_c into '/uhadoop2018/benjujolibre/chile2gram/' using PigStorage();

store top_100_tokens_a into '/uhadoop2018/benjujolibre/argentina2gram/' using PigStorage();

store top_100_tokens_p into '/uhadoop2018/benjujolibre/peru2gram/' using PigStorage();

