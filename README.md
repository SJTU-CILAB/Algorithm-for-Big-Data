# Algorithms for Big Data

《Algorithms for Big Data》（大数据算法）课程的教学资料仓库，收录课件、实验示例、作业代码模板以及论文调研与写作材料。

课程内容按 Lecture 1–22 组织，覆盖 MapReduce 与 Spark、相似性与近邻检索、大规模机器学习、图数据挖掘、推荐系统、时间序列分析和数据流挖掘。当前包含 22 讲课件、36 个 Jupyter Notebook 和 4 份 Chapter 作业代码模板。

## AI 课程助教

<a href="https://wbapp-xdrboti5h2c1km3knhvnz2.app.workbuddy.host/?sharecode=V3MGCTQXIW"><img src="docs/assets/course-ta-icon.svg" alt="大数据算法 AI 课程助教图标" width="88" align="right"></a>

**[打开 AI 课程助教 →](https://wbapp-xdrboti5h2c1km3knhvnz2.app.workbuddy.host/?sharecode=V3MGCTQXIW)**

使用普通浏览器即可直接提问，无需安装客户端或登录 WorkBuddy。助教由 [WorkBuddy](https://www.workbuddy.cn/) 发布，结合本仓库资料提供：

- **概念与推导讲解**：解释算法直觉、定义、公式和例子。
- **实验与代码定位**：查找 Notebook 单元格、源码函数和对应讲次。
- **作业辅导**：定位 Chapter 模板，提供分步提示、伪代码与检查方法。
- **复习规划**：按讲次梳理重点和知识联系。

打开页面后可选择讲次，也可保留“全部”。右上角的“模型”菜单可切换当前可用模型，“刷新模型”可重新获取云端目录；展开“查看模型 ID 与目录标价”可核对模型的实际 ID、标价和可用状态。模型选择独立于 WorkBuddy 客户端的开发对话，并会保存在当前浏览器。

回答下方的“课程出处”可展开查看文件位置和 GitHub 原文；课件引用使用 **PDF 物理页码**，代码引用注明函数、行号或单元格。切换学习主题时可点击“新建对话”。网页会话历史保存在各自浏览器，不会自动跨设备同步。

可以这样提问：

- “Chapter 3 作业在哪里、做什么？”
- “MinHash 与 LSH 有什么关系？请引用课件物理页码。”
- “帮我制定 Lecture 1–6 的复习计划。”

**资料范围**：22 讲课件共 1120 页 PDF、36 个 Notebook、6 份 Tutorial、4 份作业模板及 29 个 Python 源文件。当前知识基准为仓库提交 [`78b9424`](https://github.com/SJTU-CILAB/Algorithm-for-Big-Data/commit/78b942463ff51b2e5bd197c8bdd64b2581832eb7)；仓库后续更新需重新整理资料并更新发布，不会自动同步到助教。提交时间和考核安排以当期课程通知为准，课件中的历史安排不能直接视为本学期通知。

**模型与额度**：在线助教当前默认使用 **Hy4（`hy4std`）**，也可在网页中手动切换其他可用模型。调用使用发布账号的现有积分与模型额度，允许选择收费模型；目录标价仅供参考，实际消耗以 WorkBuddy 账单为准。每次提问前会复核所选模型的启用状态，额度不足、限流或服务异常时显示云端错误并保留问题，不会自动重复调用。部分推理模型生成回答可能需要数分钟，请等待页面显示完成。

模型积分与云服务资源点分别计算。云服务根据计算、存储、请求和流量等实际资源用量扣点，额度按月刷新，耗尽后暂停；不能仅按网页打开时长估算可用天数。具体规则见 [WorkBuddy 官方云服务说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/App-Publishing/Cloud-Services)。

## 目录结构

| 目录 | 内容 |
| --- | --- |
| `Lecture 1/` 至 `Lecture 22/` | 各讲课件，以及对应的 Notebook、Python 代码和实验材料 |
| `Supplementary/` | kd-tree 范围查询与复杂度分析补充材料 |
| `Survey/` | 论文选题清单、ACM LaTeX 与 Word 写作参考模板 |

各讲课件保存在对应目录中，统一命名为 `Lecture_N.pdf`，其中 `N` 为讲次编号。示例文件保留原有大小写与编号方式，请按目录中的实际文件名打开。

数据、图示和模型文件随讲次整理，既有与 Notebook 同目录的文件，也有 `data/`、`datasets/`、`CIFAR10/`、`mnist/` 等子目录。数据准备方式以对应实验说明和代码中的读取路径为准。

## 课程内容与示例

下表中的示例文件名均相对于对应的 Lecture 目录。

| 讲次 | 主要内容 | 示例与材料 |
| --- | --- | --- |
| Lecture 1 | 课程概览与大数据导论 | `open_large_file.py`、`Tutorial.md` |
| Lecture 2 | MapReduce 基础与函数式编程 | `Lecture_2.ipynb` |
| Lecture 3 | MapReduce 算法与 Spark | `Lecture_3.ipynb`、`Tutorial.md` |
| Lecture 4 | MinHash 与文档相似性 | `lecture_4.ipynb`、`Tutorial.md` |
| Lecture 5 | 局部敏感哈希与近邻检索 | `lecture_5.ipynb`、`Tutorial.md` |
| Lecture 6 | 局部敏感哈希理论 | `lecture_6(1).ipynb` 等 3 个 Notebook、`Tutorial.md` |
| Lecture 7 | 大规模机器学习：决策树 | `lecture_7(1).ipynb` 等 3 个 Notebook |
| Lecture 8 | 大规模机器学习：集成学习 | `lecture_8(1).ipynb`、`lecture8(2).py` |
| Lecture 9 | SVM 与并行 SGD | `lecture9(1).ipynb` 等 3 个 Notebook |
| Lecture 10 | 奇异值分解与降维 | `lecture_10.ipynb`、图像压缩示例材料 |
| Lecture 11 | 嵌入表示学习 | `lecture_11.ipynb`，包含 Word2Vec 与文本分析示例 |
| Lecture 12 | PageRank | `lecture_12(1).ipynb`、`lecture_12(2).ipynb` |
| Lecture 13 | 图社区发现 | `lecture_13.ipynb`、`Louvain.py` |
| Lecture 14 | 节点表示学习 | `lecture_14.ipynb` 等 3 个 Notebook，包含 DeepWalk 与 node2vec |
| Lecture 15 | 图神经网络 | `lecture_15(1).ipynb`、`lecture_15(2).ipynb` |
| Lecture 16 | 大规模图神经网络 | `lecture_16.ipynb`、`lecture_16(2).ipynb`、`Tutorial.md` |
| Lecture 17 | 推荐系统：基于内容的方法与协同过滤 | `lecture_17.ipynb`、`lecture_17(2).ipynb`、`CFModel.py` |
| Lecture 18 | 推荐系统：隐因子模型 | `lecture_18.ipynb` 等 4 个 Notebook、`PMF.py`、`Metrics_topK.py` |
| Lecture 19 | 图神经网络推荐系统 | `NGCF/`、`LightGCN/` 中的模型、训练与数据处理代码 |
| Lecture 20 | 时间序列数据挖掘（一） | `lecture_20.ipynb`，包含 AR、MA、ARMA、ARIMA 等示例 |
| Lecture 21 | 时间序列分析（二） | `lecture_21.ipynb`、`demo.ipynb`、`demo2.ipynb`，以及 RNN 分类与回归脚本 |
| Lecture 22 | 数据流挖掘 | 课件 |

## Chapter 作业

仓库收录以下 4 份 Chapter 作业代码模板，保留了需要实现的 `TODO`。

| 作业 | 文件位置 | 主要内容 |
| --- | --- | --- |
| Chapter 1 | `Lecture 3/Chapter1_Homework.py` | 使用 `map` 与 `reduce` 完成姓名规范化、求和与连乘 |
| Chapter 2 | `Lecture 6/Chapter2_Homework.py` | 欧氏距离 LSH：哈希计算、插入、候选集与近邻排序 |
| Chapter 3 | `Lecture 9/Chapter3_Homework.py` | 基于熵与数据划分的决策树实现 |
| Chapter 4 | `Lecture 11/Chapter4_Homework.py` | SVD 实现、奇异值截断与图像重建 |

Chapter 编号与 Lecture 编号分别组织。查找作业时按上表定位；例如，Chapter 3 是决策树作业，Chapter 4 是 SVD 作业。提交方式、截止时间和考核要求以当期课程通知为准。

## 补充与调研材料

- `Supplementary/Lecture5_kdtree_complexity.pdf`：kd-tree 的正交范围查询与复杂度分析。
- `Survey/Survey Seed Papers.docx`：图数据挖掘、推荐系统、序列数据挖掘三个方向的论文题目清单，共 30 个条目，可作为调研选题入口。
- `Survey/ACM Conference Proceedings LATEX Template/` 及同名压缩包：LaTeX 写作参考模板、示例与说明。
- `Survey/ACM Conference Proceedings Word Template.docx`：Word 写作参考模板。

## 使用方式

获取仓库：

```bash
git clone https://github.com/SJTU-CILAB/Algorithm-for-Big-Data.git
cd Algorithm-for-Big-Data
```

1. 按讲次阅读课件，再结合对应 Notebook 或源码理解算法实现。
2. 先阅读该讲的 `Tutorial.md`（若有）及 Notebook 内的说明，准备所需依赖和数据。现有教程分布在 Lecture 1、3、4、5、6、16。
3. 示例使用的库随讲次而异，涉及 NumPy、pandas、scikit-learn、PySpark、gensim、PyTorch、DGL、PyTorch Geometric、Keras 等；按实际导入项和实验说明准备运行环境。
4. 运行使用相对路径的代码时，保持数据目录结构与实验说明一致，并按顺序执行 Notebook 单元格。目录名含空格，终端切换目录时使用引号，例如 `cd "Lecture 3"`。
5. 完成作业模板中的 `TODO` 后，结合题目要求检查结果；论文调研可从 `Survey/` 中的选题清单与写作模板开始。
