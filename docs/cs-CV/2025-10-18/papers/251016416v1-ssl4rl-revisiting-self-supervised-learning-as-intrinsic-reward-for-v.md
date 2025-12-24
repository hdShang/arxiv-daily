---
layout: default
title: "SSL4RL: Revisiting Self-supervised Learning as Intrinsic Reward for Visual-Language Reasoning"
---

# SSL4RL: Revisiting Self-supervised Learning as Intrinsic Reward for Visual-Language Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16416" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16416v1</a>
  <a href="https://arxiv.org/pdf/2510.16416.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16416v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16416v1', 'SSL4RL: Revisiting Self-supervised Learning as Intrinsic Reward for Visual-Language Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaojun Guo, Runyu Zhou, Yifei Wang, Qi Zhang, Chenheng Zhang, Stefanie Jegelka, Xiaohan Wang, Jiajun Chai, Guojun Yin, Wei Lin, Yisen Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-18

---

## 💡 一句话要点

**SSL4RL：利用自监督学习作为视觉-语言推理的内在奖励**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言推理` `自监督学习` `强化学习` `多模态学习` `内在奖励`

## 📋 核心要点

1. 现有视觉-语言模型在利用视觉信息方面存在不足，容易依赖语言先验或文本捷径，限制了其推理能力。
2. SSL4RL框架将自监督学习任务的目标转化为强化学习的奖励信号，无需人工标注或复杂的奖励函数设计。
3. 实验表明，SSL4RL在视觉中心和视觉-语言推理任务上均取得了显著的性能提升，并成功应用于图学习。

## 📝 摘要（中文）

视觉-语言模型（VLM）通过整合大型语言模型和视觉输入展现了卓越的能力。然而，它们常常无法充分利用视觉证据，要么依赖于视觉中心任务中的语言先验，要么在推理过程中依赖于文本捷径。虽然强化学习（RL）可以使模型与期望的行为对齐，但由于缺乏可扩展和可靠的奖励机制，其在VLM中的应用受到阻碍。为了克服这一挑战，我们提出了SSL4RL，这是一个新颖的框架，它利用自监督学习（SSL）任务作为基于RL微调的可验证奖励来源。我们的方法将SSL目标（例如预测图像旋转或重建掩码补丁）重新定义为密集、自动的奖励信号，从而消除了对人类偏好数据或不可靠的AI评估器的需求。实验表明，SSL4RL显著提高了视觉中心和视觉-语言推理基准的性能。此外，通过系统的消融研究，我们确定了影响SSL4RL任务有效性的关键因素（例如任务难度、模型规模以及与目标领域的语义对齐），为未来的工作提供了新的设计原则。我们还通过将其应用于图学习来证明了该框架的通用性，从而获得了显著的收益。SSL4RL为使用可验证的自监督目标对齐多模态模型建立了一个通用且有效的范例。

## 🔬 方法详解

**问题定义**：视觉-语言模型在视觉推理任务中表现不佳，主要原因是模型过度依赖语言信息，而忽略了视觉证据。现有的强化学习方法虽然可以用于微调模型行为，但缺乏可扩展和可靠的奖励机制，例如需要人工标注或依赖不可靠的AI评估器。

**核心思路**：论文的核心思路是将自监督学习（SSL）任务的目标函数转化为强化学习的奖励信号。通过这种方式，可以利用SSL任务的内在监督信息来引导模型的学习，而无需人工干预。这种方法可以提供密集、自动且可验证的奖励信号，从而克服了传统强化学习方法的局限性。

**技术框架**：SSL4RL框架主要包含以下几个阶段：1) 预训练的视觉-语言模型；2) 定义自监督学习任务，例如图像旋转预测或掩码图像重建；3) 将SSL任务的目标函数转化为强化学习的奖励函数；4) 使用强化学习算法（例如PPO）对视觉-语言模型进行微调，以最大化SSL奖励。整体流程是利用SSL任务提供的内在奖励来引导模型学习，从而提高其视觉推理能力。

**关键创新**：该论文的关键创新在于将自监督学习与强化学习相结合，提出了一种新的视觉-语言模型微调框架。与传统的强化学习方法相比，SSL4RL无需人工标注或复杂的奖励函数设计，而是利用SSL任务的内在监督信息来提供奖励信号。这使得强化学习可以更容易地应用于视觉-语言模型，并提高其视觉推理能力。

**关键设计**：论文中关键的设计包括：1) 选择合适的自监督学习任务，例如图像旋转预测、掩码图像重建等，这些任务需要模型理解图像的结构和语义信息；2) 设计合适的奖励函数，将SSL任务的目标函数转化为强化学习的奖励信号；3) 使用合适的强化学习算法，例如PPO，对视觉-语言模型进行微调。此外，论文还研究了任务难度、模型规模以及与目标领域的语义对齐等因素对SSL4RL任务有效性的影响。

## 📊 实验亮点

实验结果表明，SSL4RL在视觉中心和视觉-语言推理基准上均取得了显著的性能提升。例如，在某些任务上，SSL4RL的性能超过了现有的最先进方法。此外，消融实验表明，任务难度、模型规模以及与目标领域的语义对齐等因素对SSL4RL任务的有效性有重要影响。该框架还成功应用于图学习，并获得了显著的收益。

## 🎯 应用场景

SSL4RL框架具有广泛的应用前景，可以应用于各种需要视觉-语言推理的任务，例如视觉问答、图像描述、视觉导航等。该方法可以提高模型在这些任务中的性能，并降低对人工标注数据的依赖。此外，该框架还可以推广到其他多模态学习任务中，例如语音-语言学习、视频-语言学习等。

## 📄 摘要（原文）

> Vision-language models (VLMs) have shown remarkable abilities by integrating large language models with visual inputs. However, they often fail to utilize visual evidence adequately, either depending on linguistic priors in vision-centric tasks or resorting to textual shortcuts during reasoning. Although reinforcement learning (RL) can align models with desired behaviors, its application to VLMs has been hindered by the lack of scalable and reliable reward mechanisms. To overcome this challenge, we propose SSL4RL, a novel framework that leverages self-supervised learning (SSL) tasks as a source of verifiable rewards for RL-based fine-tuning. Our approach reformulates SSL objectives-such as predicting image rotation or reconstructing masked patches-into dense, automatic reward signals, eliminating the need for human preference data or unreliable AI evaluators. Experiments show that SSL4RL substantially improves performance on both vision-centric and vision-language reasoning benchmarks. Furthermore, through systematic ablations, we identify key factors-such as task difficulty, model scale, and semantic alignment with the target domain-that influence the effectiveness of SSL4RL tasks, offering new design principles for future work. We also demonstrate the framework's generality by applying it to graph learning, where it yields significant gains. SSL4RL establishes a versatile and effective paradigm for aligning multimodal models using verifiable, self-supervised objectives.

