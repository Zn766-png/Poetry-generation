# 大作业 诗词生成

## 任务：
1. 输入“首句/藏头字”，生成符合格式的七言绝句，并能展示生成样例与基本评测。
2. 数据集：下载地址为https://dicalab-scu.github.io/nlp/post/ancient-poems-dataset/
3. 只取七言绝句子集，四句、每句 7 字。
4. 输入输出：生成对象七言绝句：每句 7 个汉字（不含标点），共 4 句。条件生成（至少支持一种）：
- 首句续写：给定第一句，生成后 3 句
- 藏头诗：给定 4 个字，分别作为四句首字

## 模型：
任选模型实现，最低基线：字符级 GRU/LSTM。需要实现一种采样策略（temperature，top-k…），评测指标为困惑度PPL以及格式合规率。每种条件输入至少展示 5 组生成结果，对 5 组结果做简短分析，如是否跑题、是否重复、是否结构完整。调整采样策略参数值，比较模型的生成效果。

## 提交：
1. 代码文件
2. 模型checkpoint以及报告。报告至少包含：数据处理说明、模型结构、训练曲线、指标表、生成样例与分析。 

***

# Major Assignment: Poetry Generation 
## Task:
1. Input "first line / initial character", generate a seven-line ancient poem in the specified format, and display the generated sample and basic evaluation.
2. Dataset: Download link is https://dicalab-scu.github.io/nlp/post/ancient-poems-dataset/
3. Only select the seven-line sentence set, with 4 lines and 7 characters each.
4. Input and output: Generated object: seven-line ancient poem: each line 7 Chinese characters (excluding punctuation), a total of 4 lines. Conditional generation (at least one type supported):
- First line continuation: given the first line, generate the next 3 lines
- Initial character poem: given 4 characters, respectively as the first characters of the four lines 
## Model:
Choose any model implementation. The minimum baseline is character-level GRU/LSTM. Implement a sampling strategy (temperature, top-k...), and the evaluation metrics are perplexity PPL and format compliance rate. Show at least 5 generated results for each condition input, and briefly analyze the 5 results, such as whether they deviate from the topic, whether they are repetitive, and whether they have a complete structure. Adjust the parameter values of the sampling strategy and compare the generation effects of the model. 
## Submission:
1. Code file
2. Model checkpoint and report. The report should at least include: data processing description, model structure, training curves, performance metrics table, generated samples and analysis.