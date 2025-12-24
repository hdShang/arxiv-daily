---
layout: default
title: "Integrating Offline Pre-Training with Online Fine-Tuning: A Reinforcement Learning Approach for Robot Social Navigation"
---

# Integrating Offline Pre-Training with Online Fine-Tuning: A Reinforcement Learning Approach for Robot Social Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00466" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00466v1</a>
  <a href="https://arxiv.org/pdf/2510.00466.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00466v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00466v1', 'Integrating Offline Pre-Training with Online Fine-Tuning: A Reinforcement Learning Approach for Robot Social Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Run Su, Hao Fu, Shuai Zhou, Yingao Fu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**提出基于RTG预测的离线-在线强化学习算法，用于提升机器人社交导航能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人社交导航` `离线强化学习` `在线微调` `Return-to-Go预测` `Transformer` `时空融合` `分布偏移`

## 📋 核心要点

1. 现有机器人社交导航方法受限于行人行为的不确定性以及训练期间有限的环境交互，导致次优探索和分布偏移。
2. 论文提出一种基于Return-to-Go预测的离线-在线强化学习算法，通过时空融合模型精确估计RTG值，缓解分布偏移。
3. 实验结果表明，该方法在模拟社交导航环境中实现了更高的成功率和更低的碰撞率，提升了导航策略的鲁棒性和适应性。

## 📝 摘要（中文）

本文提出了一种新颖的离线到在线微调强化学习算法，用于解决机器人社交导航问题。该算法将Return-to-Go (RTG) 预测集成到因果Transformer架构中。通过联合编码时间行人运动模式和空间人群动态，算法中的时空融合模型能够精确地实时估计RTG值。这种RTG预测框架通过对齐离线策略训练和在线环境交互来缓解分布偏移。此外，构建了一种混合离线-在线经验采样机制，以稳定微调期间的策略更新，确保预训练知识和实时适应的平衡集成。在模拟社交导航环境中的大量实验表明，与最先进的基线方法相比，该方法实现了更高的成功率和更低的碰撞率。这些结果突显了该算法在增强导航策略鲁棒性和适应性方面的有效性。这项工作为现实世界应用中更可靠和自适应的机器人导航系统铺平了道路。

## 🔬 方法详解

**问题定义**：机器人社交导航任务旨在使机器人在人群中安全、高效地导航。现有方法，尤其是离线强化学习方法，面临着行人行为预测的不确定性以及离线训练与在线部署之间的分布偏移问题，导致导航策略的泛化能力不足。现有方法难以平衡离线预训练的知识和在线环境的实时适应。

**核心思路**：论文的核心思路是利用Return-to-Go (RTG) 预测来桥接离线训练和在线微调之间的差距。通过精确预测RTG值，可以指导机器人在在线环境中的探索，并缓解分布偏移。同时，结合离线和在线经验，稳定策略更新，实现知识迁移和实时适应的平衡。

**技术框架**：该算法的技术框架主要包括三个部分：1) 基于因果Transformer的时空融合模型，用于实时估计RTG值；2) RTG预测框架，用于对齐离线策略训练和在线环境交互；3) 混合离线-在线经验采样机制，用于稳定策略更新。整体流程是首先利用离线数据预训练策略，然后利用在线数据进行微调，同时利用RTG预测指导探索和缓解分布偏移。

**关键创新**：该论文的关键创新在于将Return-to-Go (RTG) 预测集成到离线-在线强化学习框架中，并设计了时空融合模型来精确估计RTG值。与现有方法相比，该方法能够更有效地缓解分布偏移，并实现离线知识和在线适应的平衡。此外，混合经验采样机制也提升了策略更新的稳定性。

**关键设计**：时空融合模型采用因果Transformer架构，联合编码时间行人运动模式和空间人群动态。RTG预测框架通过最小化预测RTG值与实际RTG值之间的差异来训练。混合经验采样机制根据一定的比例从离线和在线经验池中采样数据，用于策略更新。具体的参数设置和损失函数细节在论文中未明确说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在模拟社交导航环境中取得了显著的性能提升。与最先进的基线方法相比，该方法实现了更高的成功率和更低的碰撞率，证明了其在增强导航策略鲁棒性和适应性方面的有效性。具体的性能提升数据未在摘要中给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于各种需要机器人与人交互的场景，例如商场导览机器人、医院配送机器人、餐厅服务机器人等。通过提升机器人在复杂人群环境中的导航能力，可以提高服务效率和用户体验，并降低安全风险。未来，该技术有望推动机器人更广泛地应用于日常生活和社会服务中。

## 📄 摘要（原文）

> Offline reinforcement learning (RL) has emerged as a promising framework for addressing robot social navigation challenges. However, inherent uncertainties in pedestrian behavior and limited environmental interaction during training often lead to suboptimal exploration and distributional shifts between offline training and online deployment. To overcome these limitations, this paper proposes a novel offline-to-online fine-tuning RL algorithm for robot social navigation by integrating Return-to-Go (RTG) prediction into a causal Transformer architecture. Our algorithm features a spatiotem-poral fusion model designed to precisely estimate RTG values in real-time by jointly encoding temporal pedestrian motion patterns and spatial crowd dynamics. This RTG prediction framework mitigates distribution shift by aligning offline policy training with online environmental interactions. Furthermore, a hybrid offline-online experience sampling mechanism is built to stabilize policy updates during fine-tuning, ensuring balanced integration of pre-trained knowledge and real-time adaptation. Extensive experiments in simulated social navigation environments demonstrate that our method achieves a higher success rate and lower collision rate compared to state-of-the-art baselines. These results underscore the efficacy of our algorithm in enhancing navigation policy robustness and adaptability. This work paves the way for more reliable and adaptive robotic navigation systems in real-world applications.

