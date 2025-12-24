---
layout: default
title: Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents
---

# Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13652" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13652v1</a>
  <a href="https://arxiv.org/pdf/2505.13652.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13652v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13652v1', 'Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karina Zainullina, Alexander Golubev, Maria Trofimova, Sergei Polezhaev, Ibragim Badertdinov, Daria Litvintseva, Simon Karasik, Filipp Fisin, Sergei Skvortsov, Maksim Nekrashevich, Anton Shevtsov, Boris Yangel

**分类**: cs.SE, cs.CL

**发布日期**: 2025-05-19

**备注**: ICML

---

## 💡 一句话要点

**提出引导搜索策略以解决非可序列化环境中的软件工程问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `引导搜索` `非可序列化环境` `软件工程` `强化学习` `动作价值函数` `轨迹选择` `一步前瞻`

## 📋 核心要点

1. 现有的大型语言模型在多步骤任务中表现不稳定，难以保持一致的性能。
2. 本文提出的解决方案包括一步前瞻和轨迹选择两种搜索策略，以引导模型在非可序列化环境中进行有效搜索。
3. 实验结果表明，所提方法使Qwen-72B模型的成功率提升至40.8%，并且可迁移至GPT-4o等更先进模型。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂的多步骤任务中取得了显著成果，但在多次解决尝试中往往难以保持一致的性能。为缩小平均性能与最佳性能之间的差距，本文提出了引导测试时搜索的方法，探索多个解决路径以识别最有前景的方案。针对非可序列化的强化学习环境（如Docker容器），我们研究了两种互补的搜索策略：一步前瞻和轨迹选择，均由学习的动作价值函数估计器引导。在SWE-bench Verified基准测试中，这些方法使得微调后的Qwen-72B模型的平均成功率翻倍，达到了40.8%，创下了开放权重模型的新状态。此外，我们还展示了这些技术可以转移到更先进的封闭模型上，取得类似的改进效果。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在非可序列化环境中进行多步骤任务时的性能不稳定问题。现有的有效搜索技术（如MCTS）在这类环境中难以应用，因为中间状态无法轻易保存和恢复。

**核心思路**：论文提出了两种引导搜索策略：一步前瞻和轨迹选择，利用学习的动作价值函数估计器来指导搜索过程，以提高模型在复杂环境中的表现。

**技术框架**：整体架构包括两个主要模块：首先，使用动作价值函数估计器评估不同的动作选择；其次，基于评估结果进行一步前瞻或轨迹选择，从而探索最有潜力的解决路径。

**关键创新**：最重要的技术创新在于提出了适用于非可序列化环境的引导搜索策略，这与传统的搜索方法形成了鲜明对比，后者通常依赖于可序列化的状态管理。

**关键设计**：在设计中，采用了特定的损失函数来优化动作价值函数估计器，并在网络结构上进行了调整，以适应非可序列化环境的特点。

## 📊 实验亮点

实验结果显示，所提出的引导搜索策略使得微调后的Qwen-72B模型的平均成功率从20.4%提升至40.8%，实现了显著的性能提升。此外，这些技术在更先进的封闭模型GPT-4o上也取得了类似的改进效果，展示了其广泛的适用性。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程中的自动化工具、智能代理系统以及需要在复杂环境中进行决策的其他领域。通过提高模型在非可序列化环境中的表现，能够显著提升软件开发和维护的效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have recently achieved remarkable results in complex multi-step tasks, such as mathematical reasoning and agentic software engineering. However, they often struggle to maintain consistent performance across multiple solution attempts. One effective approach to narrow the gap between average-case and best-case performance is guided test-time search, which explores multiple solution paths to identify the most promising one. Unfortunately, effective search techniques (e.g. MCTS) are often unsuitable for non-serializable RL environments, such as Docker containers, where intermediate environment states cannot be easily saved and restored. We investigate two complementary search strategies applicable to such environments: 1-step lookahead and trajectory selection, both guided by a learned action-value function estimator. On the SWE-bench Verified benchmark, a key testbed for agentic software engineering, we find these methods to double the average success rate of a fine-tuned Qwen-72B model, achieving 40.8%, the new state-of-the-art for open-weights models. Additionally, we show that these techniques are transferable to more advanced closed models, yielding similar improvements with GPT-4o.

