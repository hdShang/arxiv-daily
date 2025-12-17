---
layout: default
title: Addressing Corner Cases in Autonomous Driving: A World Model-based Approach with Mixture of Experts and LLMs
---

# Addressing Corner Cases in Autonomous Driving: A World Model-based Approach with Mixture of Experts and LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21867" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21867v1</a>
  <a href="https://arxiv.org/pdf/2510.21867.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21867v1" onclick="toggleFavorite(this, '2510.21867v1', 'Addressing Corner Cases in Autonomous Driving: A World Model-based Approach with Mixture of Experts and LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haicheng Liao, Bonan Wang, Junxian Yang, Chengyue Wang, Zhengbin He, Guohui Zhang, Chengzhong Xu, Zhenning Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-23

---

## 💡 一句话要点

**提出WM-MoE框架，利用世界模型和混合专家模型解决自动驾驶Corner Case问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `运动预测` `Corner Case` `世界模型` `混合专家模型` `大型语言模型` `长时程推理`

## 📋 核心要点

1. 现有运动预测模型在Corner Case场景下表现不佳，原因是训练数据中常见场景过度表示，泛化能力有限。
2. WM-MoE框架通过世界模型统一感知、记忆和决策，利用LLM增强长时程推理，MoE分解复杂场景，提升Corner Case处理能力。
3. 在nuScenes等数据集上的实验表明，WM-MoE显著优于现有方法，并在Corner Case和数据缺失情况下表现出更强的鲁棒性。

## 📝 摘要（中文）

本文提出WM-MoE，一种基于世界模型的运动预测框架，旨在解决自动驾驶中高风险Corner Case场景的挑战。该模型统一了感知、时间记忆和决策制定，构建紧凑的场景表示，预测未来动态并评估潜在行为的结果。为了增强长时程推理，利用大型语言模型(LLM)，引入轻量级时间分词器，将智能体轨迹和上下文线索映射到LLM的特征空间，无需额外训练，从而丰富时间上下文和常识先验。此外，引入混合专家模型(MoE)将复杂的Corner Case分解为子问题，并在不同场景类型之间分配容量，路由器将场景分配给专门的专家，推断智能体意图并执行反事实推演。同时，引入nuScenes-corner，一个新的基准，包含四个真实世界的Corner Case场景，用于严格评估。在四个基准数据集（nuScenes、NGSIM、HighD和MoCAD）上的大量实验表明，WM-MoE始终优于最先进的(SOTA)基线，并在Corner Case和数据缺失条件下保持稳健性，表明基于世界模型的架构在完全自动驾驶中具有鲁棒性和通用性的运动预测潜力。

## 🔬 方法详解

**问题定义**：自动驾驶车辆在Corner Case场景下的运动预测精度不足，现有模型难以泛化到这些罕见但高风险的场景。训练数据中常见场景的过度表示和模型自身泛化能力的限制是主要痛点。

**核心思路**：利用世界模型构建场景的紧凑表示，预测未来动态并评估潜在行为的结果，从而提升模型对Corner Case场景的理解和预测能力。通过引入LLM增强模型的长时程推理能力，并使用MoE将复杂场景分解为更易于处理的子问题。

**技术框架**：WM-MoE框架包含感知模块、时间记忆模块、决策模块和混合专家模块。感知模块负责提取场景特征，时间记忆模块利用LLM对历史轨迹进行编码，决策模块基于世界模型预测未来轨迹，混合专家模块将复杂场景分配给不同的专家进行处理。整体流程为：输入场景信息，感知模块提取特征，时间记忆模块编码历史信息，MoE将场景分配给专家，专家进行轨迹预测，输出最终预测结果。

**关键创新**：WM-MoE的关键创新在于将世界模型、LLM和MoE结合起来，用于解决自动驾驶中的Corner Case问题。世界模型提供场景理解和预测能力，LLM增强长时程推理，MoE实现对复杂场景的分解和专业化处理。与现有方法相比，WM-MoE能够更好地处理罕见和高风险的Corner Case场景。

**关键设计**：时间分词器将智能体轨迹和上下文线索映射到LLM的特征空间，无需额外训练。MoE由多个专家网络和一个路由器组成，路由器根据场景特征将场景分配给不同的专家网络。损失函数包括轨迹预测损失和行为预测损失，用于优化模型的预测精度和行为合理性。

## 📊 实验亮点

WM-MoE在nuScenes、NGSIM、HighD和MoCAD四个数据集上均取得了优于SOTA基线的性能。在nuScenes数据集上，WM-MoE在Corner Case场景下的预测精度提升显著，尤其是在数据缺失的情况下，仍能保持较高的鲁棒性。nuScenes-corner基准测试结果表明，WM-MoE能够有效应对真实世界中的复杂Corner Case。

## 🎯 应用场景

该研究成果可应用于提高自动驾驶系统的安全性和可靠性，尤其是在复杂和罕见的交通场景中。通过更准确的运动预测，自动驾驶车辆能够更好地应对Corner Case，降低事故风险，加速自动驾驶技术的商业化落地。此外，该方法也可推广到其他需要复杂场景理解和预测的领域，如机器人导航、智能交通管理等。

## 📄 摘要（原文）

> Accurate and reliable motion forecasting is essential for the safe deployment of autonomous vehicles (AVs), particularly in rare but safety-critical scenarios known as corner cases. Existing models often underperform in these situations due to an over-representation of common scenes in training data and limited generalization capabilities. To address this limitation, we present WM-MoE, the first world model-based motion forecasting framework that unifies perception, temporal memory, and decision making to address the challenges of high-risk corner-case scenarios. The model constructs a compact scene representation that explains current observations, anticipates future dynamics, and evaluates the outcomes of potential actions. To enhance long-horizon reasoning, we leverage large language models (LLMs) and introduce a lightweight temporal tokenizer that maps agent trajectories and contextual cues into the LLM's feature space without additional training, enriching temporal context and commonsense priors. Furthermore, a mixture-of-experts (MoE) is introduced to decompose complex corner cases into subproblems and allocate capacity across scenario types, and a router assigns scenes to specialized experts that infer agent intent and perform counterfactual rollouts. In addition, we introduce nuScenes-corner, a new benchmark that comprises four real-world corner-case scenarios for rigorous evaluation. Extensive experiments on four benchmark datasets (nuScenes, NGSIM, HighD, and MoCAD) showcase that WM-MoE consistently outperforms state-of-the-art (SOTA) baselines and remains robust under corner-case and data-missing conditions, indicating the promise of world model-based architectures for robust and generalizable motion forecasting in fully AVs.

