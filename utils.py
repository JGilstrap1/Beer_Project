import threading

class ThreadSafeVar(object):
    
    def __init__(self, value=None):
        self.lock = threading.Lock()
        self.value = value
        
    def set(self, value):
        with self.lock:
            self.value = value
            
    def get(self):
        var = None
        with self.lock:
            var = self.value
        return var