---
layout: default
title: Is the Information Bottleneck Robust Enough? Towards Label-Noise Resistant Information Bottleneck Learning
---

# Is the Information Bottleneck Robust Enough? Towards Label-Noise Resistant Information Bottleneck Learning

**arXiv**: [2512.10573v1](https://arxiv.org/abs/2512.10573) | [PDF](https://arxiv.org/pdf/2512.10573.pdf)

**作者**: Yi Huang, Qingyun Sun, Yisen Gao, Haonan Yuan, Xingcheng Fu, Jianxin Li

---

## 💡 一句话要点

**提出LaT-IB方法以解决信息瓶颈在标签噪声下的脆弱性问题**

**关键词**: `信息瓶颈` `标签噪声鲁棒性` `潜在解耦` `互信息正则化` `表示学习`

## 📋 核心要点

1. 信息瓶颈依赖准确标签，易受标签噪声影响导致性能下降
2. 引入最小充分清洁准则，通过噪声感知潜在解耦分离干净与噪声信息
3. 实验显示LaT-IB在标签噪声下具有优越的鲁棒性和效率

## 📄 摘要（原文）

> The Information Bottleneck (IB) principle facilitates effective representation learning by preserving label-relevant information while compressing irrelevant information. However, its strong reliance on accurate labels makes it inherently vulnerable to label noise, prevalent in real-world scenarios, resulting in significant performance degradation and overfitting. To address this issue, we propose LaT-IB, a novel Label-Noise ResistanT Information Bottleneck method which introduces a "Minimal-Sufficient-Clean" (MSC) criterion. Instantiated as a mutual information regularizer to retain task-relevant information while discarding noise, MSC addresses standard IB's vulnerability to noisy label supervision. To achieve this, LaT-IB employs a noise-aware latent disentanglement that decomposes the latent representation into components aligned with to the clean label space and the noise space. Theoretically, we first derive mutual information bounds for each component of our objective including prediction, compression, and disentanglement, and moreover prove that optimizing it encourages representations invariant to input noise and separates clean and noisy label information. Furthermore, we design a three-phase training framework: Warmup, Knowledge Injection and Robust Training, to progressively guide the model toward noise-resistant representations. Extensive experiments demonstrate that LaT-IB achieves superior robustness and efficiency under label noise, significantly enhancing robustness and applicability in real-world scenarios with label noise.

