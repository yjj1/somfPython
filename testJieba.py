# -*- coding:'utf8' -*-
#encoding=utf-8
import jieba

if __name__ == '__main__':
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式