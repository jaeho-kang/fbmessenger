import requests
from konlpy.tag import Kkma, Komoran, Hannanum, Twitter, Mecab
import logging

logging.basicConfig(filename='./logs/chatbot.log', level=logging.WARNING)

class commonGate:
	def __init__(self):
		self.tagger = Mecab()

	def reply(self,user_id, msg):
		logging.error("call reply {},{}".format(user_id,msg))
		postags = [] 
		try :
		    list = self.tagger.pos(msg)		    
		    for x in list:
		    	postags.append(x[0]+"/"+x[1])
		except :
			logging.error("except happen ")
			return "error happen"
		logging.error("postag success")
		return " ".join(postags)
