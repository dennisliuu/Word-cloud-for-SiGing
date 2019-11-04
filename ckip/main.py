text = open('SiGing.txt', 'r',encoding= 'UTF-8-sig').read()
# print(text)

from ckiptagger import data_utils, construct_dictionary, WS, POS, NER

# data_utils.download_data_gdown("./") #Download data first
ws = WS("./data")
ws_results = ws([text])
# print(ws_results)

f = open("tokenize.txt", "w+")
f.write("%s" % ws_results[0])
