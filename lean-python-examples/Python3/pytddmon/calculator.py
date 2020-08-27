
class calculator(object):

    def __init__(self,title):
        self.title=title
        return

    def runTest(self,a,op,b):
        self.result, self.msg = self.calc(a,op,b)
        return self.result, self.msg
        

    def calc(self, a, op, b):

        if a is None or b is None or op is None:
            return None, 'Ending'
            
        try:
            if op=='+':
                result=a+b
            elif op=='-':
                result=a-b
            elif op=='/':
                result=a/b
            elif op=='*':
                result=a*b
            else:
                return None,'Operator must one of be +-/*'
                
        except Exception as e:
            return None,e.__class__.__name__

        return result,str(result)


    def dispose(self):
        return
        

