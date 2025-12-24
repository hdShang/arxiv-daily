---
layout: default
title: "OctoNav: Towards Generalist Embodied Navigation"
---

# OctoNav: Towards Generalist Embodied Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09839" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09839v1</a>
  <a href="https://arxiv.org/pdf/2506.09839.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09839v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09839v1', 'OctoNav: Towards Generalist Embodied Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Gao, Liankai Jin, Xingyu Peng, Jiazhao Zhang, Yue Deng, Annan Li, He Wang, Si Liu

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-06-11

**备注**: 31 pages, 25 figures

---

## 💡 一句话要点

**提出OctoNav以解决多模态导航任务的统一性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身导航` `多模态学习` `通用代理` `推理能力` `混合训练范式`

## 📋 核心要点

1. 现有的具身导航研究多集中于特定任务，缺乏统一的框架，导致方法和数据集的碎片化。
2. 本文提出OctoNav-Bench和OctoNav-R1，旨在实现能够处理多模态和多能力指令的通用导航代理。
3. 实验结果表明，OctoNav-R1在多个任务上表现优越，显示出较强的推理能力和导航性能。

## 📝 摘要（中文）

具身导航是具身人工智能的基础，但现有研究多集中于不同的任务和能力，如ObjNav、ImgNav和VLN，导致数据集和方法各自独立。本文提出OctoNav-Bench和OctoNav-R1，旨在实现通用导航代理，能够处理包含多模态和多能力的自由形式指令。OctoNav-Bench通过设计的注释流程构建，包含多样化的指令-轨迹对，并引入Think-Before-Action (TBA-CoT) 数据集，提供行动背后的思维过程。OctoNav-R1基于MLLMs构建，适配为VLA类型模型，仅基于2D视觉观察生成低级动作，并设计了混合训练范式（HTP），包含多个阶段，最终显示出优于现有方法的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决具身导航领域中任务和能力的碎片化问题，现有方法无法有效处理多模态和多能力的自由形式指令。

**核心思路**：通过构建OctoNav-Bench和OctoNav-R1，提出一种通用的导航代理，能够理解和执行复杂的指令，提升模型的推理能力。

**技术框架**：整体架构包括三个主要阶段：Action-/TBA-SFT、Nav-GPRO和在线强化学习（Online RL），每个阶段都有特定的学习策略和奖励机制。

**关键创新**：最重要的创新在于引入Think-Before-Action (TBA-CoT) 数据集，提供行动前的思维过程，提升模型的推理能力，与现有方法相比，能够更好地处理复杂指令。

**关键设计**：在训练过程中，TBA-SFT阶段利用TBA-CoT数据集进行冷启动微调，Nav-GPRO阶段则进一步提升模型的思维能力，确保模型在执行低级动作时具备更强的推理能力。

## 📊 实验亮点

OctoNav-R1在多个基准任务上表现优越，相比于现有方法，推理能力和导航性能显著提升，具体性能数据未提供，但实验结果表明其在复杂指令处理上的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟助手等，能够在复杂环境中更好地理解和执行人类指令，提升交互的自然性和效率。未来，随着技术的进步，通用导航代理有望在更多实际场景中得到应用，推动具身人工智能的发展。

## 📄 摘要（原文）

> Embodied navigation stands as a foundation pillar within the broader pursuit of embodied AI. However, previous navigation research is divided into different tasks/capabilities, e.g., ObjNav, ImgNav and VLN, where they differ in task objectives and modalities, making datasets and methods are designed individually. In this work, we take steps toward generalist navigation agents, which can follow free-form instructions that include arbitrary compounds of multi-modal and multi-capability. To achieve this, we propose a large-scale benchmark and corresponding method, termed OctoNav-Bench and OctoNav-R1. Specifically, OctoNav-Bench features continuous environments and is constructed via a designed annotation pipeline. We thoroughly craft instruction-trajectory pairs, where instructions are diverse in free-form with arbitrary modality and capability. Also, we construct a Think-Before-Action (TBA-CoT) dataset within OctoNav-Bench to provide the thinking process behind actions. For OctoNav-R1, we build it upon MLLMs and adapt it to a VLA-type model, which can produce low-level actions solely based on 2D visual observations. Moreover, we design a Hybrid Training Paradigm (HTP) that consists of three stages, i.e., Action-/TBA-SFT, Nav-GPRO, and Online RL stages. Each stage contains specifically designed learning policies and rewards. Importantly, for TBA-SFT and Nav-GRPO designs, we are inspired by the OpenAI-o1 and DeepSeek-R1, which show impressive reasoning ability via thinking-before-answer. Thus, we aim to investigate how to achieve thinking-before-action in the embodied navigation field, to improve model's reasoning ability toward generalists. Specifically, we propose TBA-SFT to utilize the TBA-CoT dataset to fine-tune the model as a cold-start phrase and then leverage Nav-GPRO to improve its thinking ability. Finally, OctoNav-R1 shows superior performance compared with previous methods.

