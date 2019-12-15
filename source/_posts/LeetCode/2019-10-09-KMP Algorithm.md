## KMP Algorithm

### Searching for Patterns

Knuth Morris Pratt Pattern Searching algorithm uses <u>degenerating property[1]</u> of the pattern and improves the worst case bigO(m+n).

Naive: O(n*m)

[1] means pattern having same sub-patterns appearing more than once in the pattern, are considered.

prefix table: for pattern

FOLLOWING is COPIED & RECORDED fr. [https://www.zhihu.com/question/21923021](https://www.zhihu.com/question/21923021) for quickly self-explanatory.

###  PMT -- Partial Match Table![v2-e905ece7e7d8be90afc62fe9595a9b0f_hd](https://tva1.sinaimg.cn/large/006y8mN6ly1g9930c1shgj30k007iq38.jpg)

pic ref fr. :[https://www.zhihu.com/question/21923021](https://www.zhihu.com/question/21923021)

As shown in this table, if the pattern to be matched has 8 chars, then PMT should have 8 values accordingly.

For Strtings A and B, and non-empty String S, B is named as prefix of A if **A=BS**.

### KMP

"

好了，解释清楚这个表是什么之后，我们再来看如何使用这个表来加速字符串的查找，以及这样用的道理是什么。如图 1.12 所示，要在主字符串"ababababca"中查找模式字符串"abababca"。如果在 j 处字符不匹配，那么由于前边所说的模式字符串 PMT 的性质，主字符串中 i 指针之前的 PMT[j −1] 位就一定与模式字符串的第 0 位至第 PMT[j−1] 位是相同的。这是因为主字符串在 i 位失配，也就意味着主字符串从 i−j 到 i 这一段是与模式字符串的 0 到 j 这一段是完全相同的。而我们上面也解释了，模式字符串从 0 到 j−1 ，在这个例子中就是”ababab”，其前缀集合与后缀集合的交集的最长元素为”abab”， 长度为4。所以就可以断言，主字符串中i指针之前的 4 位一定与模式字符串的第0位至第 4 位是相同的，即长度为 4 的后缀与前缀相同。这样一来，我们就可以将这些字符段的比较省略掉。具体的做法是，保持i指针不动，然后将j指针指向模式字符串的PMT[j −1]位即可。

简言之，以图中的例子来说，在 i 处失配，那么主字符串和模式字符串的前边6位就是相同的。又因为模式字符串的前6位，它的前4位前缀和后4位后缀是相同的，所以我们推知主字符串i之前的4位和模式字符串开头的4位是相同的。就是图中的灰色部分。那这部分就不用再比较了。

"

![v2-03a0d005badd0b8e7116d8d07947681c_hd](https://tva1.sinaimg.cn/large/006y8mN6ly1g99367yuxoj30k00a4wes.jpg)



有了上面的思路，我们就可以使用PMT加速字符串的查找了。我们看到如果是在 j 位 失配，那么影响 j 指针回溯的位置的其实是第 j −1 位的 PMT 值，所以为了编程的方便， 我们不直接使用PMT数组，而是将PMT数组向后偏移一位。我们把新得到的这个数组称为next数组。下面给出根据next数组进行字符串匹配加速的字符串匹配程序。其中要注意的一个技巧是，在把PMT进行向右偏移时，第0位的值，我们将其设成了-1，这只是为了编程的方便，并没有其他的意义。在本节的例子中，next数组如下表所示。

![img](https://tva1.sinaimg.cn/large/006y8mN6ly1g9936oald5j30k009g3yq.jpg)![img](https://tva1.sinaimg.cn/large/006y8mN6ly1g9936es8ztj30k009gaag.jpg)

```c++
int KMP(char * t, char * p) 
{
	int i = 0; 
	int j = 0;

	while (i < strlen(t) && j < strlen(p))
	{
		if (j == -1 || t[i] == p[j]) 
		{
			i++;
           		j++;
		}
	 	else 
           		j = next[j];
    	}

    if (j == strlen(p))
       return i - j;
    else 
       return -1;
}

作者：海纳
链接：https://www.zhihu.com/question/21923021/answer/281346746
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```



作者：海纳







![img](https://pic1.zhimg.com/50/v2-645f3ec49836d3c680869403e74f7934_hd.jpg)![img](https://pic1.zhimg.com/80/v2-645f3ec49836d3c680869403e74f7934_hd.jpg)

![img](https://pic3.zhimg.com/50/v2-06477b79eadce2d7d22b4410b0d49aba_hd.jpg)![img](https://pic3.zhimg.com/80/v2-06477b79eadce2d7d22b4410b0d49aba_hd.jpg)

![img](https://pic1.zhimg.com/50/v2-8a1a205df5cad7ab2f07498484a54a89_hd.jpg)![img](https://pic1.zhimg.com/80/v2-8a1a205df5cad7ab2f07498484a54a89_hd.jpg)

![img](https://pic2.zhimg.com/50/v2-f2b50c15e7744a7b358154610204cc62_hd.jpg)![img](https://pic2.zhimg.com/80/v2-f2b50c15e7744a7b358154610204cc62_hd.jpg)

![img](https://pic2.zhimg.com/50/v2-bd42e34a9266717b63706087a81092ac_hd.jpg)![img](https://pic2.zhimg.com/80/v2-bd42e34a9266717b63706087a81092ac_hd.jpg)

求next数组值的程序如下所示：

```c++
void getNext(char * p, int * next)
{
	next[0] = -1;
	int i = 0, j = -1;

	while (i < strlen(p))
	{
		if (j == -1 || p[i] == p[j])
		{
			++i;
			++j;
			next[i] = j;
		}	
		else
			j = next[j];
	}
}

作者：海纳
链接：https://www.zhihu.com/question/21923021/answer/281346746
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

