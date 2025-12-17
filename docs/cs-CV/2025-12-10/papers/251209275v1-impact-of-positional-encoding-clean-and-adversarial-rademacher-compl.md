---
layout: default
title: Impact of Positional Encoding: Clean and Adversarial Rademacher Complexity for Transformers under In-Context Regression
---

# Impact of Positional Encoding: Clean and Adversarial Rademacher Complexity for Transformers under In-Context Regression

**arXiv**: [2512.09275v1](https://arxiv.org/abs/2512.09275) | [PDF](https://arxiv.org/pdf/2512.09275.pdf)

**作者**: Weiyi He, Yue Xing

---

## 💡 一句话要点

**分析可训练位置编码对Transformer在上下文回归中泛化与鲁棒性的影响**

**关键词**: `位置编码` `Transformer` `上下文回归` `泛化分析` `对抗鲁棒性` `Rademacher复杂度`

## 📋 核心要点

1. 核心问题：位置编码对Transformer泛化与鲁棒性的影响未知
2. 方法要点：推导单层Transformer在上下文回归中的泛化与对抗Rademacher界
3. 实验或效果：模拟研究验证理论界，显示位置编码放大泛化差距与脆弱性

## 📄 摘要（原文）

> Positional encoding (PE) is a core architectural component of Transformers, yet its impact on the Transformer's generalization and robustness remains unclear. In this work, we provide the first generalization analysis for a single-layer Transformer under in-context regression that explicitly accounts for a completely trainable PE module. Our result shows that PE systematically enlarges the generalization gap. Extending to the adversarial setting, we derive the adversarial Rademacher generalization bound. We find that the gap between models with and without PE is magnified under attack, demonstrating that PE amplifies the vulnerability of models. Our bounds are empirically validated by a simulation study. Together, this work establishes a new framework for understanding the clean and adversarial generalization in ICL with PE.

