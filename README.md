# Chinese-Sentiment
A Chinese sentiment analyze lib with Python

#simple to use：
##example

##first,you can import python lib like this:
import pos_neg_senti_dict_feature as pn
import textprocessing as tp

##for single sentence

print
pn.single_review_sentiment_score('买过散装的粽子才来买礼盒的，礼盒很大气，比超市买的100多的还要好，配置也不
错，肉的素的都有，刚煮了个蛋黄粽子很不错，米好蛋黄也黄很香，老板态度很好，还想买一份～'.decode('utf8'))


##for all dataset
for i in pn.all_review_sentiment_score(pn.sentence_sentiment_score(review)):
	print i
