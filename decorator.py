import time

def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f"Function execution time: {end_time - start_time} seconds")
    return enhanced_fn


#@timer_dec    
def brew_tea():
    # Code to brew
    print("Brewing tea...")
    time.sleep(1)
    print("Tea is ready!")    
    
 dec_brew_tea = timer_dec(brew_tea) 
 dec_brew_tea()

#brew_tea()