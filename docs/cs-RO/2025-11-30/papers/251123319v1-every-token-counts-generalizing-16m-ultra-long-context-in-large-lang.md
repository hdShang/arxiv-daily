---
layout: default
title: Every Token Counts: Generalizing 16M Ultra-Long Context in Large Language Models
---

# Every Token Counts: Generalizing 16M Ultra-Long Context in Large Language Models

**arXiv**: [2511.23319v1](https://arxiv.org/abs/2511.23319) | [PDF](https://arxiv.org/pdf/2511.23319.pdf)

**作者**: Xiang Hu, Zhanchao Zhou, Ruiqi Liang, Zehuan Li, Wei Wu, Jianguo Li

---

## 💡 一句话要点

**提出HSA-UltraLong模型以解决大语言模型超长上下文建模问题**

**关键词**: `超长上下文建模` `分层稀疏注意力` `大语言模型` `长期记忆` `MoE模型`

## 📋 核心要点

1. 核心问题：构建具有长期记忆的机器，需满足稀疏性、随机访问灵活性和长度泛化性
2. 方法要点：采用分层稀疏注意力机制，集成到Transformer中构建8B参数MoE模型
3. 实验或效果：在16M上下文长度下，多数检索任务准确率超90%，性能与全注意力基线相当

## 📄 摘要（原文）

> This work explores the challenge of building ``Machines that Can Remember'', framing long-term memory as the problem of efficient ultra-long context modeling. We argue that this requires three key properties: \textbf{sparsity}, \textbf{random-access flexibility}, and \textbf{length generalization}. To address ultra-long-context modeling, we leverage Hierarchical Sparse Attention (HSA), a novel attention mechanism that satisfies all three properties. We integrate HSA into Transformers to build HSA-UltraLong, which is an 8B-parameter MoE model trained on over 8 trillion tokens and is rigorously evaluated on different tasks with in-domain and out-of-domain context lengths to demonstrate its capability in handling ultra-long contexts. Results show that our model performs comparably to full-attention baselines on in-domain lengths while achieving over 90\% accuracy on most in-context retrieval tasks with contexts up to 16M. This report outlines our experimental insights and open problems, contributing a foundation for future research in ultra-long context modeling.

