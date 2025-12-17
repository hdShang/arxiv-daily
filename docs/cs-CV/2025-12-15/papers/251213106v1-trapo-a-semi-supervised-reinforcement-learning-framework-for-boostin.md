---
layout: default
title: TraPO: A Semi-Supervised Reinforcement Learning Framework for Boosting LLM Reasoning
---

# TraPO: A Semi-Supervised Reinforcement Learning Framework for Boosting LLM Reasoning

**arXiv**: [2512.13106v1](https://arxiv.org/abs/2512.13106) | [PDF](https://arxiv.org/pdf/2512.13106.pdf)

**作者**: Shenzhi Yang, Guangcheng Zhu, Xing Zheng, Yingfan MA, Zhongqi Chen, Bowen Song, Weiqiang Wang, Junbo Zhao, Gang Chen, Haobo Wang

---

## 💡 一句话要点

**提出TraPO半监督强化学习框架，以少量标注样本提升大语言模型推理能力**

**关键词**: `半监督强化学习` `大语言模型推理` `轨迹相似性匹配` `数学推理基准` `数据效率优化` `泛化能力提升`

## 📋 核心要点

1. 核心问题：无监督RLVR方法在训练后期易发生模型崩溃，源于缺乏外部监督强化错误推理模式
2. 方法要点：利用小规模标注集引导无标注样本的RLVR训练，通过轨迹相似性匹配识别可靠样本
3. 实验或效果：在六个数学推理基准和三个分布外任务上实现高数据效率和强泛化，仅用10%标注数据超越全监督模型

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has proven effective in training large reasoning models (LRMs) by leveraging answer-verifiable signals to guide policy optimization, which, however, suffers from high annotation costs. To alleviate this problem, recent work has explored unsupervised RLVR methods that derive rewards solely from the model's internal consistency, such as through entropy and majority voting. While seemingly promising, these methods often suffer from model collapse in the later stages of training, which may arise from the reinforcement of incorrect reasoning patterns in the absence of external supervision. In this work, we investigate a novel semi-supervised RLVR paradigm that utilizes a small labeled set to guide RLVR training on unlabeled samples. Our key insight is that supervised rewards are essential for stabilizing consistency-based training on unlabeled samples, ensuring that only reasoning patterns verified on labeled instances are incorporated into RL training. Technically, we propose an effective policy optimization algorithm, TraPO, that identifies reliable unlabeled samples by matching their learning trajectory similarity to labeled ones. Building on this, TraPO achieves remarkable data efficiency and strong generalization on six widely used mathematical reasoning benchmarks (AIME24/25, AMC, MATH-500, Minerva, and Olympiad) and three out-of-distribution tasks (ARC-c, GPQA-diamond, and MMLU-pro). With only 1K labeled and 3K unlabeled samples, TraPO reaches 42.6% average accuracy, surpassing the best unsupervised method trained on 45K unlabeled samples (38.3%). Notably, when using 4K labeled and 12K unlabeled samples, TraPO even outperforms the fully supervised model trained on the full 45K labeled samples on all benchmarks, while using only 10% of the labeled data. The code is available via https://github.com/ShenzhiYang2000/TRAPO.

