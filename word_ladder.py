class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        wordset =set(wordList)
        if endWord not in wordList:
            return 0
        l = len(beginWord)
        all_combination ={}
        for word  in wordList:
            for i in range (l):
                combination =word[:i]+"*"+word[i+1:]
                if combination not in all_combination:
                    all_combination[combination] =[]
                all_combination[combination].append(word)

        queue =[(beginWord,1)]
        head =0
        visited =set()
        visited.add(beginWord)
        while head <len (queue):
            current_word  ,level = queue[head] 
            head +=1

            for i in range (l):
                combination = current_word[:i] + "*" + current_word[i+1:]
                if combination in all_combination:
                    for next_word in all_combination[combination]:
                        if next_word == endWord:
                            return level +1
                        if next_word not in  visited:
                            visited.add(next_word)
                            queue.append((next_word ,level+1))
                    all_combination[combination] =[]
        return 0










            
