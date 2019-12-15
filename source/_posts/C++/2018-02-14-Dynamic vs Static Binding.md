---
layout: post
categories: C++
tag: [] 



---

Ref: http://notes.maxwi.com/3516/08/19/static-dynamic-binding/

- 静态类型：就是对象声明时采用的类型，一旦确定就无法更改，编译期已经确定
- 动态类型：通常是指一个指针或引用在调用时所指向的类型，可以理解为赋值号右侧对象的类型（当然采用直接赋值就是括号中的对象的类型），可以在运行时更改，在运行期决定
- 静态绑定（static binding）：又名前期绑定（early binding），绑定的是对象的静态类型，发生在编译期，即程序编译完成后就已经确定
- 动态绑定（dynamic binding）：又名后期绑定（late binding），绑定的是对象的动态类型，发生在运行期，即在运行期由当前的动态类型决定所需要调用的函数或属性

可以简单理解为，通常我们定义的非虚函数都是静态绑定，即静态类型与动态类型都指同一种类型，在编译期就已经确定，那么运行时调用的函数也就是相应类型对象的函数。
而虚函数可以发生动态绑定，即在运行时，根据指针或引用所指对象的类型来决定调用相应的虚函数。如当定义父类的指针，指向派生类的对象时，该指针的动态类型与静态类型就不一致,
动态类型即派生类，静态类型为父类，那么在使用此指针在运行时调用虚函数时会首先调用动态类型对象（即派生类对象）的虚函数，如果动态类型中没有重写（override）该虚函数，
则调用的还是基类中的虚函数。
举例说明：
所有的讲解都是注释中，请认真阅读每一句注释

```c++

#include <iostream>

class A {
public:
    void func(void)  //普通的非虚函数，只能静态绑定
    {
        std::cout << "A::func" << std::endl;
    }
    virtual void vfunc1()   //虚函数，可以在运行时，根据动态类型不同而发生动态绑定
    {
        std::cout << "A::vfunc1" << std::endl;
    }
    virtual void vfunc2(int i = 2)
    {
        std::cout << "A::vfunc2: " << i << std::endl;
    }
};

class B : public A {
public:
    void func(void)
    {
        std::cout << "B::func" << std::endl;
    }
    virtual void vfunc1()
    {
        std::cout << "B::vfunc1" << std::endl;
    }
    virtual void vfunc2(int i = 5)  //注意B改变了继承而来的虚函数的默认参数
    {
        std::cout << "B::vfunc2: " << i << std::endl;
    }
};

class C : public B {  //注意C继承自B而不是A
};

int main(void)
{
    B* pb = new B();  //pb的静态类型即是它声明的类型B，动态类型是它指向的类型B，即动态类型与静态类型一致
    C* pc = new C(); //pc的静态类型与动态类型一致
    A* pa = pc;   //pa的静态类型是A，动态类型是C
    pa = pb; //将pa的动态类型改为B
    B *pbnull = nullptr;  //定义B指向空指针，它将在编译期发生静态绑定
    pa->func();  //A::func，虽然pa的静态类型与动态类型不一样，但func是不是虚函数，只有在通过指针或引用调用虚函数时，才会有运行时发生动态绑定，即pa优先调用其动态类型中的虚函数，所以此时pa只能调用它自己的func
    pa->vfunc1(); //B::vfunc1，此时pa发生了动态绑定，即调用它动态类型B的虚函数vfunc1
    pb->func(); //B::func，pb的func将隐藏继承自A中的函数func，所有非虚函数的调用都由静态类型决定，即编译期就已经确定了
    pb->vfunc2(); //B::vfunc2:5，pb正常通过静态绑定调用自己的函数vfunc2
    pa->vfunc2(); //B::vfunc2:2，发现pa此时动态绑定调用的是类型B的成员函数，但形参去是A自己的形参，因为C++为了执行效率，缺省参数值都是静态绑定的，所以永远不要重新定义一个继承而来的virtual函数的缺省参数值
    pc->func(); //B::func，pc正常的静态绑定，调用继承自B的函数func
    pa = pc;  //将pa的动态类型改为pc
    pa->vfunc1();  //B::vfunc1，此时pa实际上发生了动态绑定，被动态绑定到pc，将调用其动态类型C中的虚函数，但由于C中没有重写继承自B的虚函数，所以只能调用其父类B中的虚函数，注意不是A中的
    pbnull->func();  //B::func，虽然pbnull此时指向的是空指针，但其静态绑定是在编译期确定的，也就是说编译完成之后，pbnull就已经存在pbnull->func()的调用了。
    // pbnull->vfunc1(); //编译没有问题，但将发生运行时错误，linux下运行报错为Segmentation fault。因为在运行时发生动态绑定时，pbnull是指向空指针的，显然空指针不属于任何类型，pbnull也就无法正常绑定。之所以编译器无法检查到这类问题应该就是动态导致用户可以随时将pbnull绑定到一个其派生类的对象上

    //释放动态内存
    delete pb;
    delete pc;

    return 0;
}

```

上面的注释中已经讲解的非常清楚了，最后两句指向空指针的类对象也可以调用其静态绑定的函数需要特别注意，这是一种极不推荐的做法

注意

- 永远不要重新定义继承而来的非虚函数，这样的函数由对象声明时的静太类型确定，没有多态性，将给程序留下不可预知的隐患
- 永远不要重新定义一个继承而来的虚函数的缺省参数值，因为缺省参数值都是静态绑定的。
- 接口基类不应该有非虚函数，即全部使用纯虚函数