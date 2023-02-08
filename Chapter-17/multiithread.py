import threading
threadObj=threading.Thread(target=print,args=['cats','dogs','mice'],kwargs= {'sep':'&'})
threadObj.start()