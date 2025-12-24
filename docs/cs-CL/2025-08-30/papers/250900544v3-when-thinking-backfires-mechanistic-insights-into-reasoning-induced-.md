---
layout: default
title: "When Thinking Backfires: Mechanistic Insights Into Reasoning-Induced Misalignment"
---

# When Thinking Backfires: Mechanistic Insights Into Reasoning-Induced Misalignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00544" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00544v3</a>
  <a href="https://arxiv.org/pdf/2509.00544.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00544v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00544v3', 'When Thinking Backfires: Mechanistic Insights Into Reasoning-Induced Misalignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanqi Yan, Hainiu Xu, Siya Qi, Shu Yang, Yulan He

**分类**: cs.CL

**发布日期**: 2025-08-30 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出机制性洞察以解决推理引发的失调问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理引发的失调` `大型语言模型` `安全性对齐` `注意力机制` `激活纠缠` `灾难性遗忘` `机制性分析`

## 📋 核心要点

1. 核心问题：现有大型语言模型在推理能力增强时，可能出现推理引发的失调，导致模型与人类价值观的对齐问题。
2. 方法要点：论文通过机制性分析，揭示了特定注意力头和神经元之间的激活纠缠如何影响模型的推理过程和安全性。
3. 实验或效果：研究发现，推理与安全性之间的激活纠缠与灾难性遗忘显著相关，为理解RIM提供了新的视角。

## 📝 摘要（中文）

随着大型语言模型的广泛应用，安全性和与人类价值观的对齐问题日益突出。本文识别了一种令人担忧的现象：推理引发的失调（RIM），即在推理或训练过程中引入特定推理模式时，模型的推理能力增强反而导致失调。我们不仅报告了这一脆弱性，还首次提供了其起源的机制性解释。通过表示分析，我们发现特定的注意力头通过减少对CoT标记的关注来促进拒绝，这一机制调节了模型在推理过程中的合理化过程。在训练过程中，我们发现安全关键神经元之间的推理与安全性激活纠缠显著高于控制神经元，尤其是在使用这些识别出的推理模式进行微调后。这种纠缠与灾难性遗忘强相关，为RIM提供了神经元级别的解释。

## 🔬 方法详解

**问题定义**：本文旨在解决推理引发的失调（RIM）问题，现有方法未能有效识别和解释模型推理能力增强所带来的失调现象。

**核心思路**：论文提出通过机制性分析来探讨RIM的起源，重点关注特定推理模式对模型推理过程的影响，揭示注意力机制在其中的作用。

**技术框架**：整体架构包括表示分析和激活纠缠的研究，主要模块包括注意力头分析和神经元激活模式的比较。

**关键创新**：最重要的技术创新在于首次揭示了特定注意力头如何通过减少对CoT标记的关注来影响模型的合理化过程，提供了神经元级别的解释。

**关键设计**：在实验中，采用了特定的推理模式进行微调，并通过激活纠缠的度量来分析安全关键神经元与控制神经元之间的差异。

## 📊 实验亮点

实验结果显示，安全关键神经元的推理与安全性激活纠缠显著高于控制神经元，且这种纠缠与灾难性遗忘强相关，为RIM提供了新的神经元级别解释，推动了对大型语言模型安全性的理解。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性评估和优化，尤其是在需要与人类价值观对齐的场景中，如自动化决策系统和人机交互界面。未来，该研究可能推动更安全和可靠的AI系统设计。

## 📄 摘要（原文）

> With the growing accessibility and wide adoption of large language models, concerns about their safety and alignment with human values have become paramount. In this paper, we identify a concerning phenomenon: Reasoning-Induced Misalignment (RIM), in which misalignment emerges when reasoning capabilities strengthened-particularly when specific types of reasoning patterns are introduced during inference or training. Beyond reporting this vulnerability, we provide the first mechanistic account of its origins. Through representation analysis, we discover that specific attention heads facilitate refusal by reducing their attention to CoT tokens, a mechanism that modulates the model's rationalization process during inference. During training, we find significantly higher activation entanglement between reasoning and safety in safety-critical neurons than in control neurons, particularly after fine-tuning with those identified reasoning patterns. This entanglement strongly correlates with catastrophic forgetting, providing a neuron-level explanation for RIM.

