---
layout: default
title: ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models
---

# ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24864" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24864v1</a>
  <a href="https://arxiv.org/pdf/2505.24864.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24864v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24864v1', 'ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, Yi Dong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

**备注**: 26 pages, 17 figures

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/nvidia/Nemotron-Research-Reasoning-Qwen-1.5B)

---

## 💡 一句话要点

**提出ProRL以扩展大语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `推理能力` `语言模型` `KL散度` `任务多样性` `模型训练` `深度学习`

## 📋 核心要点

1. 现有方法中，强化学习是否真正提升了模型的推理能力仍存在争议，且基础模型在某些任务上表现不佳。
2. 论文提出ProRL，通过KL散度控制、参考策略重置和多样化任务组合，探索新的推理策略。
3. 实验结果显示，RL训练的模型在多项评估中表现优于基础模型，尤其在基础模型失败的情况下，提升显著。

## 📝 摘要（中文）

近年来，推理中心的语言模型进展表明，强化学习（RL）是一种有前景的方法，用于将模型与可验证的奖励对齐。然而，RL是否真正扩展了模型的推理能力，或仅仅放大了基础模型分布中潜在的高奖励输出，仍存在争议。本研究通过引入ProRL，一种新颖的训练方法，展示了延长的RL训练能够发现基础模型无法访问的新推理策略。实证分析表明，RL训练的模型在多种评估中始终优于基础模型，尤其是在基础模型完全失败的情况下。研究结果为RL在语言模型中有意义地扩展推理边界的条件提供了新见解，并为未来的长时间RL推理工作奠定了基础。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有强化学习方法在扩展语言模型推理能力方面的争议，尤其是其是否能发现新的推理策略。现有方法在某些任务上表现不佳，无法充分利用模型的潜力。

**核心思路**：论文提出ProRL训练方法，强调通过延长RL训练时间和多样化任务组合，能够揭示基础模型未能发现的新推理策略。此设计旨在突破基础模型的推理边界。

**技术框架**：ProRL的整体架构包括三个主要模块：KL散度控制用于平衡探索与利用，参考策略重置以避免模型陷入局部最优，以及多样化任务组合以增强模型的泛化能力。

**关键创新**：ProRL的核心创新在于其训练方法的设计，通过延长训练时间和引入多样化任务，能够有效发现新的推理策略，与传统RL方法相比，显著提升了模型的推理能力。

**关键设计**：在ProRL中，KL散度控制用于确保模型在探索新策略时不偏离已有的有效策略，参考策略重置则用于定期更新模型的学习目标，确保其适应不同的任务场景。

## 📊 实验亮点

实验结果表明，RL训练的模型在多项pass@k评估中表现优于基础模型，尤其在基础模型完全失败的情况下，提升幅度显著，验证了ProRL的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过提升语言模型的推理能力，ProRL可以在复杂任务中提供更准确的答案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in reasoning-centric language models have highlighted reinforcement learning (RL) as a promising method for aligning models with verifiable rewards. However, it remains contentious whether RL truly expands a model's reasoning capabilities or merely amplifies high-reward outputs already latent in the base model's distribution, and whether continually scaling up RL compute reliably leads to improved reasoning performance. In this work, we challenge prevailing assumptions by demonstrating that prolonged RL (ProRL) training can uncover novel reasoning strategies that are inaccessible to base models, even under extensive sampling. We introduce ProRL, a novel training methodology that incorporates KL divergence control, reference policy resetting, and a diverse suite of tasks. Our empirical analysis reveals that RL-trained models consistently outperform base models across a wide range of pass@k evaluations, including scenarios where base models fail entirely regardless of the number of attempts. We further show that reasoning boundary improvements correlates strongly with task competence of base model and training duration, suggesting that RL can explore and populate new regions of solution space over time. These findings offer new insights into the conditions under which RL meaningfully expands reasoning boundaries in language models and establish a foundation for future work on long-horizon RL for reasoning. We release model weights to support further research: https://huggingface.co/nvidia/Nemotron-Research-Reasoning-Qwen-1.5B

