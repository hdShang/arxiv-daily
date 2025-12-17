---
layout: default
title: Mechanistic Interpretability of Antibody Language Models Using SAEs
---

# Mechanistic Interpretability of Antibody Language Models Using SAEs

**arXiv**: [2512.05794v1](https://arxiv.org/abs/2512.05794) | [PDF](https://arxiv.org/pdf/2512.05794.pdf)

**作者**: Rebonto Haque, Oliver M. Turnbull, Anisha Parsan, Nithin Parsan, John J. Yang, Charlotte M. Deane

---

## 💡 一句话要点

**采用稀疏自编码器提升抗体语言模型的机制可解释性与生成控制**

**关键词**: `稀疏自编码器` `抗体语言模型` `机制可解释性` `生成控制` `蛋白质语言模型` `潜在特征分析`

## 📋 核心要点

1. 研究TopK和Ordered稀疏自编码器在抗体语言模型p-IgGen中的应用，以揭示潜在特征。
2. TopK SAEs能映射生物相关特征，但高相关性不保证生成因果控制；Ordered SAEs提供可靠可操控特征，但激活模式更复杂。
3. 实验表明TopK SAEs适合概念映射，Ordered SAEs更适用于精确生成引导，推进领域特定蛋白质模型的机制可解释性。

## 📄 摘要（原文）

> Sparse autoencoders (SAEs) are a mechanistic interpretability technique that have been used to provide insight into learned concepts within large protein language models. Here, we employ TopK and Ordered SAEs to investigate an autoregressive antibody language model, p-IgGen, and steer its generation. We show that TopK SAEs can reveal biologically meaningful latent features, but high feature concept correlation does not guarantee causal control over generation. In contrast, Ordered SAEs impose an hierarchical structure that reliably identifies steerable features, but at the expense of more complex and less interpretable activation patterns. These findings advance the mechanistic interpretability of domain-specific protein language models and suggest that, while TopK SAEs are sufficient for mapping latent features to concepts, Ordered SAEs are preferable when precise generative steering is required.

