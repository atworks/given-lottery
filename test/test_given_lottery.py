import sys
import os

sys.path.append(os.path.abspath(".."))

import given_lottery

def test_引数が無くても動くが負が返る():
    assert given_lottery.draw_lots() == -1

def test_引数があれば何か返す():
    result = given_lottery.draw_lots("a,b,c")
    print(result)
    assert len(result) > 0

def test_100回くらいやる():
    data = 'a,b,c'
    member = data.split(',')
    counter = 0
    data_list = dict(zip(member,[0]*len(member)))

    for i in range(100):
        result = given_lottery.draw_lots(data)
        data_list[result] += 1
        counter += 1
    
    for m in member:
        print(data_list[m])

    assert counter > 0

def test_10000回くらいやる():
    data = 'a,b,c'
    member = data.split(',')
    counter = 0
    data_list = dict(zip(member,[0]*len(member)))

    for i in range(10000):
        result = given_lottery.draw_lots(data)
        data_list[result] += 1
        counter += 1
    
    for m in member:
        print(data_list[m])

    assert counter > 0


