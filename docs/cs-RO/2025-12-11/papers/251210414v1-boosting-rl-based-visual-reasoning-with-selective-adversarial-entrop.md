---
layout: default
title: Boosting RL-Based Visual Reasoning with Selective Adversarial Entropy Intervention
---

# Boosting RL-Based Visual Reasoning with Selective Adversarial Entropy Intervention

**arXiv**: [2512.10414v1](https://arxiv.org/abs/2512.10414) | [PDF](https://arxiv.org/pdf/2512.10414.pdf)

**作者**: Yang Yu, Zhuangzhuang Chen, Siqi Wang, Lanqing Li, Xiaomeng Li

---

## 💡 一句话要点

**提出选择性对抗熵干预以增强基于强化学习的视觉推理能力**

**关键词**: `强化学习` `视觉语言模型` `熵干预` `对抗攻击` `视觉推理` `策略优化`

## 📋 核心要点

1. 现有基于强化学习的视觉语言模型微调方法忽视采样阶段的熵干预，影响响应多样性和性能
2. 提出SaEI方法，通过熵引导对抗采样和令牌选择性熵计算，在强化学习采样中增强策略熵
3. 在领域内和领域外数据集上实验显示，该方法能显著提升策略探索和推理能力

## 📄 摘要（原文）

> Recently, reinforcement learning (RL) has become a common choice in enhancing the reasoning capabilities of vision-language models (VLMs). Considering existing RL-based finetuning methods, entropy intervention turns out to be an effective way to benefit exploratory ability, thereby improving policy performance. Notably, most existing studies intervene in entropy by simply controlling the update of specific tokens during policy optimization of RL. They ignore the entropy intervention during the RL sampling that can boost the performance of GRPO by improving the diversity of responses. In this paper, we propose Selective-adversarial Entropy Intervention, namely SaEI, which enhances policy entropy by distorting the visual input with the token-selective adversarial objective coming from the entropy of sampled responses. Specifically, we first propose entropy-guided adversarial sampling (EgAS) that formulates the entropy of sampled responses as an adversarial objective. Then, the corresponding adversarial gradient can be used to attack the visual input for producing adversarial samples, allowing the policy model to explore a larger answer space during RL sampling. Then, we propose token-selective entropy computation (TsEC) to maximize the effectiveness of adversarial attack in EgAS without distorting factual knowledge within VLMs. Extensive experiments on both in-domain and out-of-domain datasets show that our proposed method can greatly improve policy exploration via entropy intervention, to boost reasoning capabilities. Code will be released once the paper is accepted.

