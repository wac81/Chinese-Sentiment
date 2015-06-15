__author__ = 'anchengwu'
#coding=utf-8

import sys
sys.path.append("../../../Preprocessing module")

import pos_neg_senti_dict_feature as pn
import textprocessing as tp

# Load dataset
review = tp.get_excel_data("../Machine learning features/seniment review set/pos_review.xlsx", 1, 1, "data")

#test single dataset
print pn.single_review_sentiment_score('买过散装的粽子才来买礼盒的，礼盒很大气，比超市买的100多的还要好，配置也不错，肉的素的都有，刚煮了个蛋黄粽子很不错，米好蛋黄也黄很香，老板态度很好，还想买一份～'.decode('utf8'))

#test all dataset
for i in pn.all_review_sentiment_score(pn.sentence_sentiment_score(review)):
	print i

