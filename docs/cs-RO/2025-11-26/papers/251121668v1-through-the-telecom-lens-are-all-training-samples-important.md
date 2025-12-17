---
layout: default
title: Through the telecom lens: Are all training samples important?
---

# Through the telecom lens: Are all training samples important?

**arXiv**: [2511.21668v1](https://arxiv.org/abs/2511.21668) | [PDF](https://arxiv.org/pdf/2511.21668.pdf)

**作者**: Shruti Bothe, Illyyne Saffar, Aurelie Boisbunon, Hasan Farooq, Julien Forgeat, Md Moin Uddin Chowdhury

---

## 💡 一句话要点

**提出样本重要性框架以优化电信AI训练的计算与能源效率**

**关键词**: `样本重要性分析` `梯度分析` `电信AI优化` `可持续AI` `计算效率提升`

## 📋 核心要点

1. 核心问题：电信数据噪声高、成本大，标准训练假设所有样本同等重要，影响效率与可持续性。
2. 方法要点：通过样本级梯度分析识别影响模式，选择性优先处理重要数据以减少计算。
3. 实验或效果：在三个真实电信数据集上验证，保持性能同时降低数据需求和计算开销。

## 📄 摘要（原文）

> The rise of AI in telecommunications, from optimizing Radio Access Networks to managing user experience, has sharply increased data volumes and training demands. Telecom data is often noisy, high-dimensional, costly to store, process, and label. Despite Ai's critical role, standard workflows still assume all training samples contribute equally. On the other hand, next generation systems require AI models that are accurate, efficient, and sustainable.The paper questions the assumptions of equal importance by focusing on applying and analyzing the roles of individual samples in telecom training and assessing whether the proposed model optimizes computation and energy use. we perform sample-level gradient analysis across epochs to identify patterns of influence and redundancy in model learning. Based on this, we propose a sample importance framework thats electively prioritizes impactful data and reduces computation without compromising accuracy. Experiments on three real-world telecom datasets show that our method [reserves performance while reducing data needs and computational overhead while advancing the goals of sustainable AI in telecommunications.

