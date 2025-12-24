---
layout: default
title: "F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions"
---

# F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06951" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06951v2</a>
  <a href="https://arxiv.org/pdf/2509.06951.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06951v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06951v2', 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Lv, Weijie Kong, Hao Li, Jia Zeng, Zherui Qiu, Delin Qu, Haoming Song, Qizhi Chen, Xiang Deng, Jiangmiao Pang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-08 (更新: 2025-09-09)

**备注**: Homepage: https://aopolin-lv.github.io/F1-VLA/

---

## 💡 一句话要点

**F1模型：通过视觉预测连接理解、生成与动作，提升具身智能任务性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `视觉预测` `具身智能` `Transformer` `逆动力学` `长期规划` `动态环境`

## 📋 核心要点

1. 现有VLA模型在动态环境中表现出短视行为和鲁棒性不足，难以有效执行语言条件任务。
2. F1模型通过视觉预测生成显式规划目标，将动作生成转化为预测引导的逆动力学问题。
3. F1模型在包含大量任务的数据集上进行三阶段训练，显著提升了任务成功率和泛化能力。

## 📝 摘要（中文）

本文提出了一种名为F1的预训练视觉-语言-动作（VLA）框架，旨在解决具身AI中动态视觉环境下语言条件任务的执行问题。现有VLA模型主要采用反应式的状态-动作映射，导致短视行为和在动态场景中的鲁棒性较差。F1集成了视觉预测生成到决策流程中，采用混合Transformer架构，包含感知、预测生成和控制等专用模块，从而连接理解、生成和动作。F1的核心是下一尺度预测机制，合成目标条件下的视觉预测作为显式规划目标。通过预测未来可能的视觉状态，F1将动作生成重构为预测引导的逆动力学问题，从而实现隐式地达成视觉目标的动作。为了赋予F1鲁棒性和泛化能力，本文提出了一个三阶段训练方案，在一个包含超过33万条轨迹和136个不同任务的大型数据集上进行训练。该训练方案增强了模块化推理，并使模型具备可迁移的视觉预测能力，这对于复杂和动态环境至关重要。在真实世界任务和模拟基准上的大量评估表明，F1始终优于现有方法，在任务成功率和泛化能力方面都取得了显著提升。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在动态环境中执行语言条件任务时，主要依赖反应式的状态-动作映射，缺乏对未来状态的预测和规划，导致短视行为，难以应对复杂和动态的环境，鲁棒性较差。因此，需要一种能够进行长期规划并适应动态环境的VLA模型。

**核心思路**：F1模型的核心思路是将视觉预测融入到决策过程中，通过预测未来可能的视觉状态作为显式的规划目标，从而指导动作的生成。这种方法将动作生成问题转化为一个预测引导的逆动力学问题，使得模型能够生成隐式地达成视觉目标的动作，从而实现长期规划和鲁棒性。

**技术框架**：F1模型采用混合Transformer架构，包含三个主要模块：感知模块、预测生成模块和控制模块。感知模块负责从视觉输入中提取特征；预测生成模块基于感知特征和目标条件，预测未来可能的视觉状态；控制模块则根据预测的未来状态和当前状态，生成相应的动作。整个流程可以概括为：视觉输入 -> 感知 -> 目标条件 -> 视觉预测 -> 控制 -> 动作。

**关键创新**：F1模型的关键创新在于其视觉预测机制和三阶段训练方案。视觉预测机制通过预测未来状态，为动作生成提供显式目标，从而实现长期规划。三阶段训练方案则增强了模型的模块化推理能力和可迁移的视觉预测能力，使其能够更好地适应复杂和动态的环境。

**关键设计**：F1模型使用了下一尺度预测机制，具体实现细节未知。三阶段训练方案包括：第一阶段，预训练感知模块和预测生成模块；第二阶段，微调整个模型，使其能够生成有效的动作；第三阶段，使用强化学习进一步优化模型的性能。损失函数的设计也至关重要，可能包括预测损失、动作损失和奖励损失等，具体细节未知。

## 📊 实验亮点

F1模型在真实世界任务和模拟基准上进行了广泛的评估，实验结果表明，F1模型始终优于现有方法，在任务成功率和泛化能力方面都取得了显著提升。具体的性能数据和提升幅度在论文中进行了详细的展示，证明了F1模型的有效性和优越性。

## 🎯 应用场景

F1模型具有广泛的应用前景，可应用于机器人导航、物体操作、自动驾驶等领域。通过赋予机器人更强的视觉预测和规划能力，F1模型可以帮助机器人在复杂和动态的环境中更好地完成任务，提高其自主性和智能化水平，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.

