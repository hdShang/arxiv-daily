---
layout: default
title: "ThinkDial: An Open Recipe for Controlling Reasoning Effort in Large Language Models"
---

# ThinkDial: An Open Recipe for Controlling Reasoning Effort in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18773" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18773v1</a>
  <a href="https://arxiv.org/pdf/2508.18773.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18773v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18773v1', 'ThinkDial: An Open Recipe for Controlling Reasoning Effort in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianyu He, Siyu Yuan, Xuefeng Li, Mingxuan Wang, Jiangjie Chen

**分类**: cs.CL

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出ThinkDial以解决大语言模型推理控制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理控制` `开源框架` `强化学习` `性能优化`

## 📋 核心要点

1. 现有方法在控制大语言模型的推理能力和计算资源方面存在显著挑战，尤其是在开源社区中缺乏有效的解决方案。
2. 论文提出的ThinkDial框架通过引入三种可控推理模式，实现了对推理过程的灵活控制，优化了计算资源的使用。
3. 实验结果表明，ThinkDial在保持性能阈值的同时，实现了响应长度的显著减少，展现出良好的压缩性能和泛化能力。

## 📝 摘要（中文）

大语言模型（LLMs）通过链式推理展现了卓越的问题解决能力，但在实际应用中控制其计算努力仍然是一个重大挑战。近期的专有系统如OpenAI的gpt-oss系列引入了直观的推理控制模式，但开源社区在这方面的进展有限。本文提出了ThinkDial，这是第一个开放式端到端框架，成功实现了gpt-oss风格的可控推理。该系统支持在三种不同推理模式之间无缝切换：高模式（完全推理能力）、中模式（50%令牌减少，性能下降<10%）和低模式（75%令牌减少，性能下降<15%）。通过端到端的训练范式，ThinkDial在整个流程中集成了预算模式控制，展现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在实际应用中推理控制的难题，现有方法在资源管理和性能平衡方面存在不足。

**核心思路**：ThinkDial通过引入三种不同的推理模式，允许用户根据需求灵活调整计算资源，从而实现高效的推理控制。

**技术框架**：该框架包括预算模式监督微调和两阶段的预算感知强化学习，确保在整个训练过程中嵌入可控推理能力。

**关键创新**：ThinkDial的主要创新在于其开放式设计和端到端的训练流程，使得可控推理成为可能，显著区别于现有的专有系统。

**关键设计**：在训练过程中，采用了适应性奖励塑形的强化学习策略，并设置了不同的令牌减少比例，以实现性能与计算资源的最佳平衡。

## 📊 实验亮点

实验结果显示，ThinkDial在高模式下实现了完整的推理能力，而在中模式和低模式下分别实现了50%和75%的令牌减少，性能下降均低于10%和15%。这一压缩性能的提升在保持响应质量的同时，显著降低了计算资源的消耗。

## 🎯 应用场景

ThinkDial的研究成果在多个领域具有广泛的应用潜力，包括智能助手、自动化客服和教育技术等。通过灵活控制推理能力，该框架能够在资源受限的环境中提供高效的服务，提升用户体验。未来，该技术可能推动更多开源大语言模型的实用化进程。

## 📄 摘要（原文）

> Large language models (LLMs) with chain-of-thought reasoning have demonstrated remarkable problem-solving capabilities, but controlling their computational effort remains a significant challenge for practical deployment. Recent proprietary systems like OpenAI's gpt-oss series have introduced discrete operational modes for intuitive reasoning control, but the open-source community has largely failed to achieve such capabilities. In this paper, we introduce ThinkDial, the first open-recipe end-to-end framework that successfully implements gpt-oss-style controllable reasoning through discrete operational modes. Our system enables seamless switching between three distinct reasoning regimes: High mode (full reasoning capability), Medium mode (50 percent token reduction with <10 percent performance degradation), and Low mode (75 percent token reduction with <15 percent performance degradation). We achieve this through an end-to-end training paradigm that integrates budget-mode control throughout the entire pipeline: budget-mode supervised fine-tuning that embeds controllable reasoning capabilities directly into the learning process, and two-phase budget-aware reinforcement learning with adaptive reward shaping. Extensive experiments demonstrate that ThinkDial achieves target compression-performance trade-offs with clear response length reductions while maintaining performance thresholds. The framework also exhibits strong generalization capabilities on out-of-distribution tasks.

