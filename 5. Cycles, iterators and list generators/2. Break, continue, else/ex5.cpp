#include <iostream>

class Operator {
    long a {0}, b {0}, c {0};

    Operator(Operator& op) = default;
public:
    Operator() = default;

    Operator* create_copy() 
    {
        Operator * ptr_obj = new Operator(*this);
        return ptr_obj;
    }
};

int main()
{
    Operator op1;
    Operator *ptr_op = new Operator();

    Operator op2(op1);
    Operator *ptr_op2 = new Operator(op1);

    Operator *op3 = op1.create_copy();
    delete op3;


    return 0;
}