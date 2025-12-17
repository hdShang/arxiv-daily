---
layout: default
title: Guiding the Inner Eye: A Framework for Hierarchical and Flexible Visual Grounded Reasoning
---

# Guiding the Inner Eye: A Framework for Hierarchical and Flexible Visual Grounded Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22172" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22172v1</a>
  <a href="https://arxiv.org/pdf/2511.22172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22172v1" onclick="toggleFavorite(this, '2511.22172v1', 'Guiding the Inner Eye: A Framework for Hierarchical and Flexible Visual Grounded Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoyang Wei, Wenchao Ding, Yanchao Hao, Xi Chen

**分类**: cs.CV

**发布日期**: 2025-11-27

**备注**: 9pages

---

## 💡 一句话要点

**提出GRiP框架，通过认知引导强化学习提升视觉基础推理的鲁棒性和灵活性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉基础推理` `强化学习` `认知引导` `多模态学习` `视觉语言模型`

## 📋 核心要点

1. 现有视觉基础推理方法受困于强化学习的不稳定和监督微调的刚性，难以兼顾学习能力和认知灵活性。
2. GRiP框架通过认知引导的强化学习，显式引导模型的感知焦点和逻辑路径，提升视觉推理的鲁棒性和灵活性。
3. GRiP在TreeBench和V* Bench等基准测试中取得了开源模型中最优结果，验证了其在复杂视觉推理中的有效性。

## 📝 摘要（中文）

本文提出GRiP（Guided Reasoning and Perception）框架，旨在解决现有视觉基础推理方法在端到端强化学习的不稳定性和监督微调的刚性之间的困境。GRiP采用两阶段训练方法，通过显式引导模型的感知焦点和逻辑路径，培养鲁棒且灵活的视觉基础推理能力。该框架的核心在于认知增强的强化学习阶段，包含两个关键创新：一是显著性加权IoU奖励，激励模型优先定位任务关键对象而非无关干扰项；二是多启发式奖励，鼓励多样但逻辑上有效的推理路径，从而提升认知灵活性。基于Qwen2.5-VL-7B模型初始化，GRiP在多个具有挑战性的基准测试中表现出显著的性能提升，并在TreeBench和V* Bench上取得了开源模型中最先进的结果，证明了其在复杂视觉推理方面的有效性。

## 🔬 方法详解

**问题定义**：现有视觉基础推理模型在复杂场景下表现不佳，主要痛点在于：端到端强化学习训练不稳定，难以收敛；监督微调虽然稳定，但模型缺乏认知灵活性，难以泛化到新的场景。模型难以区分关键对象和干扰项，推理路径单一，缺乏探索能力。

**核心思路**：GRiP的核心思路是通过认知引导的强化学习，显式地引导模型关注任务关键对象，并鼓励模型探索多样化的推理路径。通过设计特定的奖励函数，激励模型学习更鲁棒、更灵活的视觉推理能力。

**技术框架**：GRiP框架包含两个主要阶段：第一阶段是使用预训练的视觉语言模型（如Qwen2.5-VL-7B）进行初始化；第二阶段是认知增强的强化学习阶段，该阶段使用设计的奖励函数来训练模型。整体流程是：输入图像和问题，模型通过视觉感知模块定位相关对象，然后进行逻辑推理，最终输出答案。

**关键创新**：GRiP的关键创新在于两个方面：一是显著性加权IoU奖励，该奖励函数根据对象的重要性对IoU进行加权，激励模型优先关注任务关键对象；二是多启发式奖励，该奖励函数鼓励模型探索多样化的推理路径，提升模型的认知灵活性。

**关键设计**：显著性加权IoU奖励的具体计算方式是：首先确定图像中每个对象的显著性权重，然后计算模型预测的边界框与真实边界框的IoU，最后将IoU与显著性权重相乘得到最终的奖励值。多启发式奖励的具体实现方式是：设计多个不同的启发式规则，根据模型是否满足这些规则来给予不同的奖励。具体参数设置和网络结构细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

GRiP框架在TreeBench和V* Bench等具有挑战性的视觉推理基准测试中取得了显著的性能提升，并在开源模型中达到了最先进水平。这些结果表明，通过认知引导的强化学习可以有效地提升视觉基础推理的鲁棒性和灵活性。具体的性能数据和提升幅度在论文中未详细给出，属于未知信息。

## 🎯 应用场景

GRiP框架具有广泛的应用前景，可应用于智能客服、自动驾驶、机器人导航等领域。通过提升模型在复杂视觉场景下的推理能力，可以实现更智能、更可靠的AI系统。例如，在自动驾驶中，GRiP可以帮助车辆更准确地识别交通信号灯和行人，从而提高驾驶安全性。

## 📄 摘要（原文）

> Models capable of "thinking with images" by dynamically grounding their reasoning in visual evidence represent a major leap in multimodal AI. However, replicating and advancing this ability is non-trivial, with current methods often trapped between the instability of end-to-end reinforcement learning (RL) and the rigidity of supervised fine-tuning (SFT). This leads to models that either struggle to learn or lack the cognitive flexibility required for complex, real-world scenes. To navigate this dilemma, we introduce GRiP (Guided Reasoning and Perception), a novel two-stage training framework that cultivates robust and flexible visual grounded reasoning by explicitly guiding the model's perceptual focus and logical pathways. GRiP's core lies in its cognitive-enhanced RL stage, which features two key innovations: (1) a Salience-Weighted IoU Reward that incentivizes the model to prioritize the localization of mission-critical objects over trivial distractors, and (2) a Multi-Heuristic Reward that encourages cognitive flexibility by rewarding diverse yet logically valid reasoning pathways. Initialized from the Qwen2.5-VL-7B model, GRiP demonstrates significant performance gains across multiple challenging benchmarks. It achieves state-of-the-art results among open-source models on the highly challenging TreeBench and V* Bench, proving its effectiveness in complex visual reasoning. Our work demonstrates that moving beyond simplistic rewards and instead guiding models with cognitively-inspired signals for what to see and how to think is crucial for unlocking the next level of multimodal intelligence. The code will be made publicly available.

