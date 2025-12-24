---
layout: default
title: "WoMAP: World Models For Embodied Open-Vocabulary Object Localization"
---

# WoMAP: World Models For Embodied Open-Vocabulary Object Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01600" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01600v1</a>
  <a href="https://arxiv.org/pdf/2506.01600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01600v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01600v1', 'WoMAP: World Models For Embodied Open-Vocabulary Object Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tenny Yin, Zhiting Mei, Tao Sun, Lihan Zha, Emily Zhou, Jeremy Bao, Miyu Yamane, Ola Shorinwa, Anirudha Majumdar

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-06-02

---

## 💡 一句话要点

**提出WoMAP以解决机器人开放词汇物体定位问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇定位` `主动感知` `高斯点云` `物体检测` `潜在世界模型`

## 📋 核心要点

1. 现有方法在开放词汇物体定位中难以超越演示数据集，导致泛化能力不足。
2. WoMAP通过高斯点云生成数据，提取开放词汇物体检测器的奖励信号，并利用潜在世界模型进行动态预测。
3. 实验结果显示，WoMAP在零-shot物体定位任务中成功率显著提高，超越了现有基线方法。

## 📝 摘要（中文）

语言指导的主动物体定位是机器人面临的一项重要挑战，要求在部分可观察环境中高效探索。然而，现有方法在超越演示数据集的泛化能力上存在困难，或无法生成物理上合理的动作。为了解决这些问题，我们提出了WoMAP（世界模型用于主动感知）：一种训练开放词汇物体定位策略的方法，采用基于高斯点云的真实到模拟再到真实的管道，能够在不需要专家演示的情况下进行可扩展的数据生成，并从开放词汇物体检测器中提取密集奖励信号，同时利用潜在世界模型进行动态和奖励预测，以在推理时为高层次动作提案提供基础。严格的仿真和硬件实验表明，WoMAP在广泛的零-shot物体定位任务中表现优越，成功率比VLM和扩散策略基线分别高出9倍和2倍。此外，我们还展示了WoMAP在TidyBot上的强泛化能力和模拟到真实的迁移效果。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在开放词汇物体定位中的挑战，现有方法如模仿学习和视觉语言模型（VLM）在泛化和生成物理合理动作方面存在不足。

**核心思路**：WoMAP提出了一种新的训练框架，结合高斯点云生成、奖励信号提取和潜在世界模型，旨在提高物体定位的效率和准确性。

**技术框架**：该方法包括三个主要模块：1) 高斯点云生成模块用于数据生成；2) 开放词汇物体检测器提取奖励信号；3) 潜在世界模型用于动态和奖励预测，确保高层次动作的物理合理性。

**关键创新**：WoMAP的核心创新在于其无需专家演示的可扩展数据生成能力，以及通过潜在世界模型实现的动态和奖励预测，这与传统方法的依赖于演示数据的方式有本质区别。

**关键设计**：在参数设置上，WoMAP优化了高斯点云生成的参数，并设计了适合开放词汇物体检测的损失函数，以确保模型在训练过程中能够有效学习物体定位的策略。具体的网络结构和训练细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，WoMAP在零-shot物体定位任务中的成功率比VLM高出9倍，比扩散策略基线高出2倍，展示了其在开放词汇物体定位中的显著优势和强泛化能力。

## 🎯 应用场景

WoMAP的研究成果在机器人自主导航、智能家居、仓储自动化等领域具有广泛的应用潜力。通过提高机器人在复杂环境中的物体定位能力，能够显著提升其自主决策和执行任务的效率，推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> Language-instructed active object localization is a critical challenge for robots, requiring efficient exploration of partially observable environments. However, state-of-the-art approaches either struggle to generalize beyond demonstration datasets (e.g., imitation learning methods) or fail to generate physically grounded actions (e.g., VLMs). To address these limitations, we introduce WoMAP (World Models for Active Perception): a recipe for training open-vocabulary object localization policies that: (i) uses a Gaussian Splatting-based real-to-sim-to-real pipeline for scalable data generation without the need for expert demonstrations, (ii) distills dense rewards signals from open-vocabulary object detectors, and (iii) leverages a latent world model for dynamics and rewards prediction to ground high-level action proposals at inference time. Rigorous simulation and hardware experiments demonstrate WoMAP's superior performance in a broad range of zero-shot object localization tasks, with more than 9x and 2x higher success rates compared to VLM and diffusion policy baselines, respectively. Further, we show that WoMAP achieves strong generalization and sim-to-real transfer on a TidyBot.

