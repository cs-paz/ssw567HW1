def classify_triangle(a, b, c):
    if(a == b and a == c):
        return "equilateral"
    elif(a == b or c ==  b or a == c):
        return "isosceles"
    elif(pow(a, 2) + pow(b, 2) == pow(c, 2)):
        return "right"
    else:
        return "scalene"

def classify_triangle_with_errors(a, b, c):
    if(a == b and a == c):
        return "this will error"
    elif(a == b or c ==  b or a == c):
        return "this will error"
    elif(pow(a, 2) + pow(b, 2) == pow(c, 2)):
        return "this will error"
    else:
        return "this will error"

def test_classify_triangle_1():
    assert classify_triangle(1, 1, 1) == "equilateral"

def test_classify_triangle_2():
    assert classify_triangle(2, 2, 2) == "equilateral"

def test_classify_triangle_3():
    assert classify_triangle(3, 3, 3) == "equilateral"

def test_classify_triangle_4():
    assert classify_triangle(3, 2, 3) == "isosceles"

def test_classify_triangle_5():
    assert classify_triangle(5, 9, 5) == "isosceles"

def test_classify_triangle_6():
    assert classify_triangle(1, 6, 1) == "isosceles"

def test_classify_triangle_7():
    assert classify_triangle(3, 4, 5) == "right"

def test_classify_triangle_8():
    assert classify_triangle(5, 12, 13) == "right"

def test_classify_triangle_9():
    assert classify_triangle(8, 15, 17) == "right"

def test_classify_triangle_10():
    assert classify_triangle(1, 2, 3) == "scalene"

def test_classify_triangle_11():
    assert classify_triangle(6, 7, 8) == "scalene"

def test_classify_triangle_12():
    assert classify_triangle(5, 4, 3) == "scalene"

def test_classify_triangle_1_with_errors():
    assert classify_triangle_with_errors(1, 1, 1) == "equilateral"

def test_classify_triangle_4_with_errors():
    assert classify_triangle_with_errors(3, 2, 3) == "isosceles"

def test_classify_triangle_7_with_errors():
    assert classify_triangle_with_errors(3, 4, 5) == "right"

def test_classify_triangle_12_with_errors():
    assert classify_triangle_with_errors(5, 4, 3) == "scalene"


def main():
    test_classify_triangle_1()
    test_classify_triangle_2()
    test_classify_triangle_3()
    test_classify_triangle_4()
    test_classify_triangle_5()
    test_classify_triangle_6()
    test_classify_triangle_7()
    test_classify_triangle_8()
    test_classify_triangle_9()
    test_classify_triangle_10()
    test_classify_triangle_11()
    test_classify_triangle_12()
    test_classify_triangle_1_with_errors()
    test_classify_triangle_4_with_errors()
    test_classify_triangle_7_with_errors()
    test_classify_triangle_12_with_errors()

if __name__ == "__main__":
    main()