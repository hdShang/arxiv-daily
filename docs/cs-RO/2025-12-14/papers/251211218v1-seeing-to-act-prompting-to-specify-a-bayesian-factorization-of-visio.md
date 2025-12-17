---
layout: default
title: Seeing to Act, Prompting to Specify: A Bayesian Factorization of Vision Language Action Policy
---

# Seeing to Act, Prompting to Specify: A Bayesian Factorization of Vision Language Action Policy

**arXiv**: [2512.11218v1](https://arxiv.org/abs/2512.11218) | [PDF](https://arxiv.org/pdf/2512.11218.pdf)

**作者**: Kechun Xu, Zhenjie Zhu, Anzhe Chen, Shuqi Zhao, Qing Huang, Yifei Yang, Haojian Lu, Rong Xiong, Masayoshi Tomizuka, Yue Wang

---

## 💡 一句话要点

**提出BayesVLA贝叶斯分解方法，解决视觉-语言-动作模型中模态不平衡导致的泛化问题。**

**关键词**: `视觉-语言-动作模型` `贝叶斯分解` `模态不平衡` `泛化能力` `信息论分析` `预训练模型利用`

## 📋 核心要点

1. 核心问题：VLA模型微调时因模态不平衡（语言多样性低）导致视觉捷径和语言遗忘，阻碍分布外泛化。
2. 方法要点：通过贝叶斯分解将策略分解为视觉-动作先验和语言条件似然，支持“看到即行动”和“提示指定”，保留泛化能力。
3. 实验或效果：在未见指令、对象和环境上优于现有方法，信息论分析验证缓解捷径学习的有效性。

## 📄 摘要（原文）

> The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

