import sys, pdb
import csv
from random import shuffle

if __name__ == '__main__':
    answers_csv = open(sys.argv[1])
    answers_reader = csv.reader(answers_csv, delimiter='\t')
    # existing_informal_sentences_reader = csv.reader(open(sys.argv[3]), delimiter=',')
    # existing_informal_sentences = []
    # i = 0
    # for row in existing_informal_sentences_reader:
    #     if i == 0:
    #         i += 1
    #         continue
    #     s1, s2, s3, s4, s5 = row
    #     s5 = s5.strip('\n')
    #     existing_informal_sentences += [s1, s2, s3, s4, s5]
    informal_sentences_file = open(sys.argv[2], 'w')
    informal_sentences_file.write("sentence_1,sentence_2,sentence_3,sentence_4,sentence_5\n")
    scores = []
    i = 0
    informal = []
    for row in answers_reader:
        # avg_score, scores, id, sentence = row
        if len(row) == 3:
            avg_score, scores, sentence = row
        elif len(row) == 2:
            avg_score, sentence = row
        if 'http' in sentence:
            continue
        sentence = sentence.strip()
        # if sentence in existing_informal_sentences:
            # continue
        if len(sentence.split()) < 5 or len(sentence.split()) > 20:
            continue
        if float(avg_score) <= -1.0:
            informal.append(sentence)
    shuffle(informal)
    print len(informal)
    for i in range(len(informal)/5+1):
        line = ''
        if i*5+4 >= len(informal):
                break
        for j in range(5):
            try:
                line += '\"' + informal[i*5+j].decode('utf-8', 'ignore') + '\",'
            except:
                line += '\"' + informal[i*5+j].encode('utf-8') + '\",'
        line = line[:-1] #to remove last comma
        if line[0] == '<':
            line = line[1:]
        if line[-1] == '>':
            line = line [:-1]
        informal_sentences_file.write(line.encode('utf-8')+'\n')
            