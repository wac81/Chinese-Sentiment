__author__ = 'anchengwu'
#coding=utf-8

import sys
sys.path.append("../../Preprocessing module/")


import pos_neg_senti_dict_feature as pn
import textprocessing as tp

# # Load dataset
# review = tp.get_excel_data("../Machine learning features/seniment review set/pos_review.xlsx", 1, 1, "data")
# #test all dataset
# for i in pn.all_review_sentiment_score(pn.sentence_sentiment_score(review)):
# 	print(i)



#test single dataset
print(pn.single_review_sentiment_score('自然灾害自不必说，百年难遇的金融危机汹涌袭来，全球经济受到重创，艺术品市场巨幅下跌，岌岌可危'))


