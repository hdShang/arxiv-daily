---
layout: default
title: Beyond Sequences: A Benchmark for Atomic Hand-Object Interaction Using a Static RNN Encoder
---

# Beyond Sequences: A Benchmark for Atomic Hand-Object Interaction Using a Static RNN Encoder

**arXiv**: [2512.09626v1](https://arxiv.org/abs/2512.09626) | [PDF](https://arxiv.org/pdf/2512.09626.pdf)

**作者**: Yousef Azizi Movahed, Fatemeh Ziaeetabar

---

## 💡 一句话要点

**提出静态RNN编码器用于原子手-物交互分类，在MANIAC数据集上实现97.60%准确率。**

**关键词**: `手-物交互识别` `原子交互分类` `静态RNN编码器` `统计-运动特征` `MANIAC数据集` `细粒度识别`

## 📋 核心要点

1. 核心问题：细粒度分类手-物交互的原子状态（接近、抓取、持有）。
2. 方法要点：将视频转换为统计-运动特征向量，使用序列长度设为1的双向RNN作为静态编码器。
3. 实验或效果：模型在最具挑战的'抓取'类上获得0.90平衡F1分数，准确率达97.60%。

## 📄 摘要（原文）

> Reliably predicting human intent in hand-object interactions is an open challenge for computer vision. Our research concentrates on a fundamental sub-problem: the fine-grained classification of atomic interaction states, namely 'approaching', 'grabbing', and 'holding'. To this end, we introduce a structured data engineering process that converts raw videos from the MANIAC dataset into 27,476 statistical-kinematic feature vectors. Each vector encapsulates relational and dynamic properties from a short temporal window of motion. Our initial hypothesis posited that sequential modeling would be critical, leading us to compare static classifiers (MLPs) against temporal models (RNNs). Counter-intuitively, the key discovery occurred when we set the sequence length of a Bidirectional RNN to one (seq_length=1). This modification converted the network's function, compelling it to act as a high-capacity static feature encoder. This architectural change directly led to a significant accuracy improvement, culminating in a final score of 97.60%. Of particular note, our optimized model successfully overcame the most challenging transitional class, 'grabbing', by achieving a balanced F1-score of 0.90. These findings provide a new benchmark for low-level hand-object interaction recognition using structured, interpretable features and lightweight architectures.

