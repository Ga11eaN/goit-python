import redis
from random import randint

def r_set(key, value):
    global cache_counter
    global counter
    counter += 1
    r.set(key, value)
    cache_counter[key] = counter
    check_len(cache_counter)
    
def r_get(key):
    global cache_counter
    global counter
    if r.get(key):
        counter += 1
        value = r.get(key)
        cache_counter[key] = counter
        return value
    else:
        return None

def check_len(cache_counter):
    global MAX_LEN
    if len(cache_counter) > MAX_LEN:
        min_key = min(cache_counter.items(), key=lambda x: x[1])[0]
        cache_counter.pop(min_key)
        r.delete(min_key) 

def save_cache():
    global cache_counter
    r.delete('cache_counter')
    for key, value in cache_counter.items():
        r.hset('cache_counter', key, value)
        
def load_cache():
    global cache_counter
    cache = r.hgetall('cache_counter')
    for key, value in cache.items():
        cache_counter[key.decode()] = int(value)

def main():
    global cache_counter
    global counter
    global MAX_LEN
    counter = 0
    MAX_LEN = 20
    cache_counter = {}
    TEST_VALUE = 'qwertyuiopadsfhjgcxvbnb12354756'
    
    load_cache()
    
    for i in TEST_VALUE:
        r_set(i,i)
        
    for i in range(20):
        rand_int = randint(0, len(TEST_VALUE)-1)
        test_value = r_get(rand_int)
        
    print(r.keys())

    save_cache()

r = redis.Redis(
    host='localhost',
    port=6379, 
)

if __name__ == '__main__':
    main()