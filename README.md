# Algorithms for Big Data

《Algorithms for Big Data》（大数据算法）课程的教学资料仓库，收录课件、实验示例、作业代码模板以及论文调研与写作材料。

课程内容按 Lecture 1–22 组织，覆盖 MapReduce 与 Spark、相似性与近邻检索、大规模机器学习、图数据挖掘、推荐系统、时间序列分析和数据流挖掘。当前包含 22 讲课件、36 个 Jupyter Notebook 和 4 份 Chapter 作业代码模板。

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
