---
layout: default
title: "Beyond Scaling Law: A Data-Efficient Distillation Framework for Reasoning"
---

# Beyond Scaling Law: A Data-Efficient Distillation Framework for Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09883" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09883v1</a>
  <a href="https://arxiv.org/pdf/2508.09883.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09883v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09883v1', 'Beyond Scaling Law: A Data-Efficient Distillation Framework for Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaojun Wu, Xiaoguang Jiang, Huiyang Li, Jucai Zhai, Dengfeng Liu, Qiaobo Hao, Huang Liu, Zhiguo Yang, Ji Xie, Ninglun Gu, Jin Yang, Kailai Zhang, Yelun Bao, Jun Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出数据高效蒸馏框架以优化推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据高效蒸馏` `推理能力` `教师模型选择` `小语料库` `多样化推理轨迹` `大型语言模型` `数学推理` `代码生成`

## 📋 核心要点

1. 现有方法在推理能力提升上依赖于大规模数据集，导致计算成本高且效果不稳定。
2. 提出的数据高效蒸馏框架通过优化教师模型选择和小语料库使用，提升推理能力。
3. 在数学推理和代码生成任务中，DED方法以0.8k示例实现了最先进的性能，超越了现有方法。

## 📝 摘要（中文）

大型语言模型（LLMs）在算法编码和数学问题解决等任务中展现出卓越的推理能力。尽管现有方法通过扩展语料库和结合强化学习与监督微调的多阶段训练来提升推理能力，但推理的规模法则仍在形成中，导致计算成本增加。为此，本文提出了一种数据高效蒸馏框架（DED），旨在优化推理蒸馏的帕累托前沿。我们的方法包括三个关键点：首先，通过对领先推理LLMs的全面比较，开发了一种选择最佳教师模型的方法；其次，精心策划的小语料库在领域内外能力之间实现了平衡；最后，多样化的推理轨迹鼓励学生模型发展稳健的推理技能。我们在数学推理和代码生成任务上验证了该方法，取得了最先进的结果，仅需0.8k精心策划的示例，避免了大规模扩展的需求。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推理蒸馏方法在计算成本和领域外性能下降的问题。现有方法通常依赖于大规模数据集，导致资源浪费和效果不佳。

**核心思路**：论文提出了一种数据高效蒸馏框架（DED），通过优化教师模型选择和使用小规模语料库，提升推理能力，同时保持领域外性能。

**技术框架**：DED框架包括三个主要模块：教师模型选择、语料库优化和多样化推理轨迹生成。首先，通过对比分析选择最佳教师模型；其次，使用精心策划的小语料库；最后，生成多样化的推理轨迹以增强学生模型的推理能力。

**关键创新**：最重要的技术创新在于提出了优化教师模型选择的方法，以及通过小语料库实现领域内外能力的平衡。这与现有方法依赖于大规模数据集的本质区别显著。

**关键设计**：在模型训练中，采用了特定的损失函数和参数设置，以确保教师模型的有效性和学生模型的学习效率。通过多样化的推理轨迹设计，增强了学生模型的推理能力。具体的网络结构和参数设置在实验中进行了详细验证。

## 📊 实验亮点

在数学推理（AIME 2024/2025，MATH-500）和代码生成（LiveCodeBench）任务中，DED方法仅使用0.8k精心策划的示例，取得了最先进的结果，显著超越了现有方法，展示了其在推理能力提升上的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程辅助和自动化推理系统。通过提升推理能力，DED框架能够在更少的数据下实现更高效的学习，具有广泛的实际价值和未来影响，尤其是在资源受限的环境中。

## 📄 摘要（原文）

> Large language models (LLMs) demonstrate remarkable reasoning capabilities in tasks such as algorithmic coding and mathematical problem-solving. Recent methods have improved reasoning through expanded corpus and multistage training combining reinforcement learning and supervised fine-tuning. Although some methods suggest that small but targeted dataset can incentivize reasoning via only distillation, a reasoning scaling laws is still taking shape, increasing computational costs. To address this, we propose a data-efficient distillation framework (DED) that optimizes the Pareto frontier of reasoning distillation. Inspired by the on-policy learning and diverse roll-out strategies of reinforcement learning, the key idea of our approach is threefold: (1) We identify that benchmark scores alone do not determine an effective teacher model. Through comprehensive comparisons of leading reasoning LLMs, we develop a method to select an optimal teacher model. (2) While scaling distillation can enhance reasoning, it often degrades out-of-domain performance. A carefully curated, smaller corpus achieves a balanced trade-off between in-domain and out-of-domain capabilities. (3) Diverse reasoning trajectories encourage the student model to develop robust reasoning skills. We validate our method through evaluations on mathematical reasoning (AIME 2024/2025, MATH-500) and code generation (LiveCodeBench), achieving state-of-the-art results with only 0.8k carefully curated examples, bypassing the need for extensive scaling. Our systematic analysis demonstrates that DED outperforms existing methods by considering factors beyond superficial hardness, token length, or teacher model capability. This work offers a practical and efficient pathway to advanced reasoning while preserving general capabilities.

