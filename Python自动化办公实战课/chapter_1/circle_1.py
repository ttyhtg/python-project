from pathlib import Path, PurePath

# 指定要合并excel的路径
src_path = '/Users/edz/Desktop/文章1/调查问卷'

# 取得该目录下所有的xlsx格式文件
p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]