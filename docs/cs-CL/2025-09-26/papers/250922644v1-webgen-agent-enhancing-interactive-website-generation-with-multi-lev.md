---
layout: default
title: "WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning"
---

# WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22644" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22644v1</a>
  <a href="https://arxiv.org/pdf/2509.22644.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22644v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22644v1', 'WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zimu Lu, Houxing Ren, Yunqiao Yang, Ke Wang, Zhuofan Zong, Junting Pan, Mingjie Zhan, Hongsheng Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**WebGen-Agent：通过多层次反馈和步级强化学习增强交互式网站生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网站生成` `大型语言模型` `视觉语言模型` `强化学习` `多层次反馈` `交互式应用` `代码生成Agent`

## 📋 核心要点

1. 现有代码Agent在网站代码库生成任务中，仅依赖简单的代码执行进行反馈和验证，无法捕捉生成代码的实际质量，尤其是在视觉效果和用户交互方面。
2. WebGen-Agent利用视觉语言模型生成网站截图和GUI-Agent测试的文本描述和质量评分，并结合回溯和选择机制，迭代优化网站代码库。
3. 通过Step-GRPO，利用截图和GUI-Agent分数作为奖励，为LLM提供密集的过程监督信号，显著提升了模型在WebGen-Bench数据集上的网站生成准确率和外观分数。

## 📝 摘要（中文）

本文提出WebGen-Agent，一种新型网站生成Agent，它利用全面和多层次的视觉反馈来迭代地生成和改进网站代码库。视觉语言模型(VLM)生成关于网站截图和GUI-Agent测试的详细和富有表现力的文本描述和建议，以及量化其质量的分数。截图和GUI-Agent分数与回溯和选择最佳机制相结合，增强了Agent的性能。利用WebGen-Agent工作流程中固有的准确视觉分数，进一步引入了*带有截图和GUI-Agent反馈的Step-GRPO*，以提高LLM作为WebGen-Agent推理引擎的能力。通过使用每一步的截图和GUI-Agent分数作为Step-GRPO中的奖励，提供了密集且可靠的过程监督信号，有效地提高了模型的网站生成能力。在WebGen-Bench数据集上，WebGen-Agent将Claude-3.5-Sonnet的准确率从26.4%提高到51.9%，外观分数从3.0提高到3.9，优于先前的最先进的Agent系统。此外，Step-GRPO训练方法将Qwen2.5-Coder-7B-Instruct的准确率从38.9%提高到45.4%，并将外观分数从3.4提高到3.7。

## 🔬 方法详解

**问题定义**：现有基于大型语言模型的代码生成Agent在网站代码库生成任务中，主要依赖代码执行结果进行反馈，缺乏对视觉效果和用户交互的有效评估。这导致生成的网站在用户体验和视觉呈现方面存在不足。现有方法无法充分利用视觉信息来指导代码生成过程，从而限制了生成网站的质量。

**核心思路**：WebGen-Agent的核心思路是引入多层次的视觉反馈机制，利用视觉语言模型(VLM)对生成的网站截图和GUI-Agent测试结果进行分析，生成详细的文本描述和质量评分。这些视觉反馈信息被用于指导代码的迭代优化，并作为强化学习的奖励信号，从而提高网站生成的质量和用户体验。

**技术框架**：WebGen-Agent的整体框架包含以下几个主要模块：1) 代码生成模块：利用LLM生成网站代码。2) 视觉反馈模块：使用VLM对生成的网站截图和GUI-Agent测试结果进行分析，生成文本描述和质量评分。3) 代码优化模块：根据视觉反馈信息，利用回溯和选择机制，迭代优化网站代码。4) 强化学习模块：使用Step-GRPO算法，利用视觉反馈分数作为奖励信号，训练LLM，提高其网站生成能力。

**关键创新**：WebGen-Agent的关键创新在于引入了多层次的视觉反馈机制，将视觉信息融入到网站代码生成过程中。与传统的仅依赖代码执行结果的反馈方式相比，WebGen-Agent能够更全面地评估网站的质量，并提供更有效的指导信息。此外，Step-GRPO算法的引入，使得LLM能够更好地利用视觉反馈信息，提高网站生成能力。

**关键设计**：在视觉反馈模块中，VLM被用于生成网站截图和GUI-Agent测试结果的文本描述和质量评分。质量评分可以包括外观分数、功能分数等。在Step-GRPO算法中，截图和GUI-Agent分数被用作每一步的奖励信号，以提供密集的过程监督。具体损失函数未知，但目标是最大化累积奖励，即提高生成的网站的整体质量。

## 📊 实验亮点

WebGen-Agent在WebGen-Bench数据集上取得了显著的性能提升。使用Claude-3.5-Sonnet作为基础模型时，准确率从26.4%提高到51.9%，外观分数从3.0提高到3.9，超越了之前的SOTA模型。通过Step-GRPO训练，Qwen2.5-Coder-7B-Instruct的准确率从38.9%提升至45.4%，外观分数从3.4提升至3.7，验证了该方法的有效性。

## 🎯 应用场景

WebGen-Agent可应用于各种交互式网站的自动生成，例如电商网站、博客平台、企业官网等。该技术能够降低网站开发成本，提高开发效率，并改善用户体验。未来，该技术有望扩展到更复杂的Web应用和移动应用开发领域，实现更智能化的代码生成和优化。

## 📄 摘要（原文）

> Agent systems powered by large language models (LLMs) have demonstrated impressive performance on repository-level code-generation tasks. However, for tasks such as website codebase generation, which depend heavily on visual effects and user-interaction feedback, current code agents rely only on simple code execution for feedback and verification. This approach fails to capture the actual quality of the generated code. In this paper, we propose WebGen-Agent, a novel website-generation agent that leverages comprehensive and multi-level visual feedback to iteratively generate and refine the website codebase. Detailed and expressive text descriptions and suggestions regarding the screenshots and GUI-agent testing of the websites are generated by a visual language model (VLM), together with scores that quantify their quality. The screenshot and GUI-agent scores are further integrated with a backtracking and select-best mechanism, enhancing the performance of the agent. Utilizing the accurate visual scores inherent in the WebGen-Agent workflow, we further introduce \textit{Step-GRPO with Screenshot and GUI-agent Feedback} to improve the ability of LLMs to act as the reasoning engine of WebGen-Agent. By using the screenshot and GUI-agent scores at each step as the reward in Step-GRPO, we provide a dense and reliable process supervision signal, which effectively improves the model's website-generation ability. On the WebGen-Bench dataset, WebGen-Agent increases the accuracy of Claude-3.5-Sonnet from 26.4% to 51.9% and its appearance score from 3.0 to 3.9, outperforming the previous state-of-the-art agent system. Additionally, our Step-GRPO training approach increases the accuracy of Qwen2.5-Coder-7B-Instruct from 38.9% to 45.4% and raises the appearance score from 3.4 to 3.7.

