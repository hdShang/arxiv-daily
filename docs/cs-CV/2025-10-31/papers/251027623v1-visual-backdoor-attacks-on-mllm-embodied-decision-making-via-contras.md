---
layout: default
title: Visual Backdoor Attacks on MLLM Embodied Decision Making via Contrastive Trigger Learning
---

# Visual Backdoor Attacks on MLLM Embodied Decision Making via Contrastive Trigger Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.27623" target="_blank" class="toolbar-btn">arXiv: 2510.27623v1</a>
    <a href="https://arxiv.org/pdf/2510.27623.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27623v1" 
            onclick="toggleFavorite(this, '2510.27623v1', 'Visual Backdoor Attacks on MLLM Embodied Decision Making via Contrastive Trigger Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Qiusi Zhan, Hyeonjeong Ha, Rui Yang, Sirui Xu, Hanyang Chen, Liang-Yan Gui, Yu-Xiong Wang, Huan Zhang, Heng Ji, Daniel Kang

**分类**: cs.AI, cs.CL, cs.CV

**发布日期**: 2025-10-31

---

## 💡 一句话要点

**提出BEAT框架，通过对比触发学习实现MLLM具身智能体的视觉后门攻击**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉后门攻击` `多模态大语言模型` `具身智能体` `对比学习` `触发器学习`

## 📋 核心要点

1. MLLM驱动的具身智能体面临视觉后门攻击的安全风险，现有方法难以应对视角和光照变化下的物体触发器。
2. BEAT框架通过对比触发学习(CTL)，显式地学习触发器存在与否的偏好，从而锐化决策边界，提升后门激活的准确性。
3. 实验表明，BEAT在保持良好良性任务性能的同时，实现了高达80%的攻击成功率，并且在有限后门数据下，CTL将后门激活准确率提升了39%。

## 📝 摘要（中文）

本文提出BEAT框架，旨在为基于多模态大语言模型(MLLM)的具身智能体注入视觉后门。该框架利用环境中的物体作为触发器，当触发器出现在场景中时，智能体会持续执行攻击者预先设定的多步策略。BEAT通过构建包含多样场景、任务和触发器位置的训练集，使智能体暴露于触发器的变化中，并采用两阶段训练方案：首先进行监督微调(SFT)，然后进行对比触发学习(CTL)。CTL将触发器判别转化为触发器存在与不存在输入之间的偏好学习，从而明确地锐化决策边界，确保精确的后门激活。实验结果表明，BEAT在各种具身智能体基准和MLLM上实现了高达80%的攻击成功率，同时保持了良好的良性任务性能，并可靠地推广到分布外的触发器位置。与朴素的SFT相比，CTL在有限的后门数据下，后门激活准确率提高了39%。

## 🔬 方法详解

**问题定义**：论文旨在解决MLLM具身智能体中存在的视觉后门攻击问题。现有的基于文本触发器的后门攻击方法无法直接应用于视觉场景，因为视觉触发器（例如物体）在不同视角和光照条件下会发生显著变化，导致触发器难以可靠地植入，从而影响攻击的成功率。

**核心思路**：论文的核心思路是通过对比学习来增强智能体对视觉触发器的识别能力。具体来说，通过构建包含多样场景、任务和触发器位置的训练集，使智能体暴露于触发器的各种变化中。然后，利用对比触发学习(CTL)来显式地学习触发器存在与否的偏好，从而锐化决策边界，提高后门激活的准确性。

**技术框架**：BEAT框架包含两个主要阶段：监督微调(SFT)和对比触发学习(CTL)。首先，使用SFT对MLLM进行微调，使其能够执行正常的具身智能体任务。然后，使用CTL进一步微调MLLM，使其能够准确地识别视觉触发器并激活后门。CTL通过最小化对比损失函数来实现，该损失函数鼓励智能体区分包含触发器的输入和不包含触发器的输入。

**关键创新**：论文的关键创新在于提出了对比触发学习(CTL)方法。与传统的监督学习方法不同，CTL将触发器判别转化为触发器存在与不存在输入之间的偏好学习。这种方法能够更有效地利用有限的后门数据，并提高后门激活的准确性。此外，BEAT框架还通过构建包含多样场景、任务和触发器位置的训练集，增强了智能体对触发器变化的鲁棒性。

**关键设计**：CTL使用对比损失函数来学习触发器偏好。具体来说，对于每个包含触发器的输入，CTL会生成一个对应的负样本（不包含触发器的输入）。然后，CTL会最小化以下对比损失函数：L = max(0, margin - s(x_pos) + s(x_neg))，其中s(x)是智能体对输入x的评分，x_pos是包含触发器的输入，x_neg是不包含触发器的输入，margin是一个超参数。该损失函数鼓励智能体对包含触发器的输入给出更高的评分，对不包含触发器的输入给出更低的评分，从而锐化决策边界。

## 📊 实验亮点

实验结果表明，BEAT框架在各种具身智能体基准和MLLM上实现了高达80%的攻击成功率，同时保持了良好的良性任务性能。与朴素的SFT相比，CTL在有限的后门数据下，后门激活准确率提高了39%。此外，BEAT框架还能够可靠地推广到分布外的触发器位置，表明其具有较强的泛化能力。

## 🎯 应用场景

该研究成果可应用于评估和提升MLLM具身智能体的安全性，尤其是在机器人导航、自动驾驶等安全攸关的应用场景中。通过模拟和分析视觉后门攻击，可以帮助研究人员开发更鲁棒的防御机制，确保智能体在真实世界部署中的可靠性和安全性。未来的研究可以探索更复杂的攻击策略和更有效的防御方法。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have advanced embodied agents by enabling direct perception, reasoning, and planning task-oriented actions from visual inputs. However, such vision driven embodied agents open a new attack surface: visual backdoor attacks, where the agent behaves normally until a visual trigger appears in the scene, then persistently executes an attacker-specified multi-step policy. We introduce BEAT, the first framework to inject such visual backdoors into MLLM-based embodied agents using objects in the environments as triggers. Unlike textual triggers, object triggers exhibit wide variation across viewpoints and lighting, making them difficult to implant reliably. BEAT addresses this challenge by (1) constructing a training set that spans diverse scenes, tasks, and trigger placements to expose agents to trigger variability, and (2) introducing a two-stage training scheme that first applies supervised fine-tuning (SFT) and then our novel Contrastive Trigger Learning (CTL). CTL formulates trigger discrimination as preference learning between trigger-present and trigger-free inputs, explicitly sharpening the decision boundaries to ensure precise backdoor activation. Across various embodied agent benchmarks and MLLMs, BEAT achieves attack success rates up to 80%, while maintaining strong benign task performance, and generalizes reliably to out-of-distribution trigger placements. Notably, compared to naive SFT, CTL boosts backdoor activation accuracy up to 39% under limited backdoor data. These findings expose a critical yet unexplored security risk in MLLM-based embodied agents, underscoring the need for robust defenses before real-world deployment.

