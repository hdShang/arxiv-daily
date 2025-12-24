---
layout: default
title: "Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation"
---

# Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15194" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15194v2</a>
  <a href="https://arxiv.org/pdf/2509.15194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15194v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15194v2', 'Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujun Zhou, Zhenwen Liang, Haolin Liu, Wenhao Yu, Kishan Panaganti, Linfeng Song, Dian Yu, Xiangliang Zhang, Haitao Mi, Dong Yu

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-18 (更新: 2025-10-01)

**🔗 代码/项目**: [GITHUB](https://github.com/YujunZhou/EVOL-RL)

---

## 💡 一句话要点

**EVOL-RL：一种无标签进化语言模型框架，通过多数驱动选择和新颖性促进变异实现自提升。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型自提升` `无监督学习` `强化学习` `进化算法` `新颖性奖励` `多样性保持` `领域泛化`

## 📋 核心要点

1. 现有自提升语言模型方法过度依赖自我确认信号，导致模型倾向于多数支持的解决方案，造成多样性崩溃。
2. EVOL-RL框架模仿进化原则，结合多数投票的稳定性锚点和新颖性感知奖励，平衡选择与变异。
3. 实验表明，EVOL-RL显著提升了模型在数学推理和更广泛任务上的性能，并有效防止了领域内多样性崩溃。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地采用基于可验证奖励的强化学习（RLVR）进行训练，但实际部署需要模型能够在没有标签或外部评判的情况下进行自我改进。现有的自我改进方法主要依赖于自我确认信号（例如，置信度、熵或一致性）来生成奖励。这种依赖驱使模型倾向于过度自信、多数支持的解决方案，导致熵崩溃，从而降低pass@n和推理复杂度。为了解决这个问题，我们提出了EVOL-RL，一个无标签框架，它反映了平衡选择与变异的进化原则。具体而言，EVOL-RL保留多数投票的答案作为稳定性的锚点，但增加了一个新颖性感知奖励，该奖励根据每个采样解的推理与其他并发生成的响应的差异程度对其进行评分。这种多数驱动稳定+新颖性驱动探索的规则反映了变异-选择原则：选择防止漂移，而新颖性防止崩溃。评估结果表明，EVOL-RL始终优于仅多数基线；例如，在无标签AIME24上训练将Qwen3-4B-Base AIME25的pass@1从基线的4.6%提升到16.4%，pass@16从18.5%提升到37.9%。EVOL-RL不仅防止了领域内多样性崩溃，还提高了领域外泛化能力（从数学推理到更广泛的任务，例如GPQA、MMLU-Pro和BBEH）。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在无标签或外部评判的情况下进行自我改进的问题。现有方法依赖于自我确认信号，导致模型过度自信，倾向于多数答案，造成多样性（熵）崩溃，最终影响模型的推理能力和泛化性能。

**核心思路**：论文的核心思路是借鉴生物进化中的“选择与变异”原则。通过保留多数投票的答案作为稳定性的锚点（选择），并引入新颖性感知奖励来鼓励模型探索不同的推理路径（变异），从而在稳定性和探索性之间取得平衡。

**技术框架**：EVOL-RL框架包含以下主要步骤：1) 使用语言模型生成多个候选答案；2) 对这些答案进行多数投票，选出最常见的答案作为锚点；3) 计算每个候选答案的新颖性得分，该得分衡量了该答案的推理过程与其他答案的差异程度；4) 将多数投票结果和新颖性得分结合起来作为奖励信号，用于更新语言模型。

**关键创新**：最重要的技术创新点在于引入了新颖性感知奖励。与现有方法仅依赖于自我确认信号不同，EVOL-RL通过鼓励模型探索不同的推理路径来防止多样性崩溃，从而提高模型的泛化能力。

**关键设计**：新颖性得分的计算是关键设计之一。论文中具体如何衡量推理过程的差异性未知。此外，如何平衡多数投票结果和新颖性得分在奖励信号中的权重也至关重要，具体实现细节未知。

## 📊 实验亮点

实验结果表明，EVOL-RL在无标签AIME24数据集上训练后，显著提升了Qwen3-4B-Base模型在AIME25数据集上的性能，pass@1指标从基线的4.6%提升到16.4%，pass@16指标从18.5%提升到37.9%。此外，EVOL-RL还提高了模型在GPQA、MMLU-Pro和BBEH等领域外任务上的泛化能力。

## 🎯 应用场景

EVOL-RL具有广泛的应用前景，可用于训练无需人工标注或外部反馈即可自我改进的语言模型。这对于资源有限或难以获取高质量标注数据的场景尤为重要。该方法可以应用于各种自然语言处理任务，例如问答、文本生成和机器翻译，并有望提升模型的鲁棒性和泛化能力。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly trained with reinforcement learning from verifiable rewards (RLVR), yet real-world deployment demands models that can self-improve without labels or external judges. Existing self-improvement approaches primarily rely on self-confirmation signals (e.g., confidence, entropy, or consistency) to generate rewards. This reliance drives models toward over-confident, majority-favored solutions, causing an entropy collapse that degrades pass@n and reasoning complexity. To address this, we propose EVOL-RL, a label-free framework that mirrors the evolutionary principle of balancing selection with variation. Concretely, EVOL-RL retains the majority-voted answer as an anchor for stability, but adds a novelty-aware reward that scores each sampled solution by how different its reasoning is from other concurrently generated responses. This majority-for-stability + novelty-for-exploration rule mirrors the variation-selection principle: selection prevents drift, while novelty prevents collapse. Evaluation results show that EVOL-RL consistently outperforms the majority-only baseline; e.g., training on label-free AIME24 lifts Qwen3-4B-Base AIME25 pass@1 from baseline's 4.6% to 16.4%, and pass@16 from 18.5% to 37.9%. EVOL-RL not only prevents in-domain diversity collapse but also improves out-of-domain generalization (from math reasoning to broader tasks, e.g., GPQA, MMLU-Pro, and BBEH). The code is available at: https://github.com/YujunZhou/EVOL-RL.

