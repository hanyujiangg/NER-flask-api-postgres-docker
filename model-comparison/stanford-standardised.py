import os
os.environ['JAVAHOME'] = '/Library/Java/JavaVirtualMachines/jdk-14.0.1.jdk/Contents/Home'
os.environ['CLASSPATH'] = '/Users/Hanyu/Desktop/stanford-ner-2020-11-17/'
os.environ['STANFORD_MODELS'] = '/Users/Hanyu/Desktop/stanford-ner-2020-11-17/classifiers'

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk import FreqDist

st = StanfordNERTagger('../../stanford-ner-2020-11-17/classifiers/english.muc.7class.distsim.crf.ser.gz',
					   encoding='utf-8')

text = "Meyer Handelman Co. Increases Position in TE Connectivity Ltd. (NYSE:TEL). Meyer Handelman Co. Increases Position in TE Connectivity Ltd. (NYSE:TEL) Posted by Tammy Falkenburg on Feb 10th, 2021 Tweet\nMeyer Handelman Co. grew its position in shares of TE Connectivity Ltd. (NYSE:TEL) by 2.4% during the fourth quarter, according to its most recent Form 13F filing with the Securities & Exchange Commission. The institutional investor owned 132,718 shares of the electronics maker\u2019s stock after purchasing an additional 3,060 shares during the period. Meyer Handelman Co.\u2019s holdings in TE Connectivity were worth $16,067,000 as of its most recent SEC filing.\nSeveral other institutional investors and hedge funds have also recently added to or reduced their stakes in the company. Perigon Wealth Management LLC acquired a new stake in shares of TE Connectivity in the fourth quarter valued at $31,000. Prospera Financial Services Inc acquired a new position in TE Connectivity during the 3rd quarter worth about $33,000. JJJ Advisors Inc. boosted its holdings in TE Connectivity by 527.3% during the 4th quarter. JJJ Advisors Inc. now owns 276 shares of the electronics maker\u2019s stock valued at $33,000 after acquiring an additional 232 shares during the period. CX Institutional grew its position in TE Connectivity by 59.5% in the 3rd quarter. CX Institutional now owns 362 shares of the electronics maker\u2019s stock valued at $35,000 after acquiring an additional 135 shares in the last quarter. Finally, NEXT Financial Group Inc purchased a new stake in TE Connectivity during the third quarter worth about $43,000. Institutional investors and hedge funds own 91.35% of the company\u2019s stock. Get TE Connectivity alerts:\nSeveral research firms have recently commented on TEL. Robert W. Baird reissued an \u201coutperform\u201d rating and issued a $118.00 price objective on shares of TE Connectivity in a research note on Monday, October 19th. Morgan Stanley raised their price target on shares of TE Connectivity from $121.00 to $127.00 and gave the company an \u201cequal weight\u201d rating in a research report on Thursday, January 28th. Jefferies Financial Group upped their price objective on TE Connectivity from $107.00 to $126.00 and gave the stock a \u201cbuy\u201d rating in a research report on Thursday, October 15th. TheStreet upgraded TE Connectivity from a \u201cc\u201d rating to a \u201cb\u201d rating in a research note on Wednesday, October 28th. Finally, UBS Group boosted their target price on TE Connectivity from $135.00 to $150.00 and gave the stock a \u201cbuy\u201d rating in a research note on Thursday, January 28th. Four research analysts have rated the stock with a hold rating and ten have given a buy rating to the company\u2019s stock. The company currently has an average rating of \u201cBuy\u201d and an average target price of $111.79. In other TE Connectivity news, Director Terrence R. Curtin sold 70,250 shares of the company\u2019s stock in a transaction on Thursday, February 4th. The shares were sold at an average price of $127.75, for a total value of $8,974,437.50. Following the completion of the transaction, the director now owns 125,219 shares in the company, valued at $15,996,727.25. The transaction was disclosed in a legal filing with the Securities & Exchange Commission, which is accessible through this hyperlink . Also, SVP Mario Calastri sold 48,387 shares of the firm\u2019s stock in a transaction dated Tuesday, November 24th. The stock was sold at an average price of $115.52, for a total value of $5,589,666.24. In the last three months, insiders have sold 173,688 shares of company stock worth $21,029,106. 0.80% of the stock is owned by corporate insiders.\nNYSE TEL traded down $0.69 during trading on Wednesday, reaching $128.10. 39,890 shares of the company\u2019s stock were exchanged, compared to its average volume of 2,040,664. The company has a 50 day moving average price of $125.15 and a two-hundred day moving average price of $108.41. The stock has a market cap of $42.39 billion, a P/E ratio of -178.87, a price-to-earnings-growth ratio of 2.35 and a beta of 1.41. TE Connectivity Ltd. has a 1 year low of $48.62 and a 1 year high of $131.97. The company has a debt-to-equity ratio of 0.37, a quick ratio of 1.04 and a current ratio of 1.57.\nTE Connectivity (NYSE:TEL) last issued its earnings results on Tuesday, January 26th. The electronics maker reported $1.47 earnings per share for the quarter, topping the consensus estimate of $1.29 by $0.18. The business had revenue of $3.52 billion for the quarter, compared to analyst estimates of $3.26 billion. TE Connectivity had a positive return on equity of 14.86% and a negative net margin of 1.98%. The business\u2019s quarterly revenue was up 11.2% on a year-over-year basis. During the same quarter last year, the company earned $1.21 EPS. Research analysts forecast that TE Connectivity Ltd. will post 5.3 EPS for the current fiscal year.\nThe business also recently disclosed a quarterly dividend, which will be paid on Friday, March 5th. Shareholders of record on Friday, February 19th will be issued a dividend of $0.48 per share. The ex-dividend date is Thursday, February 18th. This represents a $1.92 dividend on an annualized basis and a yield of 1.50%. TE Connectivity\u2019s payout ratio is currently 45.07%.\nAbout TE Connectivity\nTE Connectivity Ltd., together with its subsidiaries, manufactures and sells connectivity and sensor solutions in Europe, the Middle East, Africa, the Asia\u00c2-Pacific, and the Americas. The company operates through three segments: Transportation Solutions, Industrial Solutions, and Communications Solutions.\nSee Also: Holder of Record\nWant to see what other hedge funds are holding TEL? Visit HoldingsChannel.com to get the latest 13F filings and insider trades for TE Connectivity Ltd. (NYSE:TEL). Receive News & Ratings for TE Connectivity Daily - Enter your email address below to receive a concise daily summary of the latest news and analysts' ratings for TE Connectivity and related companies with MarketBeat.com's FREE daily email newsletter ."
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)


def stanford_to_spacy_format(text):
    pre_tag = "O"
    output = []
    curr = []
    curr_word =''
    for word, tag in text:
        if tag != "O":
            if tag == pre_tag: # entity continuing...
                curr_word += word
                curr_word += ' '
            else: # beginning of new entity 
                if curr_word != '': # from previous diff entity 
                    curr = [curr_word[:-1],pre_tag]
                    output.append(curr)
                    curr = []
                    curr_word = word
                else: # from O 
                    curr_word += word 
                    curr_word += ' '
        else: # end of entity or continuing O
            if curr_word != '':
                curr = [curr_word[:-1],pre_tag]
                output.append(curr)
                curr = []
                curr_word = ''
        pre_tag = tag 
    return output


concatenated_ent = stanford_to_spacy_format(classified_text)
output = []
curr = ''
for ele in concatenated_ent:
    curr = ele[0]+'-'+ele[1]
    output.append(curr)

fdist = FreqDist(output)
for ele in fdist.most_common():
    print(ele)