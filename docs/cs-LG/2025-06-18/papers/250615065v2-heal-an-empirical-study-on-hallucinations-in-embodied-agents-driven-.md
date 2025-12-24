---
layout: default
title: "HEAL: An Empirical Study on Hallucinations in Embodied Agents Driven by Large Language Models"
---

# HEAL: An Empirical Study on Hallucinations in Embodied Agents Driven by Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15065" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15065v2</a>
  <a href="https://arxiv.org/pdf/2506.15065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15065v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15065v2', 'HEAL: An Empirical Study on Hallucinations in Embodied Agents Driven by Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Trishna Chakraborty, Udita Ghosh, Xiaopan Zhang, Fahim Faisal Niloy, Yue Dong, Jiachen Li, Amit K. Roy-Chowdhury, Chengyu Song

**分类**: cs.LG, cs.RO

**发布日期**: 2025-06-18 (更新: 2025-10-14)

**备注**: Accepted by EMNLP 2025 Findings

---

## 💡 一句话要点

**提出系统性研究以解决大语言模型驱动的具身智能体的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能体` `大语言模型` `幻觉现象` `场景与任务不一致` `系统性研究` `模型评估` `导航错误`

## 📋 核心要点

1. 现有的具身智能体在处理用户指令时，常因未能将指令与观察到的物理环境相结合而产生幻觉，导致导航错误。
2. 论文通过构建一个新的探测集，系统性地评估了幻觉现象的发生情况及其触发因素，旨在揭示模型的局限性。
3. 实验结果显示，尽管模型在推理上表现出色，但在面对场景与任务不一致时，仍无法有效解决问题，突显了其基本局限性。

## 📝 摘要（中文）

随着大语言模型（LLMs）逐渐成为具身智能体的认知核心，幻觉现象的出现引发了导航错误，例如寻找不存在的冰箱。本文首次系统性研究了在场景与任务不一致情况下，LLM驱动的具身智能体在执行长时间任务时的幻觉现象。研究旨在探讨幻觉的发生程度、触发类型及当前模型的响应。通过构建一个能够诱发高达40倍幻觉率的探测集，评估了12个模型在两个模拟环境中的表现，发现模型在推理上表现良好，但在处理不可行任务时存在根本性局限。我们还提供了针对每种场景的理想模型行为的可操作性见解，以指导更稳健的规划策略的开发。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型驱动的具身智能体在执行长时间任务时因场景与任务不一致而产生的幻觉问题。现有方法在处理用户指令与物理环境的结合上存在明显不足，导致导航错误。

**核心思路**：论文的核心思路是通过构建一个新的幻觉探测集，系统性地评估不同模型在面对场景与任务不一致时的表现，揭示其局限性并提供改进建议。

**技术框架**：研究采用了两个模拟环境，评估了12个不同的模型。探测集设计旨在诱发高达40倍的幻觉率，以便深入分析模型的反应和推理能力。

**关键创新**：本研究的关键创新在于首次系统性地探讨了LLM驱动的具身智能体的幻觉现象，并提供了针对不同场景的理想模型行为指导，这在现有文献中尚属首次。

**关键设计**：在实验中，设计了特定的参数设置和评估标准，以确保探测集的有效性和模型评估的准确性，具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，尽管模型在推理方面表现良好，但在处理场景与任务不一致时，幻觉现象的发生率高达40倍，显示出当前模型在应对复杂任务时的基本局限性。这一发现为未来模型的改进提供了重要的参考依据。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、服务机器人及虚拟助手等，能够帮助提升具身智能体在复杂环境中的导航和任务执行能力。通过减少幻觉现象，未来的智能体将更加可靠，能够更好地理解和执行用户指令，从而提高用户体验。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly being adopted as the cognitive core of embodied agents. However, inherited hallucinations, which stem from failures to ground user instructions in the observed physical environment, can lead to navigation errors, such as searching for a refrigerator that does not exist. In this paper, we present the first systematic study of hallucinations in LLM-based embodied agents performing long-horizon tasks under scene-task inconsistencies. Our goal is to understand to what extent hallucinations occur, what types of inconsistencies trigger them, and how current models respond. To achieve these goals, we construct a hallucination probing set by building on an existing benchmark, capable of inducing hallucination rates up to 40x higher than base prompts. Evaluating 12 models across two simulation environments, we find that while models exhibit reasoning, they fail to resolve scene-task inconsistencies-highlighting fundamental limitations in handling infeasible tasks. We also provide actionable insights on ideal model behavior for each scenario, offering guidance for developing more robust and reliable planning strategies.

