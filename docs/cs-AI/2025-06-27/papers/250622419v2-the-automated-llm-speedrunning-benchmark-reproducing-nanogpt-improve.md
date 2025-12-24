---
layout: default
title: "The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements"
---

# The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22419" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22419v2</a>
  <a href="https://arxiv.org/pdf/2506.22419.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22419v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22419v2', 'The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingchen Zhao, Despoina Magka, Minqi Jiang, Xian Li, Roberta Raileanu, Tatiana Shavrina, Jean-Christophe Gagnon-Audet, Kelvin Niu, Shagun Sodhani, Michael Shvartsman, Andrei Lupu, Alisia Lupidi, Edan Toledo, Karen Hambardzumyan, Martin Josifoski, Thomas Foster, Lucia Cipolina-Kun, Abhishek Charnalia, Derek Dunfield, Alexander H. Miller, Oisin Mac Aodha, Jakob Foerster, Yoram Bachrach

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-27 (更新: 2025-06-30)

---

## 💡 一句话要点

**提出自动化LLM速度竞赛基准以解决科学重现性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `科学重现性` `自动化基准` `NanoGPT` `AI代理`

## 📋 核心要点

1. 核心问题：现有的AI代理在重现科学研究成果方面存在显著挑战，尤其是在复杂的研究领域中。
2. 方法要点：论文提出了自动化LLM速度竞赛基准，通过19个任务评估AI代理的重现能力，结合多种提示格式。
3. 实验或效果：研究发现，尽管提供详细提示，现有LLMs在重现已知创新时表现不佳，显示出该领域的研究空白。

## 📝 摘要（中文）

大型语言模型（LLMs）的快速进展有助于科学进步，而重现已有研究成果的能力是关键。本文引入了自动化LLM速度竞赛基准，基于NanoGPT速度竞赛的贡献，评估AI代理在活跃研究领域重现结果的能力。19个速度竞赛任务为代理提供了先前记录的训练脚本，并可选择性地配对三种提示格式。记录设计为快速执行，速度竞赛的改进涵盖了从高层算法到硬件优化的多样化代码级变化。研究发现，尽管提供详细提示，近期的推理LLMs结合最先进的框架在重现已知创新方面仍存在困难。该基准为评估LLMs自动化科学重现能力提供了简单且有效的度量。

## 🔬 方法详解

**问题定义**：本文旨在解决AI代理在科学研究中重现已有成果的能力不足的问题。现有方法在复杂的研究任务中，尤其是涉及多种算法和优化时，表现不佳。

**核心思路**：论文的核心思路是通过引入自动化LLM速度竞赛基准，利用已有的NanoGPT速度竞赛成果，评估AI代理在重现研究结果方面的能力。设计上，基准任务结合了多种提示格式，以帮助代理更好地理解和执行任务。

**技术框架**：整体架构包括19个速度竞赛任务，每个任务提供先前的训练记录和可选的提示格式。任务设计为快速执行，涵盖了从算法到硬件优化的多样化改进。

**关键创新**：最重要的技术创新在于构建了一个简单且非饱和的基准，专注于评估LLMs在科学重现中的自动化能力，这与现有的重现性评估方法有本质区别。

**关键设计**：在设计中，任务的提示格式包括伪代码和论文式描述，旨在提供足够的信息以帮助代理理解任务，同时保持任务的多样性和挑战性。

## 📊 实验亮点

实验结果显示，尽管提供了详细的提示，现有的推理LLMs在重现已知创新方面仍然面临困难。这一发现强调了当前技术在科学重现性任务中的局限性，为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究、教育和AI辅助的自动化实验室。通过提高AI在重现性方面的能力，可以加速科学发现和技术创新，推动各领域的研究进展。

## 📄 摘要（原文）

> Rapid advancements in large language models (LLMs) have the potential to assist in scientific progress. A critical capability toward this endeavor is the ability to reproduce existing work. To evaluate the ability of AI agents to reproduce results in an active research area, we introduce the Automated LLM Speedrunning Benchmark, leveraging the research community contributions on the NanoGPT speedrun, a competition to train a GPT-2 model in the shortest time. Each of the 19 speedrun tasks provides the agent with the previous records training script, optionally paired with one of three hint formats, ranging from pseudocode to paper-like descriptions of the new records improvements. Records execute quickly by design and speedrun improvements encompass diverse code-level changes, ranging from high-level algorithmic advancements to hardware-aware optimizations. These features make the benchmark both accessible and realistic for the frontier problem of improving LLM training. We find that recent reasoning LLMs combined with SoTA scaffolds struggle to reimplement already-known innovations in our benchmark, even when given detailed hints. Our benchmark thus provides a simple, non-saturated measure of an LLMs ability to automate scientific reproduction, a necessary (but not sufficient) skill for an autonomous research agent.

