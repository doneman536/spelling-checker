import mmh3
import math
from dotenv import load_dotenv
import os

load_dotenv()
# Bloom filter using the normal hash function 
class BloomFilter:

    def __init__(self, size, false_positive):
        seed_start = int(os.getenv("SEED_START"))
        seed_jump = int(os.getenv("SEED_JUMP"))
        self.__hash_count = int(- math.log(false_positive/100) // math.log(2))
        self.__size = size
        self.__hashs_seeds = [seed_start + seed_jump * i for i in range(self.__hash_count)]
        self.__bit_array = [0] * size

    def __calculate_hash(self, element) :
        hash_indexes = []
        count = 0
        for seed in self.__hashs_seeds :
            hash_value = mmh3.hash(element, seed)
            index = hash_value % self.__size
            hash_indexes.append(index)
            count += 1 if self.__bit_array[index] else 0
        return hash_indexes, count 

    def addElement(self, element) :
        hash_indexes, count = self.__calculate_hash(element)
        if count == self.__hash_count :
            return False 
        for index in hash_indexes:
            self.__bit_array[index] = 1
        return True

    def checkIsExits(self, element):
        hash_indexes ,count = self.__calculate_hash(element)
        for index in hash_indexes :
            if self.__bit_array[index] == 0 :
                return False
        return True
        
            







    