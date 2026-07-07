import time

def brew_tea():
    # Code to brew
    start_time = time.time()
    print("Brewing tea...")
    time.sleep(1)
    print("Tea is ready!")  
    end_time = time.time()
    print(f"Tea brewing time: {end_time - start_time} seconds")
    
brew_tea()  