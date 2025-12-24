---
layout: default
title: Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation
---

# Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08364" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08364v2</a>
  <a href="https://arxiv.org/pdf/2505.08364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08364v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08364v2', 'Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Enci Zhang, Xingang Yan, Wei Lin, Tianxiang Zhang, Qianchun Lu

**分类**: cs.AI

**发布日期**: 2025-05-13 (更新: 2025-09-17)

**备注**: 14 pages, 3 figs

---

## 💡 一句话要点

**提出自适应难度课程学习与专家引导自我重构以提升LLM推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `课程学习` `自我重构` `强化学习` `数学推理` `知识吸收`

## 📋 核心要点

1. 现有大型语言模型在解决复杂问题时表现不稳定，尤其是在数学推理方面存在显著挑战。
2. 提出自适应难度课程学习和专家引导自我重构两种新策略，以提升模型的推理能力和知识吸收。
3. 在使用Qwen2.5-7B模型的实验中，这些策略的结合使得模型在AIME24基准上提升了10%，在AIME25基准上提升了16.6%。

## 📝 摘要（中文）

尽管在数学推理等领域取得了显著进展，大型语言模型在持续解决复杂问题方面仍面临重大挑战。本文提出了两种新策略以增强大型语言模型的能力。首先，自适应难度课程学习（ADCL）通过定期重新评估即将到来的数据批次的难度，解决了模型在训练过程中对问题难度的动态感知变化。其次，专家引导自我重构（EGSR）通过引导模型在自身概念框架内重构专家解决方案，促进了更深层次的理解和知识吸收。大量实验表明，这些人类启发的策略协同作用显著提升了模型性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂问题推理中的不稳定性，特别是模型对问题难度的感知变化导致的性能波动。现有方法未能有效应对这一挑战。

**核心思路**：提出自适应难度课程学习（ADCL）和专家引导自我重构（EGSR）两种策略，前者通过动态调整训练难度，后者通过引导模型在自身框架内重构解决方案，促进深层理解。

**技术框架**：整体架构包括两个主要模块：ADCL模块负责动态评估和调整问题难度，EGSR模块则通过强化学习引导模型进行自我重构，二者协同工作以提升推理能力。

**关键创新**：ADCL解决了模型在训练过程中对问题难度的动态感知变化，EGSR则通过引导而非直接模仿的方式促进了更深层次的知识吸收，这与现有的单一模仿学习方法有本质区别。

**关键设计**：在ADCL中，难度评估采用了基于模型当前能力的动态调整机制；EGSR中，设计了特定的奖励机制以鼓励模型在自我重构过程中进行探索与创新。

## 📊 实验亮点

实验结果显示，结合自适应难度课程学习和专家引导自我重构后，模型在AIME24基准上性能提升了10%，在AIME25基准上提升了16.6%，显著优于标准的Zero-RL基线，展示了这两种策略的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和复杂问题求解等。通过提升大型语言模型的推理能力，可以在更广泛的场景中应用，如自动化问题解答、个性化学习和智能助手等，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Despite impressive progress in areas like mathematical reasoning, large language models still face significant challenges in consistently solving complex problems. Drawing inspiration from key human learning strategies, we propose two novel strategies to enhance the capability of large language models to solve these complex problems. First, Adaptive Difficulty Curriculum Learning (ADCL) is a novel curriculum learning strategy that tackles the Difficulty Shift phenomenon (i.e., a model's perception of problem difficulty dynamically changes during training) by periodically re-estimating difficulty within upcoming data batches to maintain alignment with the model's evolving capabilities. Second, Expert-Guided Self-Reformulation (EGSR) is a novel reinforcement learning strategy that bridges the gap between imitation learning and pure exploration by guiding models to reformulate expert solutions within their own conceptual framework, rather than relying on direct imitation, fostering deeper understanding and knowledge assimilation. Extensive experiments on challenging mathematical reasoning benchmarks, using Qwen2.5-7B as the base model, demonstrate that these human-inspired strategies synergistically and significantly enhance performance. Notably, their combined application improves performance over the standard Zero-RL baseline by 10% on the AIME24 benchmark and 16.6% on AIME25.

