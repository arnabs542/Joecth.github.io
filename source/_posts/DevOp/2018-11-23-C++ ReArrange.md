---
layout: post
categories: C++
tag: [] 



---
### 1.  cout of `char*`

```c++
#include <iostream>
const char *str = "hellogogo";

int main(){
  const char *pstr = str;
  cout "The address of pstr is: " << pstr << endl;
}
-------------------------
 "The address of pstr is: hellogogo"
```



### 2. compiled by c or c++

```cpp
#ifdef __cpluscplu
	cout << "cpp";
#else
	print("c");
#endif
```



#### 3. compiled time OP symbol

```cpp
int id[sizeof(unsigned long)];

// Compiled OK, cuz sizeof is COMPILING time symbol, which is determined in compile, regarded as machine-dependent constant.
```



### 4.