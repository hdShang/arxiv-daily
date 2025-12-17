---
layout: default
title: The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality
---

# The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality

**arXiv**: [2512.10791v1](https://arxiv.org/abs/2512.10791) | [PDF](https://arxiv.org/pdf/2512.10791.pdf)

**作者**: Aileen Cheng, Alon Jacovi, Amir Globerson, Ben Golan, Charles Kwong, Chris Alberti, Connie Tao, Eyal Ben-David, Gaurav Singh Tomar, Lukas Haas, Yonatan Bitton, Adam Bloniarz, Aijun Bai, Andrew Wang, Anfal Siddiqui, Arturo Bajuelos Castillo, Aviel Atias, Chang Liu, Corey Fry, Daniel Balle, Deepanway Ghosal, Doron Kukliansky, Dror Marcus, Elena Gribovskaya, Eran Ofek, Honglei Zhuang, Itay Laish, Jan Ackermann, Lily Wang, Meg Risdal, Megan Barnes, Michael Fink, Mohamed Amin, Moran Ambar, Natan Potikha, Nikita Gupta, Nitzan Katz, Noam Velan, Ofir Roval, Ori Ram, Polina Zablotskaia, Prathamesh Bang, Priyanka Agrawal, Rakesh Ghiya, Sanjay Ganapathy, Simon Baumgartner, Sofia Erell, Sushant Prakash, Thibault Sellam, Vikram Rao, Xuanhui Wang, Yaroslav Akulov, Yulong Yang, Zhen Yang, Zhixin Lai, Zhongru Wu, Anca Dragan, Avinatan Hassidim, Fernando Pereira, Slav Petrov, Srinivasan Venkatachary, Tulsee Doshi, Yossi Matias, Sasha Goldshtein, Dipanjan Das

---

## 💡 一句话要点

**提出FACTS排行榜，通过多场景基准全面评估大语言模型生成文本的事实准确性。**

**关键词**: `事实性评估` `大语言模型基准` `多模态问答` `信息搜索` `文档引用` `自动化评判`

## 📋 核心要点

1. 核心问题：评估大语言模型生成文本的事实准确性，覆盖图像问答、闭卷知识、信息搜索和文档引用等多样场景。
2. 方法要点：构建包含四个子排行榜的在线套件，使用自动化评判模型评分，综合平均得分提供整体事实性评估。
3. 实验或效果：排行榜包含公开和私有分割，支持外部参与并维护完整性，旨在提供稳健平衡的模型事实性衡量。

## 📄 摘要（原文）

> We introduce The FACTS Leaderboard, an online leaderboard suite and associated set of benchmarks that comprehensively evaluates the ability of language models to generate factually accurate text across diverse scenarios. The suite provides a holistic measure of factuality by aggregating the performance of models on four distinct sub-leaderboards: (1) FACTS Multimodal, which measures the factuality of responses to image-based questions; (2) FACTS Parametric, which assesses models' world knowledge by answering closed-book factoid questions from internal parameters; (3) FACTS Search, which evaluates factuality in information-seeking scenarios, where the model must use a search API; and (4) FACTS Grounding (v2), which evaluates whether long-form responses are grounded in provided documents, featuring significantly improved judge models. Each sub-leaderboard employs automated judge models to score model responses, and the final suite score is an average of the four components, designed to provide a robust and balanced assessment of a model's overall factuality. The FACTS Leaderboard Suite will be actively maintained, containing both public and private splits to allow for external participation while guarding its integrity. It can be found at https://www.kaggle.com/benchmarks/google/facts .

