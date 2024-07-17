# BIT_Course_structure_to_Excel

将北京理工大学的培养方案页转换为excel
由于作者不会写带有认证的爬虫，所以需要手动获取HTML源码

***
## 使用步骤：
1. 下载本项目源码或使用git运行：

`git clone https://github.com/guanosine-diphosphate/BIT_Course_structure_to_Excel.git`

2. 确保已经正确安装~~屁眼通红~~Python，在项目路径下（若第一步使用git，则运行

`cd BIT_Course_structure_to_Excel`

进入路径）运行：

`pip install -r requirements.txt`

3. 进入培养方案页，右键空白处，在右键菜单中点击“查看网页源代码”或类似选项，复制新窗口中的所有内容，在`html.txt`中粘贴
4. 运行main.py,在项目根目录中获得`培养方案.xls`
