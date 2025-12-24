---
layout: default
title: FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation with Vision-Language Models
---

# FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation with Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12835" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12835v1</a>
  <a href="https://arxiv.org/pdf/2505.12835.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12835v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12835v1', 'FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation with Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengxing Cai, Jinhan Dong, Jingjun Tan, Jingcheng Deng, Sihang Li, Zhifeng Gao, Haidong Wang, Zicheng Su, Agachai Sumalee, Renxin Zhong

**分类**: cs.CL, cs.CV

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出FlightGPT以解决无人机视觉语言导航中的多模态融合与可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机导航` `视觉语言模型` `多模态融合` `可解释性` `强化学习` `群体相对策略优化` `思维链推理` `城市导航`

## 📋 核心要点

1. 现有无人机视觉语言导航方法在多模态融合、泛化能力和可解释性方面存在显著不足，限制了其实际应用。
2. 本文提出FlightGPT框架，通过两阶段训练流程和基于思维链的推理机制，提升了无人机的导航能力和决策可解释性。
3. 在CityNav数据集上的实验结果显示，FlightGPT在所有场景中均达到了最先进的性能，成功率显著高于现有基线。

## 📝 摘要（中文）

无人机视觉语言导航（VLN）在灾害响应、物流配送和城市检查等应用中至关重要。然而，现有方法常常面临多模态融合不足、泛化能力弱和可解释性差等挑战。为了解决这些问题，本文提出了FlightGPT，一个基于视觉语言模型（VLM）的新型无人机VLN框架，具有强大的多模态感知能力。我们设计了一个两阶段的训练流程：首先，通过高质量示例进行监督微调（SFT），以改善初始化和结构化推理；然后，采用群体相对策略优化（GRPO）算法，结合考虑目标准确性、推理质量和格式合规性的复合奖励，提升泛化能力和适应性。此外，FlightGPT引入了基于思维链（CoT）的推理机制，以提高决策的可解释性。大量实验表明，FlightGPT在城市规模数据集CityNav上实现了所有场景的最先进性能，在未见环境中成功率比最强基线高出9.22%。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机视觉语言导航中的多模态融合不足、泛化能力弱和可解释性差的问题。现有方法在复杂环境中表现不佳，难以满足实际应用需求。

**核心思路**：FlightGPT框架通过引入两阶段的训练流程和基于思维链的推理机制，旨在提升无人机在视觉和语言导航任务中的表现和决策透明度。这样的设计能够有效整合多模态信息，增强模型的适应性和解释性。

**技术框架**：FlightGPT的整体架构包括两个主要阶段：首先是监督微调（SFT），利用高质量示例进行模型初始化和推理能力的提升；其次是群体相对策略优化（GRPO），通过复合奖励机制优化模型的决策过程。

**关键创新**：FlightGPT的核心创新在于引入了基于思维链的推理机制，这一机制能够有效提升模型的决策可解释性，与现有方法相比，显著改善了推理过程的透明度和准确性。

**关键设计**：在训练过程中，采用了复合奖励函数，考虑了目标准确性、推理质量和格式合规性等多个因素，以确保模型在不同环境中的泛化能力。同时，网络结构设计上注重多模态信息的融合，提升了整体性能。

## 📊 实验亮点

在CityNav数据集上的实验结果显示，FlightGPT在所有场景中均达到了最先进的性能，成功率比最强基线高出9.22%。这一显著提升证明了其在未见环境中的强大适应能力和决策质量。

## 🎯 应用场景

FlightGPT的研究成果在多个领域具有广泛的应用潜力，包括灾害响应、物流配送和城市检查等场景。通过提升无人机在复杂环境中的导航能力，该技术能够有效支持紧急救援、货物运输和基础设施监测等任务，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Unmanned Aerial Vehicle (UAV) Vision-and-Language Navigation (VLN) is vital for applications such as disaster response, logistics delivery, and urban inspection. However, existing methods often struggle with insufficient multimodal fusion, weak generalization, and poor interpretability. To address these challenges, we propose FlightGPT, a novel UAV VLN framework built upon Vision-Language Models (VLMs) with powerful multimodal perception capabilities. We design a two-stage training pipeline: first, Supervised Fine-Tuning (SFT) using high-quality demonstrations to improve initialization and structured reasoning; then, Group Relative Policy Optimization (GRPO) algorithm, guided by a composite reward that considers goal accuracy, reasoning quality, and format compliance, to enhance generalization and adaptability. Furthermore, FlightGPT introduces a Chain-of-Thought (CoT)-based reasoning mechanism to improve decision interpretability. Extensive experiments on the city-scale dataset CityNav demonstrate that FlightGPT achieves state-of-the-art performance across all scenarios, with a 9.22\% higher success rate than the strongest baseline in unseen environments. Our implementation is publicly available.

