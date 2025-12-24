---
layout: default
title: "GuirlVG: Incentivize GUI Visual Grounding via Empirical Exploration on Reinforcement Learning"
---

# GuirlVG: Incentivize GUI Visual Grounding via Empirical Exploration on Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04389" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04389v1</a>
  <a href="https://arxiv.org/pdf/2508.04389.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04389v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04389v1', 'GuirlVG: Incentivize GUI Visual Grounding via Empirical Exploration on Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weitai Kang, Bin Lei, Gaowen Liu, Caiwen Ding, Yan Yan

**分类**: cs.AI

**发布日期**: 2025-08-06

**备注**: 9 pages

---

## 💡 一句话要点

**提出GuirlVG以解决GUI视觉定位效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图形用户界面` `视觉定位` `强化学习` `多模态学习` `数据效率` `智能助手` `人机交互`

## 📋 核心要点

1. 现有的GUI-VG方法主要依赖于监督微调，存在数据需求高和训练成本大的问题。
2. GuirlVG通过强化学习和新颖的稳定化技术，优化了RFT的应用，提升了训练效率。
3. 实验结果显示，GuirlVG在少量样本下显著超越传统SFT方法，验证了其有效性。

## 📝 摘要（中文）

图形用户界面视觉定位（GUI-VG）是GUI代理的核心能力，传统上依赖于多模态大语言模型（MLLMs）的监督微调（SFT），这需要大量数据和高昂的训练成本。随着MLLMs的进步，SFT的必要性逐渐受到质疑。本文提出GuirlVG，一种基于强化学习的GUI-VG方法，通过系统的实证研究和新颖的稳定化技术，优化了强化微调（RFT）的应用。研究表明，GuirlVG在仅使用5.2K训练样本的情况下，超越了基于10M样本的SFT方法，分别在ScreenSpot、ScreenSpotPro和ScreenSpotV2上实现了7.7%、17.2%和91.9%的准确率提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有GUI-VG方法在数据需求和训练成本上的不足，尤其是传统的监督微调方法效率低下的问题。

**核心思路**：GuirlVG通过引入强化学习和对RFT的深入分析，提出了一种更高效的训练方式，旨在减少对大量标注数据的依赖。

**技术框架**：GuirlVG的整体架构包括数据采集、RFT的核心组件分解、动态稳定化机制和训练配置优化等多个模块，形成一个系统的训练流程。

**关键创新**：论文的主要创新在于提出了动态稳定化的对抗KL因子，旨在减轻奖励过度优化的问题，从而提升训练的稳定性和效果。

**关键设计**：在参数设置上，GuirlVG采用了针对RFT的优化配置，设计了新的损失函数以平衡探索与利用，同时在网络结构上进行了适当的调整，以适应GUI-VG的特定需求。

## 📊 实验亮点

GuirlVG在仅使用5.2K训练样本的情况下，分别在ScreenSpot、ScreenSpotPro和ScreenSpotV2上实现了7.7%、17.2%和91.9%的准确率提升，显著超越了基于10M样本的SFT方法，展示了其在GUI-VG领域的强大潜力。

## 🎯 应用场景

GuirlVG的研究成果在图形用户界面自动化、智能助手和人机交互等领域具有广泛的应用潜力。通过提高GUI-VG的效率，能够降低开发成本，提升用户体验，推动智能应用的普及与发展。

## 📄 摘要（原文）

> Graphical user interface visual grounding (GUI-VG), a core capability for GUI agents, has primarily relied on supervised fine-tuning (SFT) of multimodal large language models (MLLMs), which demands extensive data curation and significant training costs. However, as MLLMs continue to advance and even cover GUI domains during pretraining, the necessity of exhaustive SFT post-training becomes increasingly questionable. Meanwhile, recent successes of rule-based reinforcement fine-tuning (RFT) suggest a more efficient alternative. Despite this promise, the optimal manner of applying RFT for GUI-VG remains unexplored. To bridge this gap, we introduce GuirlVG, a reinforcement learning-based GUI-VG method built on a systematic empirical study and a novel stabilization technique. We find that naive application of RFT underperforms the SFT baseline, motivating a deeper exploration. First, we decompose RFT into its core components and analyze the optimal formulation of each. Second, we propose a novel Adversarial KL Factor that dynamically stabilizes training to mitigate reward over-optimization. Third, we further explore the training configurations of RFT to enhance effectiveness. Extensive experiments show that GuirlVG, with only 5.2K training samples, outperforms SFT methods trained on over 10M samples, achieving a 7.7% improvement on ScreenSpot, a 17.2% improvement on ScreenSpotPro, and 91.9% accuracy on ScreenSpotV2.

