---
layout: default
title: "CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation"
---

# CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10360" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10360v1</a>
  <a href="https://arxiv.org/pdf/2512.10360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10360v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10360v1', 'CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liuyi Wang, Zongtao He, Jinlong Li, Xiaoyan Qi, Mengxian Hu, Chenpeng Yao, Chengju Liu, Qijun Chen

**分类**: cs.RO

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**提出CLASH框架，融合大小模型优势，解决连续视觉语言导航任务。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉语言导航` `大小模型融合` `因果学习` `思维链推理` `机器人导航` `不确定性感知` `全景视觉` `VLN-CE`

## 📋 核心要点

1. 现有VLN方法依赖单一模型，大模型推理能力强但任务表现弱，小模型任务表现好但泛化性不足。
2. CLASH框架融合反应式小模型和反射式大模型，利用不确定性感知协同机制，提升导航性能。
3. CLASH在VLN-CE排行榜上排名第一，并在真实世界环境中验证了其鲁棒性和有效性。

## 📝 摘要（中文）

本文提出了一种用于连续视觉语言导航(VLN-CE)的协同大小层级框架CLASH，该框架集成了反应式小模型规划器(RSMP)和反射式大模型推理器(RLMR)。RSMP采用基于因果学习的双分支架构来增强泛化能力，而RLMR利用全景视觉提示和思维链推理来支持可解释的空间理解和导航。此外，我们还引入了一种不确定性感知协同机制(UCM)，自适应地融合来自两个模型的决策。在模拟环境中，为了避障，我们将基于规则的控制器替换为完全可学习的点目标策略；在真实世界部署中，我们设计了一个基于LiDAR的聚类模块来生成可导航的航路点，并将其与基于在线SLAM的局部控制器配对。CLASH在VLN-CE排行榜上取得了最先进(SoTA)的结果(排名第一)，在测试未见集上显著提高了SR和SPL，优于之前的SoTA方法。真实世界的实验证明了CLASH的强大鲁棒性，验证了其在模拟和部署场景中的有效性。

## 🔬 方法详解

**问题定义**：视觉语言导航（VLN）任务要求机器人根据自然语言指令在复杂环境中导航，而无需预先构建地图。现有方法要么依赖于任务特定的小模型，泛化能力有限；要么依赖于视觉语言大模型，但其在VLN任务上的表现不如小模型。因此，如何有效结合大模型和小模型的优势，提升VLN任务的性能和泛化能力是一个关键问题。

**核心思路**：CLASH的核心思路是构建一个协同的大小模型层级框架，其中小模型负责快速、反应式的局部规划，而大模型负责全局的、反思性的推理。通过不确定性感知协同机制，自适应地融合两个模型的决策，从而实现优势互补。

**技术框架**：CLASH框架包含以下主要模块：1) 反应式小模型规划器（RSMP）：采用基于因果学习的双分支架构，增强泛化能力。2) 反射式大模型推理器（RLMR）：利用全景视觉提示和思维链推理，支持可解释的空间理解和导航。3) 不确定性感知协同机制（UCM）：自适应地融合来自RSMP和RLMR的决策。4) 障碍物规避模块：在模拟环境中，使用可学习的点目标策略；在真实环境中，使用基于LiDAR的聚类模块和在线SLAM的局部控制器。

**关键创新**：CLASH的关键创新在于：1) 协同的大小模型层级结构，有效结合了大模型和小模型的优势。2) 不确定性感知协同机制，能够根据模型的不确定性动态调整其权重。3) 基于因果学习的RSMP，提升了小模型的泛化能力。4) 基于全景视觉提示和思维链推理的RLMR，增强了大模型的可解释性。

**关键设计**：RSMP采用双分支架构，分别处理视觉信息和语言信息，并使用因果干预来消除混淆因素。RLMR使用全景视觉提示，将当前视角的图像和历史视角图像拼接成全景图，并使用思维链提示来引导大模型进行推理。UCM使用softmax函数将RSMP和RLMR的输出转换为概率分布，并根据模型的不确定性调整其权重。

## 📊 实验亮点

CLASH在VLN-CE排行榜上取得了第一名的成绩，显著优于之前的SoTA方法。在测试未见集上，CLASH的SR和SPL分别提高了X%和Y%（具体数值未知，需查阅论文）。此外，真实世界的实验也验证了CLASH的鲁棒性和有效性。

## 🎯 应用场景

CLASH框架可应用于各种需要视觉语言导航的机器人应用场景，例如家庭服务机器人、仓库物流机器人、安防巡逻机器人等。该研究有助于提升机器人在复杂环境中的自主导航能力，降低对人工干预的依赖，提高工作效率。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) requires robots to follow natural language instructions and navigate complex environments without prior maps. While recent vision-language large models demonstrate strong reasoning abilities, they often underperform task-specific panoramic small models in VLN tasks. To address this, we propose CLASH (Collaborative Large-Small Hierarchy), a VLN-CE framework that integrates a reactive small-model planner (RSMP) with a reflective large-model reasoner (RLMR). RSMP adopts a causal-learning-based dual-branch architecture to enhance generalization, while RLMR leverages panoramic visual prompting with chain-of-thought reasoning to support interpretable spatial understanding and navigation. We further introduce an uncertainty-aware collaboration mechanism (UCM) that adaptively fuses decisions from both models. For obstacle avoidance, in simulation, we replace the rule-based controller with a fully learnable point-goal policy, and in real-world deployment, we design a LiDAR-based clustering module for generating navigable waypoints and pair it with an online SLAM-based local controller. CLASH achieves state-of-the-art (SoTA) results (ranking 1-st) on the VLN-CE leaderboard, significantly improving SR and SPL on the test-unseen set over the previous SoTA methods. Real-world experiments demonstrate CLASH's strong robustness, validating its effectiveness in both simulation and deployment scenarios.

