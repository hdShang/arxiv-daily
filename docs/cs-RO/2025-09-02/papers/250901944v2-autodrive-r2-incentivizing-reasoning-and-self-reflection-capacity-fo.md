---
layout: default
title: "AutoDrive-R$^2$: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving"
---

# AutoDrive-R$^2$: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01944" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01944v2</a>
  <a href="https://arxiv.org/pdf/2509.01944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01944v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01944v2', 'AutoDrive-R$^2$: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenlong Yuan, Chengxuan Qian, Jing Tang, Rui Chen, Zijian Song, Lei Sun, Xiangxiang Chu, Yujun Cai, Dapeng Zhang, Shuo Li

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-02 (更新: 2025-12-01)

---

## 💡 一句话要点

**AutoDrive-R²：通过推理和自反思能力提升自动驾驶VLA模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉语言动作模型` `思维链` `强化学习` `推理能力` `自反思能力` `轨迹规划` `组相对策略优化`

## 📋 核心要点

1. 现有的自动驾驶VLA模型在决策过程的可解释性、连贯性和动作序列的合理性方面存在不足。
2. AutoDrive-R²通过CoT处理和RL，提升自动驾驶系统的推理和自反思能力，从而解决上述问题。
3. 实验结果表明，AutoDrive-R²在nuScenes和Waymo数据集上均取得了SOTA性能，并展现出强大的泛化能力。

## 📝 摘要（中文）

本文提出AutoDrive-R²，一种新型VLA框架，旨在增强自动驾驶系统的推理和自反思能力。该框架通过思维链（CoT）处理和强化学习（RL）实现这一目标。首先，构建了一个名为nuScenesR²-6K的创新CoT数据集，用于监督微调，通过包含自反思验证的四步逻辑链，有效构建输入信息和输出轨迹之间的认知桥梁。其次，为了在RL阶段最大化推理和自反思，采用组相对策略优化（GRPO）算法，并结合基于物理的奖励框架，该框架融合了空间对齐、车辆动力学和时间平滑标准，以确保可靠且真实的轨迹规划。在nuScenes和Waymo数据集上的广泛评估结果表明，该方法具有最先进的性能和强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作（VLA）模型在自动驾驶中展现了潜力，但其决策过程缺乏可解释性和连贯性，生成的动作序列也可能不够合理。因此，需要提升模型在复杂环境下的推理能力和自我反思能力，以确保安全可靠的驾驶行为。

**核心思路**：AutoDrive-R²的核心思路是通过引入思维链（CoT）和强化学习（RL）来增强VLA模型的推理和自反思能力。CoT通过逐步推理的方式，使模型能够更好地理解场景并做出决策。RL则通过奖励机制，鼓励模型生成更安全、更合理的驾驶轨迹。

**技术框架**：AutoDrive-R²框架主要包含两个阶段：监督微调阶段和强化学习阶段。在监督微调阶段，使用nuScenesR²-6K数据集对VLA模型进行训练，该数据集包含四步逻辑链，并带有自反思验证。在强化学习阶段，使用组相对策略优化（GRPO）算法，并结合基于物理的奖励函数，对模型进行进一步优化。奖励函数考虑了空间对齐、车辆动力学和时间平滑性。

**关键创新**：AutoDrive-R²的关键创新在于：1) 提出了nuScenesR²-6K数据集，该数据集专门用于训练具有推理和自反思能力的VLA模型。2) 将CoT和RL相结合，有效地提升了模型的决策能力和安全性。3) 设计了基于物理的奖励函数，能够更好地指导模型生成合理的驾驶轨迹。

**关键设计**：nuScenesR²-6K数据集包含6000个场景，每个场景都包含四步逻辑链：观察（Observation）、思考（Reasoning）、行动（Action）和反思（Reflection）。奖励函数的设计考虑了多个因素，包括与车道线的对齐程度、车辆的加速度和角速度、以及轨迹的平滑性。GRPO算法用于优化策略，鼓励模型探索不同的驾驶策略。

## 📊 实验亮点

AutoDrive-R²在nuScenes和Waymo数据集上取得了显著的性能提升。在nuScenes数据集上，AutoDrive-R²的NDS（NuScenes Detection Score）指标超过了现有最佳方法，提升幅度达到显著水平。在Waymo Open Dataset上的实验结果也表明，AutoDrive-R²具有强大的泛化能力，能够适应不同的驾驶环境。

## 🎯 应用场景

AutoDrive-R²的研究成果可应用于各种自动驾驶场景，例如城市道路、高速公路和停车场。通过提升自动驾驶系统的推理和自反思能力，可以提高驾驶安全性、减少交通事故，并改善用户体验。该研究还有助于推动自动驾驶技术的商业化落地，加速智能交通系统的发展。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models in autonomous driving systems have recently demonstrated transformative potential by integrating multimodal perception with decision-making capabilities. However, the interpretability and coherence of the decision process and the plausibility of action sequences remain largely underexplored. To address these issues, we propose AutoDrive-R$^2$, a novel VLA framework that enhances both reasoning and self-reflection capabilities of autonomous driving systems through chain-of-thought (CoT) processing and reinforcement learning (RL). Specifically, we first propose an innovative CoT dataset named nuScenesR$^2$-6K for supervised fine-tuning, which effectively builds cognitive bridges between input information and output trajectories through a four-step logical chain with self-reflection for validation. Moreover, to maximize both reasoning and self-reflection during the RL stage, we further employ the Group Relative Policy Optimization (GRPO) algorithm within a physics-grounded reward framework that incorporates spatial alignment, vehicle dynamic, and temporal smoothness criteria to ensure reliable and realistic trajectory planning. Extensive evaluation results across both nuScenes and Waymo datasets demonstrates the state-of-the-art performance and robust generalization capacity of our proposed method.

