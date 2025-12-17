---
layout: default
title: Flexible Concept Bottleneck Model
---

# Flexible Concept Bottleneck Model

**arXiv**: [2511.06678v1](https://arxiv.org/abs/2511.06678) | [PDF](https://arxiv.org/pdf/2511.06678.pdf)

**作者**: Xingbo Du, Qiantong Dou, Lei Fan, Rui Zhang

---

## 💡 一句话要点

**提出灵活概念瓶颈模型以解决动态概念适应问题**

**关键词**: `概念瓶颈模型` `视觉语言模型` `动态概念适应` `超网络` `稀疏最大模块`

## 📋 核心要点

1. 现有基于视觉语言模型的概念瓶颈模型在引入新概念时需完全重训练，限制灵活性
2. 设计超网络基于概念嵌入生成预测权重，无需重训练即可整合新概念
3. 在五个基准测试中达到与先进基线相当的准确率，并展示对未见概念的强适应性

## 📄 摘要（原文）

> Concept bottleneck models (CBMs) improve neural network interpretability by
> introducing an intermediate layer that maps human-understandable concepts to
> predictions. Recent work has explored the use of vision-language models (VLMs)
> to automate concept selection and annotation. However, existing VLM-based CBMs
> typically require full model retraining when new concepts are involved, which
> limits their adaptability and flexibility in real-world scenarios, especially
> considering the rapid evolution of vision-language foundation models. To
> address these issues, we propose Flexible Concept Bottleneck Model (FCBM),
> which supports dynamic concept adaptation, including complete replacement of
> the original concept set. Specifically, we design a hypernetwork that generates
> prediction weights based on concept embeddings, allowing seamless integration
> of new concepts without retraining the entire model. In addition, we introduce
> a modified sparsemax module with a learnable temperature parameter that
> dynamically selects the most relevant concepts, enabling the model to focus on
> the most informative features. Extensive experiments on five public benchmarks
> demonstrate that our method achieves accuracy comparable to state-of-the-art
> baselines with a similar number of effective concepts. Moreover, the model
> generalizes well to unseen concepts with just a single epoch of fine-tuning,
> demonstrating its strong adaptability and flexibility.

