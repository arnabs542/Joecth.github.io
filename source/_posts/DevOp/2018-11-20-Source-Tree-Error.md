---
layout: post
categories: DevOps
---
Error: The following untracked working tree files would be overwritten by checkout:

Sol:

​    開啟SourceTree通過命令列，進入本地版本倉庫目錄下，直接執行

```bash
git clean -d -fx
```

即可。可能很多人都不明白-d，-fx到底是啥意思，其實git clean -d -fx表示：刪除 一些 沒有 git add 的 檔案；

​    git clean 引數 

​    -n 顯示將要刪除的檔案和目錄；

​    -x -----刪除忽略檔案已經對git來說不識別的檔案

​    -d -----刪除未被新增到git的路徑中的檔案

​    -f -----強制執行

​    git clean -n

​    git clean -df

​    git clean -f