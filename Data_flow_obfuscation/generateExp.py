# -*- coding = 'utf-8 -*-

import argparse

from exp_generate import Config,Generator
from answer import expression_result,check_answer
from postProcessing import postProcessing

class generateExp:
    def __init__(self, _target):
        self.target = _target
        self.expNum = 5000
        self.expFile = "Exercises.txt"
        self.answerFile = "Answer.txt"

    def main(self):
        """
        主函数
        """
        '''
        parser = argparse.ArgumentParser(description="***** this is auto-generate-expression *****")
        parser.add_argument("-n", metavar = "--number", dest = "expnum_arg", help = "Generate a given number of expressions" )
        parser.add_argument("-r", metavar = "--range", dest = "range_arg", help = "Specify the range of operands")
        parser.add_argument("-e", metavar = "--exercise file", dest = "exercise_arg", help = "Given four arithmetic problem files")
        parser.add_argument("-a", metavar = "--answer file", dest = "answer_arg", help = "Given four arithmetic problem answer files")
        args = parser.parse_args()
        '''
    
        try:
            with open(self.expFile, "w+", encoding = "utf-8") as f:
                f.truncate()
                f.close()
            with open(self.answerFile, "w+", encoding = "utf-8") as f:
                f.truncate()
                f.close()
            print("Clear existing expressions....done.")
        except:
            print("No need to clear existing expressions.")
        
        #判断生成的表达式的数目
        if self.expNum:
            #表达式的范围
            if self.target:
                config = Config(exp_num=int(self.expNum),num_range=int(self.target))
            else:
                config = Config(exp_num=int(self.expNum))
            print("** An arithmetic expression replacing literal (" + str(self.target) + ") is being generated. **")
            generator = Generator()
            res_list = generator.generate(config)
            generator.normalize_exp(res_list)
            expression_result(res_list)
            print('** Generation is complete. **')
        #后期处理表达式的值
        #print(args.exercise_arg, args.answer_arg)
        pp = postProcessing(self.expFile, self.answerFile, self.target)
        return pp.run()
    
    '''
    #练习题答案的文件判断
    if args.exercise_arg:
        if args.answer_arg:
            check_answer(args.exercise_arg, args.answer_arg)
        else:
            print('please give an answer files')
            exit(0)
    '''

if __name__ == '__main__':
    ge = generateExp(5000)
    print(ge.main())