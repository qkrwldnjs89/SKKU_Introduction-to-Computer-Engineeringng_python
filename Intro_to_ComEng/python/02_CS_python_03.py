def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        # 논로컬 시 로컬도 아니고 글로벌도 아닌 변수로 이 함수 내에서 처리
        spam = "nonlocal spam"
    def do_global():
        global spam
        # 글로벌 시 이 함수 내에서 글로벌로 취급
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignmet:", spam)
    # spam 은 test spam(local variable의 변화가 영향을 끼치지 않음)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    # spam 은 nonlocal spam
    do_global()
    print("After global assignment:", spam)
    # spam 은 nonlocal spam(scope_test 라는 함수 안이므로 global은 영향이 없다)

scope_test()
print("In global scope:", spam)
# do_global 의 global spam 이 print된다.
