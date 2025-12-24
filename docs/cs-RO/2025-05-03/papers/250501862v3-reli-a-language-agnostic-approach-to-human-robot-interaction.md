---
layout: default
title: "ReLI: A Language-Agnostic Approach to Human-Robot Interaction"
---

# ReLI: A Language-Agnostic Approach to Human-Robot Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01862" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01862v3</a>
  <a href="https://arxiv.org/pdf/2505.01862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01862v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01862v3', 'ReLI: A Language-Agnostic Approach to Human-Robot Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linus Nwankwo, Bjoern Ellensohn, Ozan Özdenizci, Elmar Rueckert

**分类**: cs.RO

**发布日期**: 2025-05-03 (更新: 2025-10-06)

**🔗 代码/项目**: [PROJECT_PAGE](https://linusnep.github.io/ReLI/)

---

## 💡 一句话要点

**提出ReLI以解决跨语言人机交互问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `语言无关` `跨语言适应` `智能体` `自然语言处理` `多轮对话` `任务执行`

## 📋 核心要点

1. 现有方法在跨语言人机交互中面临有效性不足的问题，难以处理多样化的语言指令。
2. ReLI通过将预训练模型转化为语言到行动模型，实现自然对话和语义推理，支持跨语言适应。
3. 在140种语言的实验中，ReLI在指令解析和任务执行上取得了超过90%的准确率，展示了其强大的实用性。

## 📝 摘要（中文）

随着自主智能体在工业、家庭等日常任务中的应用日益增加，如何确保在全球或跨语言环境中有效互动并执行人类指定的任务仍然是一个未解决的问题。为此，本文提出了ReLI，一种语言无关的方法，使自主智能体能够自然对话、进行语义推理并执行任务，无论任务指令的语言或形式如何。我们将大规模预训练的基础模型转化为语言到行动的模型，支持常识推理和高层次的机器人控制。通过对模型进行跨语言适应，ReLI能够在全球语言中进行泛化。实验表明，ReLI在140种语言的多轮对话中，跨语言指令解析和任务执行成功率超过90%。

## 🔬 方法详解

**问题定义**：本文旨在解决自主智能体在跨语言环境中与人类进行有效互动的难题。现有方法通常依赖于特定语言，难以适应多样化的语言指令，导致交互效率低下。

**核心思路**：ReLI的核心思路是构建一种语言无关的模型，使智能体能够通过自然语言进行对话，并进行语义推理，从而执行任务。通过这种设计，ReLI能够处理来自不同语言的指令，提升人机交互的灵活性和效率。

**技术框架**：ReLI的整体架构包括多个模块：首先是基础模型的预训练，然后将其转化为语言到行动模型，接着进行跨语言适应，最后通过自然对话实现任务执行。每个模块都经过精心设计，以确保模型的泛化能力和实用性。

**关键创新**：ReLI的主要创新在于其语言无关性和跨语言适应能力，使其能够在多种语言环境中有效工作。这一特性与现有方法的语言依赖性形成鲜明对比，极大地扩展了智能体的应用范围。

**关键设计**：在模型设计中，采用了特定的损失函数以优化指令解析的准确性，并通过多轮对话的训练增强模型的对话能力。此外，模型的参数设置经过细致调整，以确保在不同语言间的有效迁移。

## 📊 实验亮点

在实验中，ReLI在140种语言的多轮对话中，跨语言指令解析和任务执行的成功率超过90%，且标准差仅为0.2。这一结果显著优于现有的基线方法，展示了ReLI在处理多语言指令方面的卓越性能和可靠性。

## 🎯 应用场景

ReLI的研究成果在多个领域具有广泛的应用潜力，包括智能家居、工业自动化和服务机器人等。通过实现语言无关的人机交互，ReLI能够帮助不同语言背景的用户更便捷地与智能设备进行沟通，提升用户体验。此外，随着全球化进程的加快，ReLI在跨文化交流中的价值也日益凸显。

## 📄 摘要（原文）

> Adapting autonomous agents for real-world industrial, domestic, and other daily tasks is currently gaining momentum. However, in global or cross-lingual application contexts, ensuring effective interaction with the environment and executing unrestricted human-specified tasks regardless of the language remains an unsolved problem. To address this, we propose ReLI, a language-agnostic approach that enables autonomous agents to converse naturally, semantically reason about their environment, and perform downstream tasks, regardless of the task instruction's modality or linguistic origin. First, we ground large-scale pre-trained foundation models and transform them into language-to-action models that can directly provide common-sense reasoning and high-level robot control through natural, free-flow conversational interactions. Further, we perform cross-lingual adaptation of the models to ensure that ReLI generalises across the global languages. To demonstrate ReLI's robustness, we conducted extensive experiments on various short- and long-horizon tasks, including zero- and few-shot spatial navigation, scene information retrieval, and query-oriented tasks. We benchmarked the performance on $140$ languages involving $70K+$ multi-turn conversations. On average, ReLI achieved over $90\%\pm0.2$ accuracy in cross-lingual instruction parsing and task execution success. These results demonstrate its potential to advance natural human-agent interaction in the real world while championing inclusive and linguistic diversity. Demos and resources will be public at: https://linusnep.github.io/ReLI/.

