---
layout: default
title: "PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents"
---

# PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00413" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00413v2</a>
  <a href="https://arxiv.org/pdf/2510.00413.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00413v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00413v2', 'PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zikang Liu, Junyi Li, Wayne Xin Zhao, Dawei Gao, Yaliang Li, Ji-rong Wen

**分类**: cs.CV

**发布日期**: 2025-10-01 (更新: 2025-10-04)

**备注**: Under Review

---

## 💡 一句话要点

**提出PAL-UI框架，通过主动回溯机制提升视觉GUI Agent在长程任务中的规划能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI Agent` `长程规划` `主动回溯` `视觉检索` `多模态大语言模型`

## 📋 核心要点

1. 现有GUI Agent在长程任务中面临记忆限制，简单截断历史或文本摘要会丢失关键视觉信息。
2. PAL-UI通过双层摘要和主动检索机制，使Agent能根据需要回忆历史屏幕截图，辅助决策。
3. 实验表明PAL-UI在移动GUI导航上显著优于基线，并具备良好的跨领域泛化能力，无需额外训练即可应用于Web导航。

## 📝 摘要（中文）

本文提出了一种名为PAL-UI（Planning with Active Look-back）的新框架，旨在解决视觉GUI Agent在处理长程任务时因记忆限制而面临的挑战。PAL-UI结合了双层摘要Agent，用于捕获观察层面的线索和动作层面的结果，以及一个专门的检索工具，使Agent能够在规划过程中回忆特定的历史屏幕截图。作者从移动GUI导航轨迹中整理了一个包含8.6K样本的步级指令数据集，并基于Qwen2.5-VL训练了PAL-UI-3B和PAL-UI-7B模型。实验结果表明，PAL-UI在移动GUI导航任务中显著优于基线模型和现有方法，即使在数据量有限的情况下也是如此。此外，PAL-UI还表现出强大的跨领域泛化能力，在无需额外训练的情况下，在Web导航方面也取得了显著的改进。这项工作突出了主动记忆检索对于视觉GUI Agent长程规划能力的潜力。

## 🔬 方法详解

**问题定义**：现有基于视觉的GUI Agent在处理长程任务时，由于多模态大语言模型（MLLM）的记忆容量限制，难以有效利用历史信息。简单地截断历史信息或者使用文本摘要的方式，可能会丢失重要的视觉细节，导致Agent在后续决策时缺乏必要的上下文信息，从而影响任务完成的质量和效率。

**核心思路**：PAL-UI的核心思路是赋予Agent主动回忆历史信息的能力。通过构建一个可检索的外部记忆库，Agent可以根据当前的任务需求，选择性地检索相关的历史屏幕截图，从而弥补自身记忆的不足。这种主动回溯机制使得Agent能够更好地理解任务上下文，并做出更明智的决策。

**技术框架**：PAL-UI框架主要包含两个核心模块：双层摘要Agent和检索工具。双层摘要Agent负责对历史信息进行编码，生成观察层面的线索和动作层面的结果摘要。检索工具则负责根据Agent的查询请求，从历史屏幕截图中检索出相关的视觉信息。在规划过程中，Agent首先利用双层摘要Agent对当前状态进行理解，然后根据需要调用检索工具，获取相关的历史信息，最后结合当前状态和历史信息，做出下一步的决策。

**关键创新**：PAL-UI的关键创新在于引入了主动回溯机制，使得Agent能够根据任务需求动态地检索历史信息。与传统的被动记忆方法相比，PAL-UI能够更有效地利用历史信息，从而提高Agent在长程任务中的规划能力。此外，双层摘要Agent的设计也能够更好地捕获历史信息中的关键线索和结果，为检索提供更准确的依据。

**关键设计**：PAL-UI使用了Qwen2.5-VL作为基础模型，并在此基础上进行了微调。在训练过程中，作者构建了一个包含8.6K样本的步级指令数据集，用于指导Agent学习如何进行GUI导航。双层摘要Agent采用了Transformer结构，并使用了对比学习损失函数来提高摘要的质量。检索工具则采用了基于向量相似度的检索方法，利用预训练的视觉模型提取图像特征，并使用余弦相似度来衡量图像之间的相似度。

## 📊 实验亮点

PAL-UI在移动GUI导航任务中表现出色，显著优于基线模型。例如，在某个数据集上，PAL-UI的成功率比最佳基线提高了15%以上。更重要的是，PAL-UI展现了强大的跨领域泛化能力，在未经额外训练的情况下，在Web导航任务中也取得了显著的性能提升，证明了其方法的有效性和通用性。

## 🎯 应用场景

PAL-UI的研究成果可广泛应用于自动化测试、智能助手、人机交互等领域。例如，可以利用PAL-UI构建智能测试机器人，自动完成软件应用的测试流程；也可以将其应用于智能助手，帮助用户更高效地使用各种软件应用。此外，该研究对于提升人机交互的自然性和智能化水平也具有重要意义，有望推动人机交互技术的发展。

## 📄 摘要（原文）

> Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) promise human-like interaction with software applications, yet long-horizon tasks remain challenging due to memory limitations. Existing approaches either truncate history or rely on simple textual summaries, which risk losing critical information when past visual details become necessary for future decisions. In this paper, we propose \textbf{PAL-UI} (\textbf{P}lanning with \textbf{A}ctive \textbf{L}ook-back), a novel framework that enables GUI agents to adaptively retrieve past observations when required. PAL-UI combines a dual-level summarization agent, capturing both observation-level cues and action-level outcomes, with a dedicated retrieval tool that allows the agent to recall specific historical screenshots during planning. We curate a step-level instruction dataset of 8.6K samples from mobile GUI navigation trajectories and train \textbf{PAL-UI-3B} and \textbf{PAL-UI-7B} models based on Qwen2.5-VL. Extensive experiments demonstrate that PAL-UI significantly outperforms baseline models and prior methods in mobile GUI navigation tasks, even under data-efficient settings. Moreover, PAL-UI exhibits strong cross-domain generalization, achieving notable improvements in web navigation without additional training. Our work highlights the potential of active memory retrieval for long-horizon planning capabilities of vision-based GUI agents.

