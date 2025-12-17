---
layout: default
title: Spotlight on Token Perception for Multimodal Reinforcement Learning
---

# Spotlight on Token Perception for Multimodal Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09285" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09285v1</a>
  <a href="https://arxiv.org/pdf/2510.09285.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09285v1" onclick="toggleFavorite(this, '2510.09285v1', 'Spotlight on Token Perception for Multimodal Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Huang, Xiaoye Qu, Yafu Li, Yun Luo, Zefeng He, Daizong Liu, Yu Cheng

**分类**: cs.CV

**发布日期**: 2025-10-10

**备注**: 31 pages, 10 figures, project page: https://github.com/huaixuheqing/VPPO-RL

---

## 💡 一句话要点

**提出VPPO，通过关注token感知优化多模态强化学习，提升LVLM的推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态强化学习` `视觉语言模型` `token感知` `策略优化` `视觉推理`

## 📋 核心要点

1. 现有基于RLVR的多模态推理方法忽略了视觉感知的关键作用，导致LVLM在视觉基础推理方面存在不足。
2. VPPO通过token感知来衡量每个生成token的视觉依赖性，并利用该信息来优化策略梯度，从而提升视觉感知能力。
3. VPPO在多个基准测试中显著优于现有RL调优模型，并在不同模型规模上验证了其有效性，证明了其优越性。

## 📝 摘要（中文）

尽管带有可验证奖励的强化学习（RLVR）提升了大型视觉语言模型（LVLM）的推理能力，但多模态推理中的现有方法大多忽略了RLVR优化过程中视觉感知的关键作用。本文从token感知的角度对多模态RLVR进行了开创性的探索，token感知衡量了每个生成token的视觉依赖性。通过对思维链（CoT）过程的细粒度分析，我们发现了两个关键见解：首先，rollout轨迹中的token感知是稀疏分布的，只有一小部分token对视觉基础推理具有高度视觉依赖性；其次，不同轨迹在整体视觉依赖性方面表现出显著差异。基于这些观察，我们提出了一种新的策略梯度算法——视觉感知策略优化（VPPO），该算法显式地利用token感知来优化学习信号。具体来说，VPPO通过双重机制实现这一点：它通过轨迹的整体视觉依赖性来重新加权轨迹的优势，并专注于对感知关键token的策略更新。在一套全面的八个感知和推理基准测试中，VPPO相对于领先的开源RL调优模型表现出显著的提升，其有效性在7B和32B模型规模上得到一致验证。我们的发现不仅为分析多模态RLVR建立了一个新的token级感知视角，而且还提出了一种新颖有效的优化策略，以显著增强LVLM的多模态推理能力。

## 🔬 方法详解

**问题定义**：现有基于RLVR的多模态推理方法，虽然利用强化学习提升了LVLM的推理能力，但忽略了视觉感知在其中的重要作用。这些方法没有充分利用视觉信息来指导策略学习，导致模型在需要视觉基础推理的任务中表现不佳。现有方法缺乏对每个token的视觉依赖性的细粒度分析，无法有效区分对视觉推理至关重要的token和无关token。

**核心思路**：VPPO的核心思路是利用token感知来指导策略学习。通过衡量每个生成token的视觉依赖性，VPPO能够识别出对视觉推理至关重要的token，并更加关注这些token的策略更新。这种方法能够更有效地利用视觉信息，从而提升LVLM的视觉感知和推理能力。VPPO的设计基于两个关键观察：一是token感知在rollout轨迹中是稀疏的，只有少数token具有高视觉依赖性；二是不同轨迹的整体视觉依赖性存在显著差异。

**技术框架**：VPPO的整体框架包括以下几个主要步骤：1) 使用LVLM生成多个rollout轨迹，每个轨迹包含一系列token；2) 计算每个token的视觉感知，衡量其对视觉信息的依赖程度；3) 根据轨迹的整体视觉依赖性重新加权轨迹的优势；4) 仅对感知关键token进行策略更新。该框架通过显式地利用token感知来优化学习信号，从而提升LVLM的视觉感知和推理能力。

**关键创新**：VPPO的关键创新在于引入了token感知的概念，并将其应用于多模态强化学习中。与现有方法不同，VPPO能够对每个token的视觉依赖性进行细粒度分析，并利用该信息来指导策略学习。这种方法能够更有效地利用视觉信息，从而提升LVLM的视觉感知和推理能力。VPPO还提出了一种双重机制，通过重新加权轨迹的优势和专注于感知关键token的策略更新，来优化学习信号。

**关键设计**：VPPO的关键设计包括：1) 如何计算token感知：论文中具体计算方法未知，但其核心是衡量token对视觉信息的依赖程度。2) 如何根据轨迹的整体视觉依赖性重新加权轨迹的优势：具体加权函数未知，但其目标是提高视觉依赖性高的轨迹的权重，降低视觉依赖性低的轨迹的权重。3) 如何选择感知关键token：具体选择标准未知，但其目标是选择对视觉推理至关重要的token，并更加关注这些token的策略更新。

## 📊 实验亮点

VPPO在八个感知和推理基准测试中取得了显著的提升，超越了领先的开源RL调优模型。具体性能数据未知，但论文强调了VPPO在7B和32B模型规模上的一致有效性，表明其具有良好的泛化能力。VPPO的成功证明了token感知在多模态强化学习中的重要性，并为未来的研究提供了新的方向。

## 🎯 应用场景

VPPO具有广泛的应用前景，例如视觉问答、图像描述、机器人导航等。通过提升LVLM的视觉感知和推理能力，VPPO可以帮助模型更好地理解和处理视觉信息，从而在各种实际应用中取得更好的效果。未来，VPPO可以应用于更复杂的任务中，例如自动驾驶、智能家居等，为人们的生活带来更多便利。

## 📄 摘要（原文）

> While Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capabilities of Large Vision-Language Models (LVLMs), most existing methods in multimodal reasoning neglect the critical role of visual perception within the RLVR optimization process. In this paper, we undertake a pioneering exploration of multimodal RLVR through the novel perspective of token perception, which measures the visual dependency of each generated token. With a granular analysis of Chain-of-Thought (CoT) processes, we uncover two key insights: first, token perception in a rollout trajectory is sparsely distributed, where only a small fraction of tokens have high visual dependency for visually-grounded reasoning; second, different trajectories exhibit significant divergence in their overall visual dependency. Based on these observations, we propose Visually-Perceptive Policy Optimization (VPPO), a novel policy gradient algorithm that explicitly leverages token perception to refine the learning signal. Specifically, VPPO achieves this through a dual mechanism: it reweights a trajectory's advantage by its overall visual dependency, and focuses policy updates exclusively on perceptually pivotal tokens. On a comprehensive suite of eight perception and reasoning benchmarks, VPPO demonstrates substantial gains over leading open-source RL-tuned models, with its effectiveness consistently validated across 7B and 32B model scales. Our findings not only establish a new token-level perceptual perspective for analyzing multimodal RLVR but also present a novel and effective optimization strategy to significantly enhance the multimodal reasoning capabilities of LVLMs.

