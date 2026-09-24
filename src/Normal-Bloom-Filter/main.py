from bloomFilter import BloomFilter
import random
import sys

def syncTest(elementsToInsert):
    bloomFilter = BloomFilter(100000, 0.1)
    actualStore = set()
    falsePositiveCount = 0
    
    for i in range(elementsToInsert):
        randomNumber = str(random.random() * 1000000)

        if bloomFilter.checkIsExits(randomNumber) :
            if randomNumber not in actualStore :
                falsePositiveCount += 1
            continue
        bloomFilter.addElement(randomNumber)
        actualStore.add(randomNumber)
        # result = bloomFilter.addElement(str(randomNumber))
        # if result:
        #     if randomNumber not in actualStore :
        #         falsePositiveCount += 1
        #         continue
        #     actualStore.add(str(randomNumber))
        
    print("False Positive Count: " + str(falsePositiveCount))
    print("Percentage: " + str(round(falsePositiveCount/elementsToInsert * 100,4)))


def asyncTest (elementsToInsert) :
    pass
    

if __name__ == "__main__":
    if not len(sys.argv) == 3 :
        raise Exception("Usage: python3 main.py <num_elements> <mode>")
    
    elementsToInsert = int(sys.argv[1])
    mode = sys.argv[2]

    if mode == "sync":
        syncTest(elementsToInsert)
    elif mode == "async":
        asyncTest(elementsToInsert)
    else:
        raise Exception("Invalid mode. Use 'sync' or 'async'")
    