---
layout: default
title: LongVideoAgent: Multi-Agent Reasoning with Long Videos
---

# LongVideoAgent: Multi-Agent Reasoning with Long Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20618" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20618v1</a>
  <a href="https://arxiv.org/pdf/2512.20618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20618v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20618v1', 'LongVideoAgent: Multi-Agent Reasoning with Long Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runtao Liu, Ziyi Liu, Jiaqi Tang, Yue Ma, Renjie Pi, Jipeng Zhang, Qifeng Chen

**分类**: cs.AI, cs.CV, cs.LG, cs.MA

**发布日期**: 2025-12-23

**🔗 代码/项目**: [PROJECT_PAGE](https://longvideoagent.github.io/)

---

## 💡 一句话要点

**LongVideoAgent：提出一种基于多智能体推理的长视频问答框架，提升时序定位和细节捕捉能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频问答` `多智能体系统` `强化学习` `时序定位` `视觉信息提取`

## 📋 核心要点

1. 现有长视频问答方法依赖有损压缩或有限的工具集，削弱了时序定位能力，并可能遗漏细粒度的线索。
2. 提出一种多智能体框架，利用 grounding agent 定位相关片段，vision agent 提取视觉细节，主 LLM 协调推理。
3. 在 LongTVQA 和 LongTVQA+ 数据集上，该方法显著优于非智能体基线，且强化学习能进一步提升推理和规划能力。

## 📝 摘要（中文）

本文提出了一种多智能体框架，用于处理长视频问答任务。该框架由一个主LLM协调，一个负责定位问题相关片段的 grounding agent 和一个提取目标文本观测的 vision agent。主智能体在步数限制下进行规划，并通过强化学习进行训练，以鼓励简洁、正确和高效的多智能体协作。这种设计通过 grounding 帮助主智能体专注于相关片段，利用视觉细节补充字幕信息，并产生可解释的推理轨迹。在从 TVQA/TVQA+ 聚合而来的 episode-level 数据集 LongTVQA 和 LongTVQA+ 上，我们的多智能体系统显著优于强大的非智能体基线。实验还表明，强化学习进一步加强了训练后智能体的推理和规划能力。代码和数据将在 https://longvideoagent.github.io/ 上共享。

## 🔬 方法详解

**问题定义**：长视频问答任务需要模型具备在长时间跨度内进行推理的能力。现有方法通常采用有损的视频摘要或依赖有限的工具集，导致时序定位精度下降，无法捕捉视频中的细粒度信息，从而影响问答效果。

**核心思路**：论文的核心思路是将长视频问答任务分解为多个智能体协作完成。通过引入 grounding agent 和 vision agent，分别负责定位相关视频片段和提取视觉信息，从而减轻主 LLM 的负担，使其能够更专注于推理和规划。这种分工协作的方式能够更有效地利用视频信息，提高问答的准确性。

**技术框架**：LongVideoAgent 框架包含三个主要模块：主 LLM、grounding agent 和 vision agent。主 LLM 负责接收问题，协调其他智能体的工作，并最终生成答案。grounding agent 负责根据问题定位视频中相关的片段。vision agent 负责从定位到的视频片段中提取视觉信息，例如场景描述、物体识别等。整个流程如下：主 LLM 接收问题 -> 主 LLM 调用 grounding agent 定位相关片段 -> 主 LLM 调用 vision agent 提取视觉信息 -> 主 LLM 结合问题、定位片段和视觉信息进行推理 -> 主 LLM 生成答案。

**关键创新**：该方法最重要的创新点在于提出了一个多智能体协作的框架，将长视频问答任务分解为多个子任务，并由不同的智能体负责完成。这种分工协作的方式能够更有效地利用视频信息，提高问答的准确性。与现有方法相比，该方法不需要对视频进行有损压缩，能够保留更多的细节信息。此外，通过强化学习训练主 LLM，能够进一步提高其推理和规划能力。

**关键设计**：主 LLM 使用预训练的 LLM，并进行微调以适应长视频问答任务。Grounding agent 和 vision agent 可以使用现有的目标检测、视频分割等模型。强化学习的目标是鼓励主 LLM 进行简洁、正确和高效的多智能体协作。奖励函数可以设计为基于答案的准确性、使用的步数等因素。步数限制是为了防止主 LLM 无限循环调用其他智能体。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20618v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20618v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在 LongTVQA 和 LongTVQA+ 数据集上，LongVideoAgent 显著优于非智能体基线。具体而言，LongVideoAgent 在 LongTVQA 数据集上取得了 X% 的提升，在 LongTVQA+ 数据集上取得了 Y% 的提升（具体数值未知）。此外，实验还表明，通过强化学习训练主 LLM，能够进一步提高其推理和规划能力。

## 🎯 应用场景

该研究成果可应用于智能客服、视频内容理解、智能安防等领域。例如，在智能客服中，可以利用该方法对用户上传的视频进行分析，快速定位问题并给出解答。在视频内容理解中，可以用于自动生成视频摘要、视频标签等。在智能安防中，可以用于监控视频分析，自动识别异常行为。

## 📄 摘要（原文）

> Recent advances in multimodal LLMs and systems that use tools for long-video QA point to the promise of reasoning over hour-long episodes. However, many methods still compress content into lossy summaries or rely on limited toolsets, weakening temporal grounding and missing fine-grained cues. We propose a multi-agent framework in which a master LLM coordinates a grounding agent to localize question-relevant segments and a vision agent to extract targeted textual observations. The master agent plans with a step limit, and is trained with reinforcement learning to encourage concise, correct, and efficient multi-agent cooperation. This design helps the master agent focus on relevant clips via grounding, complements subtitles with visual detail, and yields interpretable trajectories. On our proposed LongTVQA and LongTVQA+ which are episode-level datasets aggregated from TVQA/TVQA+, our multi-agent system significantly outperforms strong non-agent baselines. Experiments also show reinforcement learning further strengthens reasoning and planning for the trained agent. Code and data will be shared at https://longvideoagent.github.io/.

