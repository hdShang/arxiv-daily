---
layout: default
title: "OmniPlay: Benchmarking Omni-Modal Models on Omni-Modal Game Playing"
---

# OmniPlay: Benchmarking Omni-Modal Models on Omni-Modal Game Playing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04361" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04361v3</a>
  <a href="https://arxiv.org/pdf/2508.04361.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04361v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04361v3', 'OmniPlay: Benchmarking Omni-Modal Models on Omni-Modal Game Playing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fuqing Bie, Shiyu Huang, Xijia Tao, Zhiqin Fang, Leyi Pan, Junzhe Chen, Min Ren, Liuyu Xiang, Zhaofeng He

**分类**: cs.AI

**发布日期**: 2025-08-06 (更新: 2025-09-29)

**🔗 代码/项目**: [GITHUB](https://github.com/fuqingbie/omni-game-benchmark)

---

## 💡 一句话要点

**提出OmniPlay基准以评估多模态模型在动态游戏中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `动态游戏` `推理能力` `模态融合` `基准评估` `人工智能` `智能体`

## 📋 核心要点

1. 现有的多模态模型评估方法未能有效测试其在动态互动环境中的智能表现，存在明显的局限性。
2. 论文提出OmniPlay基准，通过设计五个游戏环境，系统性地测试智能体在跨模态推理中的能力，强调模态间的相互依赖性。
3. 实验结果显示，尽管模型在记忆任务上表现优异，但在需要复杂推理的任务中却存在严重的性能下降，揭示了融合机制的脆弱性。

## 📝 摘要（中文）

尽管像Gemini和GPT-4o这样的通用基础模型在多模态能力上表现出色，但现有评估未能测试其在动态互动世界中的智能。静态基准缺乏主动性，而互动基准则严重忽视关键的听觉和时间线索。为填补这一评估空白，本文提出了OmniPlay，一个旨在评估和探测智能体模型在全感官范围内融合与推理能力的诊断基准。OmniPlay包含五个游戏环境，系统性地创建协同与冲突场景，迫使智能体进行真实的跨模态推理。对六个领先的多模态模型的综合评估显示，它们在高保真记忆任务上表现超人，但在需要强大推理和战略规划的挑战中却存在系统性失败。我们发现这种脆弱性源于脆弱的融合机制，导致在模态冲突下性能急剧下降，并揭示了一个反直觉的“少即是多”悖论，即去除感官信息反而可以改善性能。我们的研究表明，通往强人工智能的道路需要超越规模，明确关注协同融合。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态模型在动态互动环境中评估不足的问题。现有方法往往忽视了关键的听觉和时间信息，导致评估结果不全面。

**核心思路**：OmniPlay基准的核心思想是通过创建多样化的游戏环境，迫使智能体进行真实的跨模态推理，从而全面评估其融合与推理能力。

**技术框架**：OmniPlay包含五个游戏环境，设计上既有协同又有冲突的场景，智能体必须在这些环境中进行决策。评估过程中，模型的表现通过多种任务进行综合考量。

**关键创新**：该研究的主要创新在于强调模态间的相互依赖性，揭示了在模态冲突下，传统的融合机制可能导致性能的急剧下降。

**关键设计**：在设计中，采用了多种任务和评估指标，确保模型在不同场景下的表现被全面考量。同时，研究中还探讨了去除某些感官信息对模型性能的影响，提出了“少即是多”的观点。

## 📊 实验亮点

实验结果表明，六个领先的多模态模型在高保真记忆任务中表现超人，但在复杂推理和战略规划任务中却普遍存在性能下降，显示出系统性失败。这一发现强调了模态融合机制的脆弱性，并提出了去除感官信息可能改善性能的反直觉现象。

## 🎯 应用场景

OmniPlay基准的潜在应用领域包括游戏AI、机器人控制和智能助手等。通过更全面的评估方法，研究者可以更好地理解多模态模型的能力和局限性，从而推动更强大和智能的人工智能系统的发展。

## 📄 摘要（原文）

> While generalist foundation models like Gemini and GPT-4o demonstrate impressive multi-modal competence, existing evaluations fail to test their intelligence in dynamic, interactive worlds. Static benchmarks lack agency, while interactive benchmarks suffer from a severe modal bottleneck, typically ignoring crucial auditory and temporal cues. To bridge this evaluation chasm, we introduce OmniPlay, a diagnostic benchmark designed not just to evaluate, but to probe the fusion and reasoning capabilities of agentic models across the full sensory spectrum. Built on a core philosophy of modality interdependence, OmniPlay comprises a suite of five game environments that systematically create scenarios of both synergy and conflict, forcing agents to perform genuine cross-modal reasoning. Our comprehensive evaluation of six leading omni-modal models reveals a critical dichotomy: they exhibit superhuman performance on high-fidelity memory tasks but suffer from systemic failures in challenges requiring robust reasoning and strategic planning. We demonstrate that this fragility stems from brittle fusion mechanisms, which lead to catastrophic performance degradation under modality conflict and uncover a counter-intuitive "less is more" paradox, where removing sensory information can paradoxically improve performance. Our findings suggest that the path toward robust AGI requires a research focus beyond scaling to explicitly address synergistic fusion. Our platform is available for anonymous review at https://github.com/fuqingbie/omni-game-benchmark.

