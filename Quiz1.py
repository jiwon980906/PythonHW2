file = open("article.txt", "w")
file.write('Senior officials at Ethiopia’s Ministry of Mines and Petroleum say the government is set to rescind an agreement with a US-based self-described energy firm after an investigation by Quartz Africa revealed the company had no petroleum industry expertise or technical credentials. After the story was published, one local social media user drove to the company’s listed address in Virginia, and found empty office space, with no sign of an extraction company in the area. When probed about the agreement earlier this year, Ethiopia’s minister of Mines Takele Uma told Quartz Africa he was unaware of GreenComm’s existence, saying he had “no clue.” His predecessor, Samuel Urkato, who has since gone on to become Ethiopia’s minister of Science and Higher Education, acknowledged the existence of the deal when reached by phone, but refused to speak any further, hanging up and ending the call. Zecharias Zelalem brings you the latest on the Ethiopian oil scandal.')
file.close()

file = open("article.txt", "r")
text = file.read() 
 
word_dic = {}

with open("article.txt",'r') as fr:
    for line in fr:
        for word in line.lower().strip().split():
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1

word_list = sorted(word_dic.items(), key = lambda x : x[1], reverse = True)
print(word_list[:3])
