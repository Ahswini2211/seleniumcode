import  pytest

def sum(a,b):
    return a+b

@pytest.mark.parametrize("input1,input2,output",
                         [
                             (3,3,6),
                             (4,4,9),
                             (5,5,11)
                         ]
                         )
def test_cal_sum_1(input1,input2,output):
    result = sum(input1,input2)
    assert result == output