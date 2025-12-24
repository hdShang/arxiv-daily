---
layout: default
title: "Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution"
---

# Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24726" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24726v1</a>
  <a href="https://arxiv.org/pdf/2509.24726.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24726v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24726v1', 'Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaobo Wang, Zhengbo Jiao, Zifan Zhang, Yilang Peng, Xu Ze, Boyu Yang, Wei Wang, Hu Wei, Linfeng Zhang

**分类**: cs.CL

**发布日期**: 2025-09-29

**备注**: 23 pages, 3 figures

---

## 💡 一句话要点

**Socratic-Zero：通过无数据Agent协同进化引导LLM推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `数据合成` `Agent协同进化` `无数据学习`

## 📋 核心要点

1. 现有LLM推理依赖大规模人工标注数据集，成本高昂且难以扩展，数据合成方法存在质量不稳定和适应性差的问题。
2. Socratic-Zero通过教师、解题者和生成器三个Agent的协同进化，从少量种子数据中自主生成高质量训练数据。
3. 实验表明，Socratic-Zero在多个数学推理基准测试中显著优于现有数据合成方法，甚至超越了部分商业LLM。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理任务上的突破依赖于大规模、高质量的数据集，这些数据集通常由人工标注，难以扩展。数据合成或蒸馏提供了一种有希望的替代方案，但现有方法在数据质量不一致以及无法动态适应模型不断发展的能力方面存在困难，导致次优的训练信号。为了解决这些限制，我们引入了Socratic-Zero，这是一个完全自主的框架，通过三个Agent（教师、解题者和生成器）的协同进化，从最少的种子示例中生成高质量的训练数据。解题者通过学习成功和失败轨迹上的偏好反馈来不断改进其推理能力；教师根据解题者的弱点自适应地设计越来越具有挑战性的问题；生成器提炼教师的问题设计策略，以实现可扩展、高保真的课程生成。这个闭环系统产生了一个自我改进的课程，不需要预先存在的任务或标签。令人惊讶的是，从仅100个种子问题开始，我们的Socratic-Solver-8B在七个数学推理基准测试（AMC23、AIME24-25、奥林匹克、MATH-500、Minerva和GSM8K）上，比之前的数据合成方法平均提高了+20.2个百分点，并且在Qwen3和GLM4系列模型上都获得了持续的收益。更令人惊讶的是，来自Socratic-Generator-32B的合成数据使学生LLM能够在这些基准测试上实现优于其他最先进（SOTA）商业LLM的性能，包括Qwen3-235B-A22B、DeepSeek-V3.1-671B、GPT-5、Gemini-2.5-Pro、Grok-4和Claude-4.1-Opus。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在数学推理任务中对大规模高质量标注数据的依赖问题。现有数据合成方法的痛点在于生成的数据质量不稳定，难以适应模型能力的动态变化，导致训练效果不佳。

**核心思路**：论文的核心思路是通过构建一个自主的Agent协同进化框架，模拟苏格拉底式教学，让模型在与教师Agent的交互中不断学习和提升推理能力。教师Agent根据解题者Agent的弱点生成具有挑战性的问题，解题者Agent通过学习成功和失败的经验来改进自身，生成器Agent则负责提炼教师Agent的问题设计策略，从而实现可扩展的课程生成。

**技术框架**：Socratic-Zero框架包含三个主要模块：教师Agent、解题者Agent和生成器Agent。教师Agent负责根据解题者Agent的表现生成新的问题；解题者Agent负责解决教师Agent提出的问题，并根据反馈调整策略；生成器Agent负责学习教师Agent的问题生成策略，并生成大规模的训练数据。整个框架是一个闭环系统，三个Agent相互协作，共同提升LLM的推理能力。

**关键创新**：Socratic-Zero的关键创新在于其完全自主的Agent协同进化机制，无需人工标注数据，即可生成高质量的训练数据。通过教师Agent的自适应问题设计和解题者Agent的经验学习，Socratic-Zero能够有效地引导LLM学习复杂的推理技能。此外，生成器Agent的引入使得课程生成具有可扩展性，可以生成大规模的训练数据。

**关键设计**：论文中未明确给出关键参数设置、损失函数、网络结构等技术细节。但可以推断，教师Agent的问题生成策略可能涉及到基于规则或模型的生成方法，解题者Agent的学习可能采用强化学习或模仿学习等技术，生成器Agent可能采用蒸馏学习等方法。

## 📊 实验亮点

Socratic-Zero在七个数学推理基准测试中，比之前的数据合成方法平均提高了+20.2个百分点。使用Socratic-Generator-32B生成的合成数据训练的LLM，性能优于Qwen3-235B-A22B、DeepSeek-V3.1-671B等商业LLM，甚至可以媲美GPT-5、Gemini-2.5-Pro等模型，展示了强大的性能。

## 🎯 应用场景

Socratic-Zero具有广泛的应用前景，可用于提升LLM在数学、科学、逻辑等领域的推理能力。该方法可以降低LLM训练对大规模标注数据的依赖，降低训练成本，并促进LLM在资源受限环境下的应用。此外，该方法还可以应用于其他需要自主学习和知识发现的领域，例如机器人控制、自动驾驶等。

## 📄 摘要（原文）

> Recent breakthroughs in large language models (LLMs) on reasoning tasks rely heavily on massive, high-quality datasets-typically human-annotated and thus difficult to scale. While data synthesis or distillation offers a promising alternative, existing methods struggle with inconsistent data quality and an inability to dynamically adapt to the evolving capabilities of the model, leading to suboptimal training signals. To address these limitations, we introduce Socratic-Zero, a fully autonomous framework that generates high-quality training data from minimal seed examples through the co-evolution of three agents: the Teacher, the Solver, and the Generator. The Solver continuously refines its reasoning by learning from preference feedback on both successful and failed trajectories; the Teacher adaptively crafts increasingly challenging questions based on the Solver's weaknesses; and the Generator distills the Teacher's question-design strategy to enable scalable, high-fidelity curriculum generation. This closed-loop system produces a self-improving curriculum-requiring no pre-existing tasks or labels. Remarkably, starting from only 100 seed questions, our Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods across seven mathematical reasoning benchmarks (AMC23, AIME24-25, Olympiad, MATH-500, Minerva, and GSM8K), with consistent gains on both Qwen3 and GLM4 series models. Even more surprisingly, synthetic data from Socratic-Generator-32B enables student LLMs to achieve superior performance compared to other state-of-the-art (SOTA) commercial LLMs on these benchmarks, including Qwen3-235B-A22B, DeepSeek-V3.1-671B, GPT-5, Gemini-2.5-Pro, Grok-4, and Claude-4.1-Opus.

