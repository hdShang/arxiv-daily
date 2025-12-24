---
layout: default
title: "InPhyRe Discovers: Large Multimodal Models Struggle in Inductive Physical Reasoning"
---

# InPhyRe Discovers: Large Multimodal Models Struggle in Inductive Physical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12263" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12263v1</a>
  <a href="https://arxiv.org/pdf/2509.12263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12263v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12263v1', 'InPhyRe Discovers: Large Multimodal Models Struggle in Inductive Physical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gautam Sreekumar, Vishnu Naresh Boddeti

**分类**: cs.AI, cs.LG

**发布日期**: 2025-09-12

**备注**: 35 pages including appendix

---

## 💡 一句话要点

**提出InPhyRe基准，揭示大型多模态模型在归纳物理推理上的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `物理推理` `归纳推理` `视觉问答` `基准测试`

## 📋 核心要点

1. 现有视觉基准侧重于评估LMMs的参数知识，忽略了其在未见过的物理环境中的归纳物理推理能力。
2. 论文提出InPhyRe基准，旨在评估LMMs在违反常见物理定律场景下的视觉问答能力，衡量其归纳推理能力。
3. 实验结果表明，LMMs在归纳物理推理方面表现不佳，易受语言偏差影响，且对视觉输入的信任度较低。

## 📝 摘要（中文）

大型多模态模型（LMMs）将训练中观察到的通用物理定律（如动量守恒）编码为参数知识。这使得LMMs能够回答物理推理问题，例如从视觉输入预测潜在碰撞事件的结果。然而，由于参数知识仅包含训练期间看到的物理定律，当推理场景违反这些定律时，它不足以进行推理。相比之下，人类能够通过少量视觉示例将物理推理适应于未见过的物理环境。这种能力，我们称之为归纳物理推理，对于LMMs在安全关键应用中取代人类至关重要。尽管其重要性，现有的视觉基准仅评估LMMs中的参数知识，而非归纳物理推理。为此，我们提出了InPhyRe，这是第一个用于衡量LMMs中归纳物理推理的视觉问答基准。InPhyRe通过检查13个LMMs，告知我们：（1）LMMs难以将关于通用物理定律的有限参数知识应用于推理，（2）当演示样本违反通用物理定律时，LMMs中的归纳物理推理较弱，以及（3）LMMs中的归纳物理推理受到语言偏差的影响，并且在很大程度上忽略了视觉输入，质疑了LMMs在视觉输入方面的可信度。

## 🔬 方法详解

**问题定义**：现有的大型多模态模型在物理推理方面依赖于训练数据中学习到的参数知识，当测试场景违反了训练数据中常见的物理定律时，模型的推理能力会显著下降。现有的视觉基准测试主要关注模型对常见物理现象的理解，缺乏对模型在新的、违反直觉的物理环境中的泛化能力的评估。

**核心思路**：论文的核心思路是构建一个专门用于评估LMMs归纳物理推理能力的基准数据集InPhyRe。该数据集包含算法生成的合成碰撞视频，这些视频展示了违反常见物理定律的场景。通过观察LMMs在这些场景下的表现，可以评估其是否能够根据少量示例进行学习并适应新的物理环境。

**技术框架**：InPhyRe基准测试包含一系列视觉问答任务，其中LMMs需要根据给定的碰撞视频预测碰撞事件的结果。数据集通过算法生成，可以控制物理参数和违反物理定律的程度。评估过程包括比较LMMs的预测结果与真实结果，并分析其在不同场景下的表现。此外，还设计了控制实验来评估语言偏差对LMMs推理能力的影响。

**关键创新**：InPhyRe基准测试的主要创新在于其关注点是LMMs的归纳物理推理能力，而非仅仅是参数知识。通过算法生成违反常见物理定律的场景，可以有效地评估LMMs在新的物理环境中的泛化能力。此外，该基准测试还考虑了语言偏差对LMMs推理能力的影响，并设计了相应的控制实验。

**关键设计**：InPhyRe数据集中的视频由算法生成，可以精确控制物体的质量、速度、碰撞角度等参数。为了模拟违反物理定律的场景，可以调整碰撞后的速度和方向，使其不符合动量守恒定律。视觉问答任务的设计包括多种问题类型，例如预测碰撞后的物体位置、速度和方向。评估指标包括预测结果的准确率和与真实值的偏差。

## 📊 实验亮点

实验结果表明，LMMs在InPhyRe基准测试中表现不佳，即使在少量示例的引导下，也难以适应违反常见物理定律的场景。LMMs的预测结果受到语言偏差的显著影响，表明模型在很大程度上依赖于问题描述中的语言信息，而忽略了视觉输入。例如，在某些情况下，即使视频内容完全相反，只要问题描述相同，LMMs的回答也会保持一致。

## 🎯 应用场景

该研究成果可应用于评估和改进LMMs在安全关键领域的可靠性，例如自动驾驶、机器人导航和智能制造。通过提高LMMs在复杂和未知环境中的推理能力，可以减少事故风险并提高系统的整体性能。此外，该基准测试可以促进对LMMs内在局限性的理解，并指导未来模型的设计和训练。

## 📄 摘要（原文）

> Large multimodal models (LMMs) encode universal physical laws observed during training, such as momentum conservation, as parametric knowledge. It allows LMMs to answer physical reasoning queries, such as the outcome of a potential collision event from visual input. However, since parametric knowledge includes only the physical laws seen during training, it is insufficient for reasoning when the inference scenario violates these physical laws. In contrast, humans possess the skill to adapt their physical reasoning to unseen physical environments from a few visual examples. This ability, which we refer to as inductive physical reasoning, is indispensable for LMMs if they are to replace human agents in safety-critical applications. Despite its importance, existing visual benchmarks evaluate only the parametric knowledge in LMMs, and not inductive physical reasoning. To this end, we propose InPhyRe, the first visual question answering benchmark to measure inductive physical reasoning in LMMs. InPhyRe evaluates LMMs on their ability to predict the outcome of collision events in algorithmically generated synthetic collision videos. By inspecting 13 LMMs, InPhyRe informs us that (1) LMMs struggle to apply their limited parametric knowledge about universal physical laws to reasoning, (2) inductive physical reasoning in LMMs is weak when demonstration samples violate universal physical laws, and (3) inductive physical reasoning in LMMs suffers from language bias and largely ignores the visual inputs, questioning the trustworthiness of LMMs regarding visual inputs.

